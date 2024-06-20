"""
~ МОДЕЛ ПОДАТАКА / `Models` as Python classes in Django
"""

from django.db import models
from django.db.models import (
    UniqueConstraint,
)  # ограничи поља на јединствене вриједности/без дуплих уноса
from django.db.models.functions import Lower  # за мала слова вриједности поља


# Create your models here.
class Location(models.Model):
    """
    Модел који представља туристичко мјесто/дестинацију/локацију.
    """

    name = models.CharField(
        max_length=30,  # `Grad Istocno Sarajevo` -> 21 слово! ;-)
        unique=True,  # име туристичке дестинације је јединствено (case-sensitive!)
        help_text='Туристичке \
<a href="https://turizamrs.org/destinacije/" target="_blank">дестинације</a> Републике Српске',
    )
    po_box = models.CharField(
        max_length=5,
        verbose_name='PO Box',
        null=True,  # ово чак и не треба, јер постоји подразумјевана вриједност `00000` !!!
        default='00000'
    )

    def __str__(self):
        """Стринг који представља на читљив људима начин објекат модела."""
        return self.name

    class Meta:
        """Meta класа за додатне информације o моделу"""

        constraints = [
            UniqueConstraint(
                Lower("name"),
                name="location_name_case_insensitive_unique",
                violation_error_message="Локација већ постоји (велика/мала слова нису битна!)",
            ),
        ]


class Preference(models.Model):
    """
    Модел који представља жеље/свиђања/преференце корисника, тј. будућег туристе.
    """

    # приликом брисања корисника - обриши и његове преференце
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="preferences"
    )
    # да би поље било НЕОБАВЕЗНО ТРЕБА додати `blank=True` !!!
    food = models.CharField(max_length=30, null=True, blank=True)
    drink = models.CharField(max_length=30, null=True, blank=True)
    entertainment = models.CharField(max_length=30, null=True, blank=True)
    recreation = models.CharField(max_length=30, null=True, blank=True)
    sport = models.CharField(max_length=30, null=True, blank=True)
    hobby = models.CharField(max_length=50, null=True, blank=True)
    comment = models.TextField(max_length=1000, default="Још увијек нема коментара")

    def __str__(self):
        return f"{self.user.name}'s preferences"


class User(models.Model):
    """
    Модел који представља корисника, тј. будућег или бившег туристу.
    """

    name = models.CharField(
        max_length=50, help_text="Ваше име или надимак, по жељи! :-)"
    )
    email = models.EmailField(null=True, blank=True)
    region = models.CharField(max_length=50)
    state = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.name} from {self.region}"
