from django.shortcuts import render, redirect
from calorie_app.models import *
from calorie_app.forms import *
from django.contrib.auth import login, logout
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


# Create your views here.
def register_page(request):
    if request.method == "POST":
        form_data = RegisterForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect("login_page")
    form_data = RegisterForm()
    context = {
        "form_data": form_data,
        "heading": "Register",
        "title": "Register",
        "btn": "Register",
    }

    return render(request, "master/base_form.html", context)


def login_page(request):
    if request.method == "POST":
        form_data = LoginForm(request, request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            login(request, user)
            return redirect("dashboard")
    form_data = LoginForm()
    context = {
        "form_data": form_data,
        "heading": "Login",
        "title": "Login",
        "btn": "Login",
    }
    return render(request, "master/base_form.html", context)

@login_required
def logout_page(request):
    logout(request)
    return redirect("login_page")


@login_required
def dashboard(request):
    bmr = ProfileModel.objects.get(user=request.user or 1)
    bmrdata = bmr.bmr or 0
    date = timezone.now()
    calory_data = (
        CalorieConsumeModel.objects.filter(
            user=request.user, created_add=date
        ).aggregate(total=Sum("calorie_consume"))["total"]
        or 0
    )

    need_calory = bmrdata - calory_data

    context = {
        "form_data": round(calory_data, 2),
        "heading": "dashboard",
        "title": "dashboard",
        "need_calory": round(need_calory, 2),
    }
    return render(request, "dashboard.html", context)


@login_required
def profile(request):
    return render(
        request,
        "profile.html",
    )


def profile_update(request):
    try:
        user = request.user.user_profile
    except ProfileModel.DoesNotExist:
        user = None
    if request.method == "POST":
        form_data = ProfileForm(request.POST, instance=user)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user
            gender = data.gender
            weight = data.weight or 0
            height = data.height or 0
            age = data.age or 0
            # BMR= 66.47+(13.75 x weight in kg) + (5.003 x height in cm) - (6.755 x age in years)
            if gender == "Male":
                bmr_calcalute = (
                    66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
                )
            else:
                # BMR=655.1+(9.563 x weight in kg)+(1.850 xheight in cm) - (4.676 x age in years)
                bmr_calcalute = (
                    655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
                )

            data.bmr = bmr_calcalute
            data.save()

            return redirect("profile")

    form_data = ProfileForm(instance=user)
    context = {
        "form_data": form_data,
        "heading": "profile_update",
        "title": "profile_update",
        "btn": "profile_update",
    }
    return render(request, "master/base_form.html", context)


@login_required
def CalorieConsume(request):
    try:
        user = request.user.user_profile
    except:
        user = None

    if request.method == "POST":

        form_data = CalorieConsumeForm(request.POST)
        if form_data.is_valid():
            data = form_data.save()
            data.user = request.user
            data.save()
            return redirect("dashboard")
    form_data = CalorieConsumeForm()
    context = {
        "form_data": form_data,
        "heading": "CalorieConsume",
        "title": "CalorieConsume",
        "btn": "Save",
    }
    return render(request, "master/base_form.html", context)
