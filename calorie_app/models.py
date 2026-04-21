from django.db import models
from django.contrib.auth.models import User


class ProfileModel(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name="user_profile"
    )
    name = models.CharField(max_length=120, null=True)
    age = models.PositiveIntegerField(null=True)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    bmr = models.FloatField(null=True)
    GENDER_TYPES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    gender = models.CharField(choices=GENDER_TYPES, null=True, max_length=20)

    def __str__(self):
        return f"{self.name}"


class CalorieConsumeModel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="user_calorie"
    )
    item_name = models.CharField(max_length=120, null=True)
    calorie_consume = models.FloatField(max_length=120, null=True)
    created_add = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.item_name
