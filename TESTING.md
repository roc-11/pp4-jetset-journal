# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-jetset-journal-4cbea9e2528c.herokuapp.com%2F) | ![screenshot](documentation/testing/html-validator-home-new.png) | no errors |
| Contact | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-jetset-journal-4cbea9e2528c.herokuapp.com%2Fcontact%2F) | ![screenshot](documentation/testing/html-validator-contact-new.png) | no errors |
| About | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-jetset-journal-4cbea9e2528c.herokuapp.com%2Fabout%2F) | ![screenshot](documentation/testing/html-validator-about-new.png) | Bad value 75% for attribute width on element img. Displays as expected. |
| Profile | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-jetset-journal-4cbea9e2528c.herokuapp.com%2Fprofile%2F) | ![screenshot](documentation/testing/html-validator-profile-new.png) | no errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | n/a | ![screenshot](documentation/testing/css-validator-style-css.png) | Pass: No Errors |
| admin.css | n/a | ![screenshot](documentation/testing/css-validator-admin-css.png) | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| comments.js | ![screenshot](documentation/testing/js-validation-script.png) | 1 undefined variable (bootstrap) from external files |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | Screenshot | Notes |
| --- | --- | --- |
| manage.py | ![screenshot](documentation/testing/manage_py.png) | Pass: No Errors |
| settings.py | ![screenshot](documentation/testing/settings_py_new.png) | Pass: No Errors |
| About admin.py | ![screenshot](documentation/testing/about_admin_py.png) |  Pass: No Errors |
| About models.py | ![screenshot](documentation/testing/about_models_py.png) | Pass: No Errors |
| About views.py | ![screenshot](documentation/testing/about_views_py.png) | Pass: No Errors |
| Blog admin.py | ![screenshot](documentation/testing/blog_admin_py.png) | Pass: No Errors |
| Blog models.py | ![screenshot](documentation/testing/blog_models_py.png) | Pass: No Errors |
| Blog urls.py | ![screenshot](documentation/testing/blog_urls_py.png) | Pass: No Errors |
| Blog views.py | ![screenshot](documentation/testing/blog_views_py.png) | Pass: No Errors |
| Contact admin.py | ![screenshot](documentation/testing/contact_admin_py.png) | Pass: No Errors |
| Contact forms.py | ![screenshot](documentation/testing/contact_forms_py.png) | Pass: No Errors |
| Contact models.py | ![screenshot](documentation/testing/contact_models_py.png) | Pass: No Errors |
| Contact urls.py | ![screenshot](documentation/testing/contact_urls_py.png) | Pass: No Errors|
| Contact views.py | ![screenshot](documentation/testing/contact_views_py.png) | E501 line too long (115 > 79 characters). noqa |
| Profiles admin.py | ![screenshot](documentation/testing/profiles_admin_py.png) | Pass: No Errors |
| Profiles forms.py | ![screenshot](documentation/testing/profiles_forms_py.png) | Pass: No Errors |
| Profiles models.py | ![screenshot](documentation/testing/profiles_models_py.png) | Pass: No Errors |
| Profiles urls.py | ![screenshot](documentation/testing/profiles_urls_py.png) | Pass: No Errors|
| Profiles views.py | ![screenshot](documentation/testing/profiles_views_py.png) | E501 line too long (115 > 79 characters). noqa |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

