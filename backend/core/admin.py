from django.contrib import admin
from .models import Donor, NGOCampaign, Volunteer

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "total_donated", "donations_count", "created_at"]
    list_filter = ["donor_type", "status"]
    search_fields = ["name", "email", "phone"]

@admin.register(NGOCampaign)
class NGOCampaignAdmin(admin.ModelAdmin):
    list_display = ["title", "goal_amount", "raised_amount", "donors_count", "status", "created_at"]
    list_filter = ["status"]
    search_fields = ["title"]

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "skills", "hours_contributed", "created_at"]
    list_filter = ["status", "availability"]
    search_fields = ["name", "email", "phone"]
