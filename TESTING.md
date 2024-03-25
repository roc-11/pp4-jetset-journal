# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-jetset-journal-4cbea9e2528c.herokuapp.com%2F) | ![screenshot](documentation/testing/html-validator-home.png) | Element p not allowed as child of element span in this context, but displays fine. A document must not include more than one visible main element. |
| Contact | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-jetset-journal-4cbea9e2528c.herokuapp.com%2Fcontact%2F) | ![screenshot](documentation/testing/html-validator-contact.png) | Element p not allowed as child of element span in this context, but displays fine.|
| About | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-jetset-journal-4cbea9e2528c.herokuapp.com%2Fabout%2F) | ![screenshot](documentation/testing/html-validator-about.png) | Element p not allowed as child of element span in this context. (Suppressing further errors from this subtree.) Bad value 75% for attribute width on element img. |

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
| manage.py | ![screenshot](documentation/testing/manage_pyp.png) | Pass: No Errors |
| settings.py | ![screenshot](documentation/testing/settings_py.png) | E128 continuation line under-indented for visual indent. E124 closing bracket does not match visual indentation. |
| About admin.py | ![screenshot](documentation/testing/about_admin_py.png) |  Pass: No Errors |
| About models.py | ![screenshot](documentation/testing/about_models_py.png) | Pass: No Errors |
| About views.py | ![screenshot](documentation/testing/about_views_py.png) | Pass: No Errors |
| Blog admin.py | ![screenshot](documentation/testing/blog_admin_py.png) | Pass: No Errors |
| Blog models.py | ![screenshot](documentation/testing/blog_models_py.png) | Pass: No Errors |
| Blog urls.py | ![screenshot](documentation/testing/blog_urls_py.png) | Pass: No Errors |
| Blog views.py | ![screenshot](documentation/testing/blog_views_py.png) | Pass: No Errors |
| Contact admin.py | ![screenshot](documentation/testing/contact_admin_py.png) | Pass: No Errors |
 Contact forms.py | ![screenshot](documentation/testing/contact_forms_py.png) | Pass: No Errors |
| Contact models.py | ![screenshot](documentation/testing/contact_models_py.png) | Pass: No Errors |
| Contact urls.py | ![screenshot](documentation/testing/contact_urls_py.png) | Pass: No Errors|
| Contact views.py | ![screenshot](documentation/testing/contact_views_py.png) | E501 line too long (115 > 79 characters).|

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

The production site was tested using [Browserstack](https://www.browserstack.com/) to ensure compatibility across various devices, and browsers including Mac, iPhone, Windows and Android, Chrome, Safari and Firefox on different pages chosen at random.

![screenshot](documentation/testing/broswer-chrome.png)

![screenshot](documentation/testing/browser-andriod-chrome.png)

![screenshot](documentation/testing/browser-iphone15-safari.png)

![screenshot](documentation/testing/browser-microsoft-edge.png)

![screenshot](documentation/testing/browser-safari.png)

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Contact | Blog Details | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsive-mobile-home.png) | ![screenshot](documentation/responsive-mobile-about.png) | ![screenshot](documentation/responsive-mobile-contact.png) | ![screenshot](documentation/responsive-mobile-blog-detail.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsive-tablet-home.png) | ![screenshot](documentation/responsive-tablet-about.png) | ![screenshot](documentation/responsive-tablet-contact.png) | ![screenshot](documentation/responsive-tablet-blog-detail.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsive-desktop-home.png) | ![screenshot](documentation/responsive-desktop-about.png) | ![screenshot](documentation/responsive-desktop-contact.png) | ![screenshot](documentation/responsive-desktop-blog-detail.png) | Works as expected |
| XL Monitor | ![screenshot](documentation/responsive-xl-home.png) | ![screenshot](documentation/responsive-xl-about.png) | ![screenshot](documentation/responsive-xl-contact.png) | ![screenshot](documentation/responsive-xl-blog-detail.png) | Scaling starts to have minor issues |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

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
| | Click on Blog Post link (title/exceprt in card) | Redirection to blog detail page for that post | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter name | Field will accept text / numbers | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to Contact page (blank form) and displays succes message | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address (optional - can be blank) | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Redirects user to Home page, with user logged in, and displays succes message | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to view an intuitive website with straightforward navigation that is fully responsive. | ![screenshot](documentation/features/navigation_logged_out.png) |
| As a new site user, I would like to create an account so that I can comment on and like blog posts. | ![screenshot](documentation/features/signup.png) |
| As a new site user, I would like to easily edit and delete any comments that I make. | ![screenshot](documentation/features/edit-comment.png) |
| As a new site user, I would like to easily contact the website administrators with questions. | ![screenshot](documentation/features/contact-page.png) |
| As a new site user, I would like to easily understand the main purpose of the site. | ![screenshot](documentation/features/about_page.png) |
| As a new user, I want attractive and relevant visuals and colour schemes that work with the content. | n/a |
| As a returning site user, I would like to view an intuitive website with straightforward navigation that is fully responsive. | ![screenshot](documentation/features/navigation_logged_in.png) |
| As a returning site user, I would like to easily log into my account so that I can comment on and like blog posts. | ![screenshot](documentation/features/login.png) |
| As a returning site user, I would like to easily edit and delete any comments that I make. | ![screenshot](documentation/features/edit-comment.png) |
| As a site administrator, I would like to have a recognizable branded admininstator area to manage users, blog posts, blogs comments and blog likes. | ![screenshot](documentation/features/admin-area.png) |
| As a site administrator, I would like to easily create blog postings in draft or published form, for display on Jetset Journal. | ![screenshot](documentation/features/admin-create-post.png) |
| As a site administrator, I would like to easily edit the about text and profile picture using a user-friendly UI. | ![screenshot](documentation/features/about_table_ui.png) |
| As a site administrator, I would like to have control over approving user comments before they appear on the front-end. | ![screenshot](documentation/features/edit-comment-not-approved.png) |
| As a site administrator, I would like to manage user contact requests and mark them as read. | ![screenshot](documentation/features/contact-table.png) |
| As a site administrator, I would like to have a simple UI that will encourage users to return and engage with the blog. | n/a |

