from django.db import models

# Create your models here.
class Cell_Report(models.Model):
    report = models.FileField(
        upload_to='document/uploaded_file/',
    )
    created_dt = models.DateTimeField(
        auto_now_add=True,
        )
    created_by = models.CharField(
        max_length=225,
        )
    updated_dt = models.DateTimeField(
        auto_now=True,
        )
    updated_by = models.CharField(
        max_length=225,
        )

