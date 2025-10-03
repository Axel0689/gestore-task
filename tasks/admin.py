from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Campi da mostrare nella lista
    list_display = [
        "title",
        "priority",
        "due_date",
        "completed",
        "assigned_to",
        "created_at",
    ]

    # Campi per cui permettere la ricerca
    search_fields = ["title", "description", "category"]

    # Filtri laterali
    list_filter = ["priority", "completed", "category", "created_at", "assigned_to"]

    # Campi modificabili direttamente dalla lista
    list_editable = ["completed", "priority"]

    # Organizzazione dei campi nel form di modifica
    fieldsets = (
        ("Informazioni Base", {"fields": ("title", "description", "category")}),
        ("Dettagli", {"fields": ("priority", "due_date", "assigned_to")}),
        ("Stato", {"fields": ("completed",)}),
    )

    # Campi di sola lettura
    readonly_fields = ["created_at", "updated_at"]