## Automated Testing

I have conducted a series of automated tests on my application.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Adjust the code below (file names, etc.) to match your own project files/folders.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

I have used Django's built-in unit testing framework to test the application functionality.

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

Below are the results from the various apps on my application that I've tested:

| App | File | Coverage | Screenshot |
| --- | --- | --- | --- |
| Bag | test_forms.py | 99% | ![screenshot](documentation/py-test-bag-forms.png) |
| Bag | test_models.py | 89% | ![screenshot](documentation/py-test-bag-models.png) |
| Bag | test_urls.py | 100% | ![screenshot](documentation/py-test-bag-urls.png) |
| Bag | test_views.py | 71% | ![screenshot](documentation/py-test-bag-views.png) |
| Checkout | test_forms.py | 99% | ![screenshot](documentation/py-test-checkout-forms.png) |
| Checkout | test_models.py | 89% | ![screenshot](documentation/py-test-checkout-models.png) |
| Checkout | test_urls.py | 100% | ![screenshot](documentation/py-test-checkout-urls.png) |
| Checkout | test_views.py | 71% | ![screenshot](documentation/py-test-checkout-views.png) |
| Home | test_forms.py | 99% | ![screenshot](documentation/py-test-home-forms.png) |
| Home | test_models.py | 89% | ![screenshot](documentation/py-test-home-models.png) |
| Home | test_urls.py | 100% | ![screenshot](documentation/py-test-home-urls.png) |
| Home | test_views.py | 71% | ![screenshot](documentation/py-test-home-views.png) |
| Products | test_forms.py | 99% | ![screenshot](documentation/py-test-products-forms.png) |
| Products | test_models.py | 89% | ![screenshot](documentation/py-test-products-models.png) |
| Products | test_urls.py | 100% | ![screenshot](documentation/py-test-products-urls.png) |
| Products | test_views.py | 71% | ![screenshot](documentation/py-test-products-views.png) |
| Profiles | test_forms.py | 99% | ![screenshot](documentation/py-test-profiles-forms.png) |
| Profiles | test_models.py | 89% | ![screenshot](documentation/py-test-profiles-models.png) |
| Profiles | test_urls.py | 100% | ![screenshot](documentation/py-test-profiles-urls.png) |
| Profiles | test_views.py | 71% | ![screenshot](documentation/py-test-profiles-views.png) |
| x | x | x | repeat for all remaining tested apps/files |

#### Unit Test Issues

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

Use this section to list any known issues you ran into while writing your unit tests.
Remember to include screenshots (where possible), and a solution to the issue (if known).

This can be used for both "fixed" and "unresolved" issues.

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

## Bugs

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/roc-11/pp4-jetset-journal/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/roc-11/pp4-jetset-journal/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/roc-11/pp4-jetset-journal/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/roc-11/pp4-jetset-journal/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/roc-11/pp4-jetset-journal/issues/3) | Closed |

**Open Issues**

Any remaining open issues can be tracked [here](https://github.com/roc-11/pp4-jetset-journal/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/roc-11/pp4-jetset-journal/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/roc-11/pp4-jetset-journal/issues/5) | Open |

## Unfixed Bugs

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑 START OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑 END OF NOTES (to be deleted) 🛑🛑🛑🛑🛑

There are no remaining bugs that I am aware of.
