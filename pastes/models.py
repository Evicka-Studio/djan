import uuid
from datetime import timedelta
from django.db import models, transaction
from django.utils import timezone
from django.core.exceptions import ValidationError

MAX_PASTES = 1000  # Define your paste limit

class Paste(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if Paste.objects.count() >= MAX_PASTES and not self.pk:
            raise ValidationError("Maximum number of pastes reached.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def is_expired(self):
        one_month_ago = timezone.now() - timedelta(days=30)
        return self.created_at < one_month_ago

    def __str__(self):
        return f"Paste {self.id}"
