import os
import uuid
from django.db import models
from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html

def link_maker(href: str, name: str):
    return format_html(
            f"<a href='{href}' "
            f"target='_blank' rel='noopener noreferrer'>{name}</a>")


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

    @admin.display(description='Файлы')
    def files(self):
        this_user_dir = os.path.join(settings.STATIC_PATH, 'claim', str(self.id))
        if not os.path.exists(this_user_dir):
            return None
        
        files = os.listdir(this_user_dir)
        if not files:
            return None
        
        file_hrefs = []
        for file in files:
            file_hrefs.append(
                    link_maker(
                        os.path.join(
                            settings.CLAIM_FILES_BASE_URL, str(self.id), file), file))

        return format_html(', '.join(file_hrefs))

    def __str__(self):
        return f"Заявка {f'от {self.email}' if self.email else f'от {self.phone}' if self.phone else f'#{self.id}'}"

    class Meta:
        db_table = "claims"
        verbose_name = 'заявку'
        verbose_name_plural = 'заявки'
