from django.shortcuts import render,redirect
from .forms import NameForm, EmailForm, MessageForm
from .models import ContactInfo


# Create your views here.
def index(request):
    return render(request, "blog/index.html")


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    if request.method == "POST":
        name_form = NameForm(request.POST)
        email_form = EmailForm(request.POST)
        message_form = MessageForm(request.POST)
        if name_form.is_valid() and email_form.is_valid() and message_form.is_valid():
            objs = ContactInfo(name=name_form.cleaned_data, email=email_form.cleaned_data,
                               message=message_form.cleaned_data)
            objs.save()
            return redirect('/contact/')

    else:
        name_form = NameForm()
        email_form = EmailForm()
        message_form = MessageForm()

    return render(request, "blog/contact.html",
                  {'name_form': name_form, "email_form": email_form, "message_form": message_form})
