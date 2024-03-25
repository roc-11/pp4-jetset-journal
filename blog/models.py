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
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """
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
    destination = models.CharField(
        choices=DESTINATIONS, default='europe', max_length=50)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
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
    """
    Stores a single like entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE)
    value = models.CharField(
        choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)


class UserProfile(models.Model):

    """
    This class creates a user profile page.
    It uses the UserProfile model to allow users to
    fill in their profile information, and associates the profile with the
    currently logged-in user.
    """

    user = models.OneToOneField(
        User, null=True,  on_delete=models.CASCADE, related_name='user_profile')  # noqa
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
