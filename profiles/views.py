from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render, get_object_or_404, redirect, reverse, HttpResponseRedirect
)

from .models import UserProfile


@login_required
def profile(request):
    """
    Display the user's profile.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)