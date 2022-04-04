# Test Cases and Execution Report

To navigate back to the main README click [here](README.md)

The full testing spreadsheet containing all the tests performed during the testing phase of development can be found [here](/assets/testing/test-schedule.pdf)

## Test Case 001

![Test Case 001](/assets/testing/test-case-0001.png)

### Python Validation
The Python code was checked using the pep8 validator available at [pep8online.com](https://pep8online.com). No errors were reported by the validator in the files I created. The settings.py file did however contain five line too long errors. Each of these errors related to Django default code pointing to password validation paths or from Cloudinary code pointing to the cloudinary storage service and could not be shortend.

* Screenshots of the validator reports are here:
    * Pantry Folder
        * [asgi.py file](/assets/screenshots/asgi-py.png) 
        * [settings.py file](/assets/screenshots/settings-py.png) 
        * [urls.py file](/assets/screenshots/urls-py.png) 
        * [wsgi.py file](/assets/screenshots/wsgi-py.png)
    * Profiles Folder 
        * [adapter.py file](/assets/screenshots/profiles-adapter-py.png) 
        * [admin.py file top](/assets/screenshots/profiles-admin-py.png)
        * [apps.py file](/assets/screenshots/profiles-apps-py.png) 
        * [forms.py file](/assets/screenshots/profiles-forms-py.png) 
        * [models.py file](/assets/screenshots/profiles-models-py.png) 
        * [urls.py file](/assets/screenshots/profiles-urls-py.png) 
        * [utils.py file](/assets/screenshots/profiles-utils-py.png)
        * [views.py file](/assets/screenshots/profiles-views-py.png)
    * Recipes Folder 
        * [admin.py file](/assets/screenshots/recipes-admin-py.png) 
        * [apps.py file](/assets/screenshots/recipes-apps-py.png) 
        * [forms.py file](/assets/screenshots/recipes-forms-py.png)
        * [models.py file](/assets/screenshots/recipes-models-py.png)
        * [urls.py file](/assets/screenshots/recipes-urls-py.png)
        * [utils.py file](/assets/screenshots/recipes-utils-py.png)
        * [views.py file](/assets/screenshots/recipes-views-py.png)

## Test Case 001a

![Test Case 001a](/assets/testing/test-case-0001a-b.png)

### JavaScript Validation
The JavaScript code was checked using the jshint.com validator available at [jshint.com](https://jshint.com/). No errors were detected within the files I created. The validator did return two warnings, one relating to optional chaining which is a ES11 feature that can be enabled within the validator. The second warning relates to potentially confusing semantics due to nested functions referencing outer scoped variables. This relates to a for loop that adds event listeners to each of the outer scoped variables.

* Screenshot of the validator report is available here:
    * JavaScript
        * [script.js file](/assets/screenshots/jshint-validation.png)

## Test Case 001b

![Test Case 001b](/assets/testing/test-case-0001a-b.png)

### CSS Validation
Whilst I utilised bootstrap 5 to control the main layout of the site and a bulk of the styling and spacing, a reasonable amount of custom CSS was still required. I tested the site using the Jigsaw CSS Validator service which returned no errors. Three warnings related to custom vendor prefixes were identified within the custom CSS file, along with a further warning that imported style sheets are not checked, these are not considered errors. The validation by URL returned 260 warnings from the bootstrap css file delivered by the cdn.

The full CSS Validator report is available here on the [CSS Validator Site](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fpp4-the-pantry.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

![CSS Validator Report](/assets/testing/css-validator.png)

## Test Case 001c

[Test Case 001c part 1](/assets/testing/test-case-0001-c-p1.png)
[Test Case 001c part 2](/assets/testing/test-case-0001-c-p2.png)
[Test Case 001c part 3](/assets/testing/test-case-0001-c-p3.png)

### HTML Validation
Due to the way Django templates include Django template code in them, and extend other templates, it is not possible to copy the code for each page out of the source html files. Therefore, in order to validate the code correctly, I navigated to the site and accessed the rendered html code through the developer tools of the browser I used during development, Google Chrome. I then pasted the code into the HTML validator site available at [W3C Markup Validation Service](https://validator.w3.org/). The validator returns one warning relating to a javascript link inserted by django into the base html file head, and six errors relating to the fontawesome cdn link which inserts CSS into the head of the html that is rendered in the browser. There were no errors returned from the HTML produced from the templates themselves.

Given that there is logic utilised within the templates to display some elements under different conditions, 34 test cases were developed to cover the different variations of logic available within the sites pages. Each is detailed in the full testing file available from the link at the top of this page, or in the screenshots at the top of this section. I decided not to include screenshots of the validation tests for this section as it is impossible to ascertain the page being tested from the screenshot and all pages return the same results.

## Test Case 002

![Test Case 002](/assets/testing/test-case-0002.png)

### Unregistered User Testing - General Site Navigation
The overall site navigation was testing fully to ensure all links directed the user to the correct page. Given that users will receive slightly differing navigation bars depending on if they are logged in or not, this was first tested fully for users who are not logged into the site. All links and the settings modal were tested for correct functioning.

## Test Case 003

![Test Case 003](/assets/testing/test-case-0003.png)

### Unregistered User Testing - Recipe Search
As users do not have to be registered on the site or logged in to access the search functionality or recipes, it is important that it was tested for full functionality for all users. The recipe search bar on the home page and recipes pages were tested to ensure recipes were returned matching the search query for both recipe owner and recipe titles. The search functionality was also tested to ensure the correct no results found template was inserted when no results were found for the search query used.

## Test Case 004

![Test Case 004](/assets/testing/test-case-004.png)

### Unregistered User Testing - Mobile device testing
The navigation bar functionality was tested for touch screen devices using an iPhone XR and an iPhone 6+. The open and closing of the menu was tested to ensure that when the user touches off the menu bar the menu closes appropriately. The modal functionality was tested for the same functionality.

## Test Case 005

![Test Case 005](/assets/testing/test-case-005.png)

### Unregistered User Testing - Sign Up Process
The user registration or sign up process was tested extensively. This included testing the form input validation for the sign up form, along with the correct display of error messages to the user. Upon registration the redirect to the next page was tested to ensure the redirect worked as expected. This page informs the user an email has been sent to the email address they provided to validate their email address. The admin panel was utilised to ensure the email address had been added to the database correctly - whilst also ensuring it had the correct status of unvalidated. The email account utilised for sign up was checked to ensure the email functionality of the site was sending emails correctly to the user - with the correct formatting and information included. The email validation process was utilised to validate the email address. The admin panel was further utilised to ensure that the validation reflected in the database correctly.
The sign in functionality was tested to ensure it would not allow users to sign in without validating the email address. It was also tested to ensure that it would not allow users to sign in without the correct email/password combination.
The redirect for the user upon sign in was tested to ensure the adapter function was correctly creating a user profile for the user when they first verified the email address. The redirect directed the browser to the user's profile page upon sign in correctly. The template logic for the user profile was tested to ensure that the user profile displayed the correct messages to the user.

## Test Case 006

![Test Case 006](/assets/testing/test-case-006.png)

### Registered User Testing - Change Email Process
As AllAuth was utilised for the user authentication and sign up/login functionality it provided a number of functionality options. The change email functionality was tested to ensure the custom redirects applied worked correctly. Given that the email verification allauth methods were adapted with a custom method in order to create and attach a profile for the user upon first verification, these were also tested to ensure that it did not create a duplicate user profile when the user changed their email address and verified the second email.

## Test Case 007

![Test Case 007](/assets/testing/test-case-007.png)

### Registered User Testing - Change Password Process
The change password process was tested to ensure that the password change was reflected to the user correctly, and the new password was implemented straight away. This also allowed for testing of the custom templates utilised for the password change form and the user messages confirming the change.

## Test Case 008

![Test Case 008-pt1](/assets/testing/test-case-008-pt1.png)
![Test Case 008-pt2](/assets/testing/test-case-008-pt2.png)

### Registered User Testing - Recipe CRUD Functionality
As the foundation for the site, the recipe CRUD functionality has the highest importance. An extensive testing process was utilised to ensure all possible combinations of user actions were tested. This included testing the javascript functionality utilised to display characters remaining messages to the user. Form validation. The prevention of incompleted recipes appearing in search results. The addition of an imcomplete banner to the recipe card which only displays in the users my recipes section. The HTMX library was utilisted to include the ingredient and step model forms within the recipe model form and JavaScript was utilised to enable and disable the appropriate button functionality. All functionality worked as expected.

## Test Case 009

![Test Case 009](/assets/testing/test-case-009.png)

### Registered User Testing - Recipe Like and Favourite Functionality
The recipe like functionality and the associated recipe favourite functionality were tested to ensure that if the user liked a recipe, it would provide a visual indication on the recipe card, and recipe detail pages as well as provide the user with a quicker access through their own profile page listing on liked recipes. The favourited recipes were tested to ensure they appeared correctly within the users my favourites page. Recipes which were liked, then favourited, then unlike should have the favourite tag removed automatically. This was tested both within the site and within the admin panel to ensure the logic was applying correctly. 

## Test Case 0010

![Test Case 0010](/assets/testing/test-case-0010.png)

### Registered User Testing - Delete User Account
Deletion of a user account was tested for multiple purposes. First the user request to delete the account was tested to ensure it was deleted from the database correctly. It was also tested to ensure the process utilised worked accordingly. This included the confirmation of the request to delete by way of confirming the email address associated with the account as a preventative measure. The deletion process was also tested to ensure all recipes, ingredients, steps, recipe likes and recipe favourites that the user created were deleted along with the account.

To navigate back to the main README click [here](README.md)

## Additional Manual Testing

The test cases were performed multiple times during the development of the site with adjustments made to the code logic and functionality based on user feedback.