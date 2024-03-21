from django.shortcuts import render
from .forms import Contact, ContactForm

# Create your views here.
def contact_jetset_journal(request):
    contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {
            "contact_form": contact_form
        },
    )