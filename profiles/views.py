from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render, get_object_or_404, redirect, reverse, HttpResponseRedirect
)

from .models import UserProfile
from blog.models import Post
from .forms import UserProfileForm


@login_required
def profile(request):
    """
    Display the user's profile.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
         'form': form,
    }

    return render(request, template, context)


@login_required
def wishlist(request):
    """
    Display the user's / favourites.
    This view renders the user's wishlist / favourites page.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    posts = Post.objects.filter(users_wishlist=request.user)

    template = 'profiles/wishlist.html'
    context = {
        'wishlist': posts,
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, slug, *args, **kwargs):
    """
    This view handles adding to, and removing a blog from,
    the user's wishlist / favourites.
    Renders the user's wishlist / favourites page.
    """
    queryset = Post.objects.filter(status=1)
    post_wish = get_object_or_404(queryset, slug=slug)
    user = request.user
    user_profile = user.userprofile

    liked = False

    if post_wish.users_wishlist.filter(id=request.user.id).exists():
        post_wish.users_wishlist.remove(request.user)
        messages.success(
            request,
            f'Successfully removed {post_wish} from Favourites List!'
        )
        liked = False
    else:
        post_wish.users_wishlist.add(request.user)
        messages.success(
            request, f'Successfully added {post_wish} to Favourites List!'
        )
        liked = True

    return HttpResponseRedirect(request.META["HTTP_REFERER"])
