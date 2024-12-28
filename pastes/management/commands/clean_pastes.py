from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from pastes.models import Paste


class Command(BaseCommand):
    help = "Delete expired pastes older than 1 month."

    def handle(self, *args, **options):
        cutoff = timezone.now() - timedelta(days=30)
        Paste.objects.filter(created_at__lt=cutoff).delete()
        self.stdout.write("Deleted expired pastes.")
