from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    # Scelte per la priorità
    PRIORITY_CHOICES = [
        ("low", "Bassa"),
        ("medium", "Media"),
        ("high", "Alta"),
    ]

    # Campi del modello
    title = models.CharField(max_length=200, verbose_name="Titolo")
    description = models.TextField(blank=True, verbose_name="Descrizione")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creato il")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modificato il")
    due_date = models.DateTimeField(null=True, blank=True, verbose_name="Scadenza")
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="medium",
        verbose_name="Priorità",
    )
    completed = models.BooleanField(default=False, verbose_name="Completato")
    category = models.CharField(max_length=100, blank=True, verbose_name="Categoria")
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks",
        verbose_name="Assegnato a",
    )

    class Meta:
        ordering = ["-created_at"]  # Ordina per data di creazione decrescente
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title

    def is_overdue(self):
        """Controlla se il task è scaduto"""
        if self.due_date and not self.completed:
            return timezone.now() > self.due_date
        return False