The production site was tested using [Browserstack](https://www.browserstack.com/) to ensure compatibility across various devices, and browsers including Mac, iPhone, Windows and Android, Chrome, Safari and Firefox on different pages chosen at random.

| Browser | Home | About | Contact | Blog Details | Favourites | My Profile | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/chrome-home-new.png) | ![screenshot](documentation/browsers/chrome-about-new.png) | ![screenshot](documentation/browsers/chrome-contact-new.png) | ![screenshot](documentation/browsers/chrome-blogdetail-new.png) | ![screenshot](documentation/browsers/chrome-favourites-new.png) | ![screenshot](documentation/browsers/chrome-profile-new.png) | Works as expected |
| Microsoft Edge | ![screenshot](documentation/browsers/microsoft-edge-home-new.png) | ![screenshot](documentation/browsers/microsoft-edge-about-new.png) | ![screenshot](documentation/browsers/microsoft-edge-contact-new.png) | ![screenshot](documentation/browsers/microsoft-edge-blogdetail-new.png) | ![screenshot](documentation/browsers/microsoft-edge-favourites-new.png) | ![screenshot](documentation/browsers/microsoft-edge-profile-new.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/safari-home-new.png) | ![screenshot](documentation/browsers/safari-about-new.png) | ![screenshot](documentation/browsers/safari-contact-new.png) | ![screenshot](documentation/browsers/safari-blogdetail-new.png) | ![screenshot](documentation/browsers/safari-favourites-new.png) | ![screenshot](documentation/browsers/safari-profile-new.png) | Works as expected |

The first iteration of the Jetset Journal project:

![screenshot](documentation/testing/broswer-chrome.png)

![screenshot](documentation/testing/browser-andriod-chrome.png)

![screenshot](documentation/testing/browser-iphone15-safari.png)

![screenshot](documentation/testing/browser-microsoft-edge.png)

![screenshot](documentation/testing/browser-safari.png)

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home New | Home Old | About | Contact | Blog Details | Favourites | Profile | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsive-mobile-home-new.png) | ![screenshot](documentation/responsive-mobile-home.png) | ![screenshot](documentation/responsive-mobile-about.png) | ![screenshot](documentation/responsive-mobile-contact.png) | ![screenshot](documentation/responsive-mobile-blog-detail.png) |  ![screenshot](documentation/responsiveness-favourites-mobile.png) | ![screenshot](documentation/responsive-mobile-profile.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsive-tablet-home-new.png) | ![screenshot](documentation/responsive-tablet-home.png) | ![screenshot](documentation/responsive-tablet-about.png) | ![screenshot](documentation/responsive-tablet-contact.png) | ![screenshot](documentation/responsive-tablet-blog-detail.png) | ![screenshot](documentation/responsiveness-favourites-tablet.png) | ![screenshot](documentation/responsiveness-profile-tablet.png) | Works as expected |
| Desktop (DevTools) | ![screenshot](documentation/responsive-desktop-home-new.png) | ![screenshot](documentation/responsive-desktop-home.png) | ![screenshot](documentation/responsive-desktop-about.png) | ![screenshot](documentation/responsive-desktop-contact.png) | ![screenshot](documentation/responsive-desktop-blog-detail.png) | ![screenshot](documentation/responsiveness-favourites-desktop.png) | ![screenshot](documentation/responsiveness-profile-desktop.png) | Works as expected |
| XL Monitor | ![screenshot](documentation/responsive-xl-home-new.png) | ![screenshot](documentation/responsive-xl-home.png) | ![screenshot](documentation/responsive-xl-about.png) | ![screenshot](documentation/responsive-xl-contact.png) | ![screenshot](documentation/responsive-xl-blog-detail.png) |![screenshot](documentation/responsiveness-favourites-desktop-xl.png) | ![screenshot](documentation/responsiveness-profile-desktop-xl.png) | Scaling starts to have minor issues |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Desktop | Notes |
| --- | --- | --- |
| Home | ![screenshot](documentation/testing/lighthouse-desktop-home.png) | No issues - minor SEO issues |
| Home Mobile | ![screenshot](documentation/testing/lighthouse-mobile-home.png) | Medium/slow response time due to large images |
| About | ![screenshot](documentation/testing/lighthouse-desktop-about.png) | No issues |
| Contact | ![screenshot](documentation/testing/lighthouse-desktop-contact.png) | No issues |
| Blog Details | ![screenshot](documentation/testing/lighthouse-desktop-blogdetail.png) | Some minor warnings |
| Favourites | ![screenshot](documentation/testing/lighthouse-desktop-favourites.png) | No issues |
| Profile | ![screenshot](documentation/testing/lighthouse-desktop-profile.png) | No issues |

First iteration of project: 

