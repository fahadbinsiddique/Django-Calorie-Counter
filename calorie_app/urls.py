from django.urls import path
from  calorie_app.views import *

urlpatterns = [
    path("", register_page, name="register_page"),
    path("login/", login_page, name="login_page"),
    path("logout/", logout_page, name="logout_page"),
    path("dashboard/", dashboard, name="dashboard"),
    path("profile/", profile, name="profile"),
    path("profile-update/", profile_update, name="profile_update"),
    path("Calorie-Consume/", CalorieConsume, name="CalorieConsume"),
]
