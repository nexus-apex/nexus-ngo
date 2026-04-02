from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Donor, NGOCampaign, Volunteer
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusNGO with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusngo.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Donor.objects.count() == 0:
            for i in range(10):
                Donor.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    total_donated=round(random.uniform(1000, 50000), 2),
                    donations_count=random.randint(1, 100),
                    donor_type=random.choice(["individual", "corporate", "foundation"]),
                    status=random.choice(["active", "lapsed"]),
                    last_donation=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 Donor records created'))

        if NGOCampaign.objects.count() == 0:
            for i in range(10):
                NGOCampaign.objects.create(
                    title=f"Sample NGOCampaign {i+1}",
                    goal_amount=round(random.uniform(1000, 50000), 2),
                    raised_amount=round(random.uniform(1000, 50000), 2),
                    donors_count=random.randint(1, 100),
                    status=random.choice(["active", "completed", "paused"]),
                    start_date=date.today() - timedelta(days=random.randint(0, 90)),
                    end_date=date.today() - timedelta(days=random.randint(0, 90)),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 NGOCampaign records created'))

        if Volunteer.objects.count() == 0:
            for i in range(10):
                Volunteer.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    skills=f"Sample {i+1}",
                    hours_contributed=random.randint(1, 100),
                    status=random.choice(["active", "inactive", "pending"]),
                    availability=random.choice(["weekdays", "weekends", "flexible"]),
                    joined_date=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 Volunteer records created'))
