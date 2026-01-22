from django.shortcuts import render
from .forms import NameForm

def greet_user(request):
    name = None
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
    else:
        form = NameForm()

    return render(request, "greet.html", {"form": form, "name": name})
