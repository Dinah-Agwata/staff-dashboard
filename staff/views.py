import csv

from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import get_user_model


from .models import Event
from .forms import StaffActivityFilterForm

User = get_user_model()


@login_required
def staff_activity_dashboard(request):
    user = request.user
    organization = user.organization

    # Time boundary. Dashboard defaults to current month activity
    today = timezone.now()
    start_of_month = today.replace(day=1)

    # Base queryset
    queryset = (
        User.objects
        .filter(organization=organization)
        .annotate(
            total_events=Count(
                "events",
                filter=Q(events__created_at__gte=start_of_month)
            )
        )
    )

    # Filter form
    form = StaffActivityFilterForm(request.GET or None)

    if form.is_valid():
        role = form.cleaned_data.get("role")
        status = form.cleaned_data.get("status")
        start_date = form.cleaned_data.get("start_date")
        end_date = form.cleaned_data.get("end_date")

        if role:
            queryset = queryset.filter(role=role)

        if status == "active":
            queryset = queryset.filter(is_active=True)
        elif status == "inactive":
            queryset = queryset.filter(is_active=False)

        if start_date and end_date:
            queryset = queryset.annotate(
                total_events=Count(
                    "events",
                    filter=Q(events__created_at__range=(start_date, end_date))
                )
            )

    # Sorting
    sort = request.GET.get("sort")
    if sort == "name":
        queryset = queryset.order_by("first_name")
    elif sort == "events":
        queryset = queryset.order_by("-total_events")

    # CSV Export
    if "export" in request.GET:
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="staff_activity.csv"'

        writer = csv.writer(response)
        writer.writerow(["Name", "Role", "Total Events", "Last Login", "Status"])

        for staff in queryset:
            writer.writerow([
                staff.get_full_name(),
                staff.role,
                staff.total_events,
                staff.last_login,
                "Active" if staff.is_active else "Inactive"
            ])

        return response

    context = {
        "staff_list": queryset,
        "form": form,
        "user": user,
        "organization": organization
    }

    return render(request, "staff/staff_activity_dashboard.html", context)
