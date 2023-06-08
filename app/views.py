from django.contrib import messages
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from .forms import ObjectiveForm
from .models import Objective, ObjectiveValue


def objectives(request):
    objs = Objective.objects.filter(completed=False)
    value = ObjectiveValue.objects.all()

    context = {
        "title": "Задачи",
        "objs": objs,
        "red": value[2],
        "orange": value[1],
        "green": value[0],
    }
    return render(request=request, template_name="app/index.html", context=context)


def completed(request):
    objs = Objective.objects.filter(completed=True)
    value = ObjectiveValue.objects.all()

    context = {
        "title": "Задачи",
        "objs": objs,
        "red": value[2],
        "orange": value[1],
        "green": value[0],
    }
    return render(request=request, template_name="app/completed.html", context=context)


def create_obj(request):
    if request.method == "POST":
        form = ObjectiveForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Задача создана!")
            return HttpResponseRedirect(reverse("create_obj"))
        else:
            massage = "Форма заполнена не верно!"
            context = {
                "title": "Создание задачи",
                "massage": massage,
                "form": form,
            }
            return render(request=request, template_name="app/create_obj.html", context=context)
    else:
        form = ObjectiveForm()

    context = {
        "title": "Создание задачи",
        "form": form,
    }
    return render(request=request, template_name="app/create_obj.html", context=context)


def obj_completed(request, obj_id):
    Objective.objects.filter(id=obj_id).update(completed=True)
    messages.success(request, "Задча помечена как выполненная!")
    return HttpResponseRedirect(reverse("objectives"))
