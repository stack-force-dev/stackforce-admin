from django.contrib import admin
from .models import Claim

admin.site.index_title = 'StackForce'


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = ("id", "email", "phone", "created_at", "files")
    search_fields = ("id", "email", "phone", "created_at")
    ordering = ("created_at",)
    search_fields = ('email', 'phone')
