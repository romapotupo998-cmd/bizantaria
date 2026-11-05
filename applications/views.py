from django.shortcuts import render
from .models import Application

def sender(request):
    if request.method == "POST":
        Application.objects.create(
            country=request.POST.get("country"),
            representative=request.POST.get("representative"),
            position=request.POST.get("position"),
            relations=request.POST.get("relations"),
            email=request.POST.get("email"),
            message=request.POST.get("message")
        )

        print("Нову дипломатичну заявку збережено!")

        return render(request, "sender.html", {
            "success": True
        })

    return render(request, "sender.html")