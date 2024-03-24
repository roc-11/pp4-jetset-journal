from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

STATUS = ((0, "Draft"), (1, "Published"))
DESTINATIONS = (
    ('europe', 'Europe'),
    ('northamerica', 'North America'),
    ('southamerica', 'South America'),
    ('centralamerica', 'Central America'),
    ('asia', 'Asia'),
    ('africa', 'Africa'),
    ('antarctica', 'Antarctica'),
    ('australia', 'Australia'),
    ('newzealand', 'New Zealand & The Pacific'),
    ('caribbean', 'The Caribbean'),
    ('middleeast', 'The Middle East')
    )
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    destination = models.CharField(choices=DESTINATIONS, default='europe')
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"
    
    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)


class UserProfile(models.Model):
    
    user = models.OneToOneField(
        User, null=True,  on_delete=models.CASCADE, related_name='user_profile')
    bio = models.TextField(blank=True)
    profile_picture = CloudinaryField('image', default='placeholder')
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True)

    def __str__(self) -> str:
        """ Returns a string representation of the associated user. """
        return str(self.user)

    def get_absolute_url(self):
        """ Returns the absolute URL for the user's profile page. """
        return reverse('show_user_profile_page', args=[str(self.pk)])

    def is_complete(self):
        """
        Checks if the user's profile is considered complete.
        """
        required_fields = [
            'bio',
        ]

        for field_name in required_fields:
            if not getattr(self, field_name):
                return False

        return True

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()