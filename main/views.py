from django.shortcuts import render


def show_main(request):
    context = {
        "npm": "2406421320",
        "name": "Nathanael Leander Herdanatra",
        "class": "PBP A",
    }

    return render(request, "main.html", context)
