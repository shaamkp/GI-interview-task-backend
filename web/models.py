from django.db import models

from general.models import BaseModel


class Notes(BaseModel):
    title = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        db_table = 'general_note'
        verbose_name = 'General Note'
        verbose_name_plural = 'General Notes'
        ordering = ['-created_at']

    def __str__(self):
        return self.title