| Page | Desktop | Notes |
| --- | --- | --- |
| Home | ![screenshot](documentation/testing/lighthouse-home.png) | Slow response time due to large images |
| About | ![screenshot](documentation/testing/lighthouse-about.png) | Some minor warnings |
| Contact | ![screenshot](documentation/testing/lighthouse-contact.png) | Some minor warnings |
| Blog Details | ![screenshot](documentation/testing/lighthouse-blog-details.png) | Medium response time due to large image |

## Defensive Programming

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| | Click on About link in navbar | Redirection to About page | Pass | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Click on Login/Register link in navbar | Redirection to Login page | Pass | |
| | Click on Logout link in navbar | Redirection to Logout page | Pass | |
| | Click on Profile link in navbar | Redirection to Profile page - if logged in user | Pass | |
| | Click on Favourite Posts link in navbar | Redirection to Favourites page - if logged in user | Pass | |
| | Click on Blog Post link (title/exceprt in card) | Redirection to blog detail page for that post | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter name | Field will accept text / numbers | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to Contact page (blank form) and displays succes message | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click sign up button, with all valid information in form | Redirect to email confirmation page, confirmation email sent to user's email. | Pass | |
| | Click email validation link | Redirect to email confirmation page - click confirm and redirected to login page. | Pass | |
| | Click on Sign Up button | Redirects user to Home page, with user logged in, and displays succes message | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Blog Admin - Delete Post | | | | |
| | Click Delete Post button to delete post | Are you sure you want to delete? Confirm - delete post. | Pass | |
| Post Detail - Delete Commment | | | | |
| | Click Delete comment button to delete comment | Are you sure you want to delete? Confirm modal - delete post. | Pass | |

