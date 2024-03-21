from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def contact_jetset_journal(request):
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS, "Contact request received! We'll try to respond within 2 working days.")

    contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {
            "contact_form": contact_form
        },
    )