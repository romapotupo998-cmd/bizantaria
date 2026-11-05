from django.contrib import admin
from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "country",
        "representative",
        "relations",
        "email",
        "status",
        "created_at"
    )

    search_fields = (
        "country",
        "representative",
        "email"
    )

    list_filter = (
        "relations",
        "status",
        "created_at"
    )

    ordering = ("-created_at",)

    fields = (
        "country",
        "representative",
        "position",
        "relations",
        "email",
        "message",
        "status",
        "created_at"
    )

    readonly_fields = ("created_at",)