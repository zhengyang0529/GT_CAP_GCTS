from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female")
]

class Cell_Report(models.Model):
    description = models.CharField(
        verbose_name=_("Description"),
        max_length=255, 
        blank=False,
    )
    report = models.FileField(
        verbose_name=_("Report"),
        upload_to='document/uploaded_file/',
    )
    created_dt = models.DateTimeField(
        verbose_name=_("Created Date"),
        auto_now_add=True,
    )
    created_by = models.CharField(
        verbose_name=_("Created By"),
        max_length=225,
    )
    updated_dt = models.DateTimeField(
        verbose_name=_("Updated Date"),
        auto_now=True,
    )
    updated_by = models.CharField(
        verbose_name=_("Updated By"),
        max_length=225,
    )

class Member(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=100,
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        max_length=10,
        choices=GENDER_CHOICES,
    )
    date_of_birth = models.DateField(
        verbose_name=_("Date of Birth"),
    )
    cell_group = models.CharField(
        verbose_name=_("Cell Group"),
        max_length=100,
    )
    status = models.CharField(
        verbose_name=_("Status"),
        max_length=100,
    )
    baptism = models.BooleanField(
        verbose_name=_("Baptism"),
        default=False,
    )
    created_dt = models.DateField(
        verbose_name=_("Created Date"),
        auto_now_add=True,
    )
    created_by = models.CharField(
        verbose_name=_("Created By"),
        max_length=225,
    )
    updated_dt = models.DateField(
        verbose_name=_("Updated Date"),
        auto_now=True,
    )
    updated_by = models.CharField(
        verbose_name=_("Updated By"),
        max_length=225,
    )