![screenshot](documentation/testing/blog-admin-delete-post-defensive.png)

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to view an intuitive website with straightforward navigation that is fully responsive. | ![screenshot](documentation/features/navigation_logged_out.png) |
| As a new site user, I would like to create an account so that I can comment on and like blog posts. | ![screenshot](documentation/features/signup.png) |
| As a new site user, I would like to easily edit and delete any comments that I make. | ![screenshot](documentation/features/edit-comment.png) |
| As a new site user, I would like to easily contact the website administrators with questions. | ![screenshot](documentation/features/contact-page.png) |
| As a new site user, I would like to easily understand the main purpose of the site. | ![screenshot](documentation/features/about_page.png) |
| As a new user, I want attractive and relevant visuals and colour schemes that work with the content. | n/a |
| As a new site user, I would like to add blog posts to my wishlist/favourites so that I can return to them at a later date/time. | ![screenshot](documentation/features/favourites_page.png) |
| As a returning site user, I would like to view an intuitive website with straightforward navigation that is fully responsive. | ![screenshot](documentation/features/navigation_logged_in.png) |
| As a returning site user, I would like to easily log into my account so that I can comment on and like blog posts. | ![screenshot](documentation/features/login.png) |
| As a returning site user, I would like to easily edit and delete any comments that I make. | ![screenshot](documentation/features/edit-comment.png) |
| As a returning site user, I would like to add blog posts to my wishlist/favourites so that I can return to them at a later date/time. | ![screenshot](documentation/features/favourites_page.png) |
| As a site administrator, I would like to have a recognizable branded admininstator area to manage users, blog posts, blogs comments and blog likes. | ![screenshot](documentation/features/admin-area.png) |
| As a site administrator, I would like to easily create blog postings in draft or published form, for display on Jetset Journal. | ![screenshot](documentation/features/admin-create-post.png) |
| As a site administrator, I would like to easily edit the about text and profile picture using a user-friendly UI. | ![screenshot](documentation/features/about_table_ui.png) |
| As a site administrator, I would like to have control over approving user comments before they appear on the front-end. | ![screenshot](documentation/features/edit-comment-not-approved.png) |
| As a site administrator, I would like to manage user contact requests and mark them as read. | ![screenshot](documentation/features/contact-table.png) |
| As a site administrator, I would like to have a simple UI that will encourage users to return and engage with the blog. | n/a |
| As a site administrator, I would like to easily add a new blog post to the website/blog from the front-end/website. | ![screenshot](documentation/features/add_blog_post_form_1.png) |
| As a site administrator, I would like to easily edit or delete a blog post from the  website/blog from the front-end/website. | ![screenshot](documentation/features/edit_blog_post_form_1.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

I tried used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

#### Unit Test Issues

My tests do not work correctly. I ran into an issue. The bug lies somewhere in my blog/models.py file. It is a field error somewhere in a model. 

I looked at each field on all the models, and check that each one is syntactically correct, and does not contain any thing which would allow the model to insert an empty field. However I could not identify exactly where the issue arose. Looking online is seems that it likely is an issue with your models, somewhere, it could be something as simple as not specifying a max-length on a CharField, or one of the fields being null. 

`python3 manage.py test blog`

Results in the following error: 

```
Found 4 test(s).
Creating test database for alias 'default'...
Traceback (most recent call last):
File "/workspace/.pip-modules/lib/python3.9/site-packages/django/db/backends/utils.py", line 87, in _execute
return self.cursor.execute(sql)
File "/workspace/.pip-modules/lib/python3.9/site-packages/django/db/backends/sqlite3/base.py", line 324, in execute
return super().execute(query)
sqlite3.OperationalError: near "None": syntax error
```
## Fixed Bugs

- Homepage Hero Image - I had a cool CSS styling imported, which made the hero image increase in size on user hover over, and also gave it a subdued background colour. However, this was causing huge load and performance issues with the site. The CSS imported was slowing down the site homepage and making the hero image loading process have a massive impact on performance and best practice scores (Lighthouse). So a new Hero image was generated using the website [leonardo.ai](https://leonardo.ai/) and new CSS styling was implemented.

Old Homepage            |  New Homepage
:-------------------------:|:-------------------------:
![Screenshot of the footer desktop](documentation/features/hero-section-home.png)  |  ![Screenshot of the footer mobile](documentation/features/hero-section-home-new.png)

- On the first project iteration, I tried to implement a UserProfile and Profile page but failed to do so correctly. I ammended this on my project repeat. I removed blog_userprofile model, as it was incorrect and not working. I accidentally dropped the table blog_userprofile from Elephany SQL before running my migrations so caused big issues. I recreated the table blog_userprofile manually using SQL, and then could successfully run migrations to remove the model and all code referencing userprofile from the Blog app.
I then created a new app - Profiles - and made a UserProfile model, template, urls and views to show the user's profile. I added a receiver to automatically create a user profile when a user is added to the DB. It all works as intented.

![Screenshot of the user profile](documentation/features/my_profile_page.png)

- I added a wishlist/favourite post functionality which I also could not do correctly on the first project iteration. 

![Screenshot of the favourites page](documentation/features/favourites_page.png)

- I implemented real email functionality in order for users to signup to the blog as a user. They must now validate their email before they have access to the site. This is explained in the README.md file in the features>signup section.

- I successfully added front-end UI/functionality for blog admins to add, edit and delete (CRUD) posts from the front end, without having to log into the Django admin.

- I ran into issues with the user profile image on the profile page. First I installed pillow. I had to edit the image field on the model to fix this. I also had to add a folder to Cloudinary called media/image, and edit the settings.py file to ensure that the user uploaded images when to the correct place. 

settings.py:
```python
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

models.py
```python
class UserProfile(models.Model):
    
    profile_picture = models.ImageField(
        default='placeholder.jpg',
        upload_to='image/')
```

![Screenshot - errors ](documentation/testing/error-no-file.png)

![Screenshot - errors ](documentation/testing/error-pillow-install.png)

![Screenshot - errors ](documentation/testing/error-profile-image-load.png)

![Screenshot - Profile Fixed ](documentation/testing/my-profile-fixed.png)

- SECRET KEY NB - I had exposed my secret key in the first project iteration, due to the tight time constraints I was under. This was a silly mistake and I have generated a new key, correctly added it to the env.py file (.gitignore) and also to my Heroku config vars.

## Unfixed Bugs

- Users are able to enter numbers as a username on registration. It results in an error but the user is still added to the User Table. I will need to fix this in future iterations of the Jetset Journal Project.

There are no remaining bugs that I am aware of.
