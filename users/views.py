from django.shortcuts import render

# Create your views here.
from users.forms import NameForm


def dashboard(request):
    return render(request, "base.html")


def example_view(request):

    if request.method == "POST":
        form = NameForm(data=request.POST)

        print(form.data)

    form = NameForm()
    context = {"form": form}

    return render(request, "users/example.html", context)
