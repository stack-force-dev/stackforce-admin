import uuid
from django.db import models


class Claim(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)
    is_adaptive = models.BooleanField(default=False, null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    start_date = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Заявка {f'от {self.email}' if self.email else f'от {self.phone}' if self.phone else f'#{self.id}'}"

    class Meta:
        db_table = "claims"
        verbose_name = 'заявку'
        verbose_name_plural = 'заявки'
