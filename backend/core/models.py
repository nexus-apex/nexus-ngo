from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    total_donated = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    donations_count = models.IntegerField(default=0)
    donor_type = models.CharField(max_length=50, choices=[("individual", "Individual"), ("corporate", "Corporate"), ("foundation", "Foundation")], default="individual")
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("lapsed", "Lapsed")], default="active")
    last_donation = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class NGOCampaign(models.Model):
    title = models.CharField(max_length=255)
    goal_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    raised_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    donors_count = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("completed", "Completed"), ("paused", "Paused")], default="active")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Volunteer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    skills = models.CharField(max_length=255, blank=True, default="")
    hours_contributed = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("inactive", "Inactive"), ("pending", "Pending")], default="active")
    availability = models.CharField(max_length=50, choices=[("weekdays", "Weekdays"), ("weekends", "Weekends"), ("flexible", "Flexible")], default="weekdays")
    joined_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
