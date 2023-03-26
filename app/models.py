import os
import uuid
from django.db import models
from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

def link_maker(href: str, name: str):
    return format_html(
            f"<a href='{href}' "
            f"target='_blank' rel='noopener noreferrer'>{name}</a>")


class Claim(models.Model):

    class Type(models.TextChoices):
        ECOMMERCE = '1', _('Электронная коммерция')
        CUSTOMER = '2', _('Обслуживание клиентов')
        INTRANET = '3', _('Интранет-портал')
        OTHER = '4', _('Другой')


    class IsAdaptive(models.TextChoices):
        NO = '1', _('Только десктопная версия')
        YES = '2', _('Сайт с мобильной и планшетной версиями')


    class State(models.TextChoices):
        NEW = '1', _('Новый проект')
        EXISTED = '2', _('Существующий проект')


    class StartDate(models.TextChoices):
        NOW = '1', _('Как можно скорее')
        TWO_WEEKS = '2', _('В течение пару недель')
        TWO_MONTHS = '3', _('В течение пару месяцев')


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    type = models.CharField(choices=Type.choices, default=Type.OTHER, max_length=3, null=True, blank=True)
    is_adaptive = models.CharField(choices=IsAdaptive.choices, default=IsAdaptive.NO, max_length=3, null=True, blank=True)
    state = models.CharField(choices=State.choices, default=State.NEW, max_length=3, null=True, blank=True)
    start_date = models.CharField(choices=StartDate.choices, default=StartDate.NOW, max_length=3, null=True, blank=True)
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
