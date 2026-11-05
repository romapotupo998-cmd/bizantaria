from django.db import models


class Application(models.Model):
    STATUS_CHOICES = [
        ("new", "Нова"),
        ("review", "На розгляді"),
        ("approved", "Схвалена"),
        ("rejected", "Відхилена"),
    ]

    country = models.CharField(max_length=100)
    representative = models.CharField(max_length=150)
    position = models.CharField(max_length=100)
    relations = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country