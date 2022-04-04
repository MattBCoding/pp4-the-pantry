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

## User Story Testing - By Epic

2. User Profile

	> US#13 - Create a User Account - As a User, I would like to be able to create an account, so that I can create and save recipes

* Acceptance Criteria 1
    * Given that I am an unregistered user When I am on the homepage Then I can see a button to sign up And, When I click on the button Then I am taken to the user registration page

This is achieved by the link in the standard navigation bar for login/register
![Standard Nav Bar](/assets/screenshots/standard-navbar.png)

It is also achieved by the standard button in the member benefits section
![Standard Member Benefits](/assets/screenshots/standard-member-benefits.png)

* Acceptance Criteria 2
    * Given that I am an unregistered user
And, I am on the user registration page
When I enter my username, email address and password
And, I click on the register button
Then The system creates me an account
And, signs me in

This is achieved - although the process includes email verification and the user has to sign in themselves due to the security settings chosen for the site

* Acceptance Criteria 3
    * Given that I have an account
And, I am signed into the account
When I have an option to create a recipe
And, when I click on that option
Then I am taken to a page where I can provide the details of my recipe

This is achieved, the option to add a recipe appears in the user menu as part of the main navigation bar
![Logged in Nav Bar User Menu Open](/assets/screenshots/logged-in-navbar-user-menu-open.png)

* Acceptance Criteria 4
    * Given that I am a registered user
When I am signed into my account
Then I do not see the register button

This is achieved - the login/register link within the standard navigation bar is replaced with a user menu for logged in users - see image on acceptance criteria 1.

	> US#14 - Users can view their profile - As a User, I would like to be able to see the details in my user profile, so that I can see what information other users can see about me

* Acceptance Criteria 1
    * Given that I am logged into my user account
When I can access an option to view my profile
Then my profile details are displayed as they appear to other users

* Acceptance Criteria 2
    * Given that I have a user profile,
When I click on my user name on my user card
Then I can bring up my full user profile as it appears to other users

These are achieved - the user profile page displays the information visable to other users - if information is displayed that other users can not see then it is clearly labelled.
![Owner Profile Page](/assets/screenshots/owner-profile-page.png)

	> US#15 - Users can edit their profile - As a User, I would like to be able to edit my profile, so that I can keep the information upto date

* Acceptance Criteria 1
    * Given that I am logged into my account
When I am viewing my profile
Then I should be able to edit the details

This is achieved - edit button appears on user profile when account owner is logged in and viewing their own profile. See previous image.

* Acceptance Criteria 2
    * Given that I am logged into my account
When I click on the edit button on my profile page
Then I should be taken to a page to edit the details

This is achieved - the user is taken to the edit profile form page
![Edit profile page](/assets/screenshots/edit-profile-page.png)

* Acceptance Criteria 3
    * Given that I am not logged into my account
When I view my profile page, or anyone elses
Then I should not be able to see the edit button

This is achieved - the button only appears on your own profile

* Acceptance Criteria 4
    * Given that I am not logged into my account
When I type in the address to edit my profile, or anyone elses
Then I should be redirected to the log in page.

This is achieved, the all auth redirect takes users to the login page when they request access directly to a page that requires them to be logged in.

	> US#16 - Users can delete their account - As a User, I can delete my account, so that I can remove my details and recipes at my request

* Acceptance Criteria 1
    * Given that I am a registered user
When I navigate to my account
Then I have an option to delete my account

This is achieved - screenshot on user story 14 acceptance criteria two.

* Acceptance Criteria 2
    * Given that I am a registered user viewing my account details
When I click on the option to delete my account
Then I am requested to confirm the request

This is achieved - the user is required to complete a form by typing in the email address associated with the account in order to confirm the delete request.

* Acceptance Criteria 3
    * Given that I am a registered user viewing my account details
When I click on the option to delete my account
And, When I confirm the request
Then My account and the recipes that I have created are deleted

This is achieved, the account, any recipes, ingredients and steps created, all likes and favourites are removed from the database correctly

* Acceptance Criteria 4
    * Given that I am a registered user
When I delete my account
Then I should receive confirmation of the account deletion

This is achieved - the user receives a visual message confirming the account has been deleted.

	> US#17 - Users can change their password - As a user, I would like to be able to change my password, so that I can keep my account secure

* Acceptance Criteria 1
    * Given that I am a registered User, logged in to my account
When I navigate to the edit profile page
Then I have the option to change my password

This is achieved - the user has the option to change their password - it is accessed on the edit profile page
![Account Options Buttons](/assets/screenshots/account-options-buttons.png)

* Acceptance Criteria 2
    * Given that I am logged in to my account
When I change my password
Then I receive an email confirming my password has been changed

This was achieved in a slightly different way. Password resets occur via email - password changes taking place on the site are confirmed to the user through the site.

* Acceptance Criteria 3
    * Given that I am logged into my account
When I try to change my password
Then I am prevented from creating a password that does not meet security requirements

This is achieved - the form validation prevents the user submitting the form with a password that does not meet the requirements.

* Acceptance Criteria 4
    * Given that I am logged into my account
When I click the change password link
Then I am taken to the change password form
** And When** I correctly complete the form
And, press submit
Then My password is changed to the new value
And, I receive confirmation on the screen of the change.

This is achieved - the user receives a message on screen confirming the password change has occurred.

	> US#18 - Users can reset their password - As a User, I would like to be able to reset my password, so that if I forget it I can still access my account

* Acceptance Criteria 1
    * Given that I am a forgetful user
When I try to login with an incorrect password
Then An option is available to reset my password

This is achieved - there is an option on the sign in screen for those who have forgotten their password - they are emailed a reset password link

* Acceptance Criteria 2
    * Given that I click on the link to reset my password
When I enter my email address that I used to sign up,
Then I should receive an email with instructions on how to reset my password

This is achieved - as above.

* Acceptance Criteria 3
    * Given that I have received the email to reset my password
When I follow the instructions
Then my password should be reset, or I should be able to set a new password of my choosing
And When I do not follow the instructions,
Then my password should not be reset

This is achieved - the user has to complete the process for the password to be reset.

3. User sign in or sign out
	
	> US#19 - User Account Login / Logout - As a User, I would like to be able to login or logout of my account, so that I can keep my account secure

* Acceptance Criteria 1
    * Given that I am a registered user, who is not logged in
When I navigate to the sign in page
And, I enter my credentials correctly and press sign in
Then I am signed into my account

This is achieved - the user gets visual message to confirm the sign in, the nav bar also changes accordingly

* Acceptance Criteria 2
    * Given that I am a registered user, who is currently logged in
When I click on the sign out link
Then I am signed out of my account

This is achieved - the user gets visual confirmation and the nav bar changes back to the standard navbar accordingly

* Acceptance Criteria 3
    * Given that I am a registered user, who has signed out of my account
When I use the browser navigation buttons such as back button
Then I can not access information which requires me to be signed in

This is achieved. the user is redirected to the sign in page.

	> US#20 - Features restricted to signed in users - As a Site Owner, I would like to restrict some features of the site to registered users, so that it encourages people to sign up to the site

* Acceptance Criteria 1
    * Given that a user is not registered or signed in,
When they view a recipe,
Then they are unable to save a recipe

This is achieved - the button to save a recipe only appears to authenticated users

* Acceptance Criteria 2
    * Given that a user is not registered or signed in,
When they look at the recipe options
Then they do not have the ability to create a recipe

This is achieved - the option appears in the user menu in the navbar, the user menu only appears when the user is logged in

* Acceptance Criteria 3
    * Given that a user is not registered or signed in,
When they look at a recipe
Then they are unable to provide a rating or comment

This is achieved, the option only appears to authenticated users

* Acceptance Criteria 4
    * Given that a user is not registered or signed in,
When they encounter functionality that requires them to be signed in
Then they are presented with a login or register button.

This is achieved - if the user navigates directly to a url requiring them to be logged in, they are redirected to the login page.

4. User recipes

	> US#22 - Create a Recipe - As a User, I would like to be able to share my own recipes, with family and friends so they can teach them to their own children and have fun experiences together baking

* Acceptance Criteria 1
    * Given that I am a logged in user
When I navigate to the recipe section
Then I have the option to create a recipe

This is achieved, the option only appears to authenticated users in the user menu section of the navbar

* Acceptance Criteria 2
    * Given that I have created a recipe as a logged in user
When I save the completed recipe
Then it is available to other users to view

This is achieved - completed recipes will appear to other users - incomplete recipes show as incomplete and do not show to other users.

	> US#23 - View Recipes - As a User, I can access the recipes on the site, so that I can follow them at home

* Acceptance Criteria 1
    * Given that I am a user on the site
When I navigate to the recipes page
Then I am presented with a list of the recipes available

This is achieved - all users have access to the completed recipes.

* Acceptance Criteria 2
    * Given that I am a user on the site
When I navigate to the recipes page
And When I click on a recipe
Then I am presented with the full recipe details

This is achieved - the recipe summary cards link to the recipe details page for that recipe object.

	> US#24 - Update a recipe - As a user, I can update a recipe that I have created, so that I can correct any mistakes I may have made

* Acceptance Criteria 1
    * Given that I am a registered user who has created a recipe
When I navigate to that recipe
Then I have the option to edit the details

This is achieved - the recipe owner has the ability to edit the details or delete the recipe

* Acceptance Criteria 2
    * Given that I am a registered user
When I navigate to someone else's recipe
Then I do not get the edit option

This is achieved - only the recipe owner has access to this functionality

* Acceptance Criteria 3
    * Given that I am a registered user who has created a recipe
When I navigate to that recipe, and click the option to edit the details
Then I am able to edit the details of the recipe

This is achieved - the button links to the edit recipe page

* Acceptance Criteria 4
    * Given that I am a registered user who has created a recipe
When I navigate to the recipe, click the option to edit the details
And When I have edited the details of the recipe
Then I have the option to save the changes

This is achieved - the option to save the recipe details appears on the form - changes to the ingredients and steps appear in their individual forms.

	> US#25 - Delete a recipe - As a user, I can delete a recipe that I have created, so that I can remove it from the site

* Acceptance Criteria 1
    * Given that I am a registered user who is logged in, and has created a recipe
When I navigate to the recipe that I would like to delete
Then I have the option to delete the recipe

This is achieved - the option to delete the recipe appears for the recipe owner.

* Acceptance Criteria 2
    * Given that I am a registered user who is logged in, has created a recipe and I am viewing the recipe I wish to delete
When I click the delete recipe button
Then I receive a confirmation window to confirm that I really want to delete the recipe

This is achieved - the confirmation window appears in a modal which the user has to select correctly to confirm the delete request

* Acceptance Criteria 3
    * Given that I am a registered user who is logged in, has created a recipe, navigated to that recipe and clicked on the delete recipe button
When the confirmation window appears and I confirm the deletion
Then the recipe is deleted from the system

This is achieved - the recipe is deleted along with any associated ingredients and steps

* Acceptance Criteria 4
    * Given that I am a registered user, or a non registered user
When I navigate to a recipe page that I did not create
Then I do not have the option to delete the recipe

This is achieved - the option only appears to the recipe owner

5. Recipe management

	> US#26 - Save other people's recipes to my profile - As a User, I would like to be able to save new recipes, so that I can refer back to them easily at a later date.

* Acceptance Criteria 1
    * Given that I am a signed in user
When I find a recipe I would like to keep
Then I can save it to my own profile

This is achieved - liking the recipe saves it to the users profile

* Acceptance Criteria 2
    * Given that I am not a signed in user
When I find a recipe I would like to save
Then when I click on save, it reminds me to login
And When I login successfully
Then the recipe I originally wanted to save is saved

This functionality was decided to be unnecessary - the option to save the recipe by liking the recipe or adding to favourites does not appear to users not logged in.

* Acceptance Criteria 3
    * Given that I am an unregistered user
When I find a recipe I would like to save
Then when I click on save, it takes me to the login/register page
And When I successfully register an account
Then the recipe I originally wanted to save is saved

This was decided to be unnecessary as part of the above acceptance criteria

	> US#27 - Create a list of Favourite Recipes - As a User, I would like to be able to save my favourite recipes, so that I can find them quickly at a later date

* Acceptance Criteria 1
    * Given that I am a signed in user
When I want to look at my saved recipes
Then it should be clear where to find them

This is achieved - the user has the ability to navigate to my favourite recipes from the user menu

* Acceptance Criteria 2
    * Given that I am a signed in user
When I am looking at recipes I have previously saved
Then I should be able to mark my favourites

This is achieved - users can like a recipe which makes it appear on the users profile for easier access - when liked, they get the option to add it to their favourites as well.

* Acceptance Criteria 3
    * Given that I am a signed in user
When I look at a list of all my saved recipes
Then I should be able to see which are my favourites

This is achieved - there are two seperate sections for liked recipes and those marked favourites

* Acceptance Criteria 4
    * Given that I am a signed in user
When I want to look at only my favourite recipes
Then I should be able to filter my saved recipes to show only the favourites

This is achieved by the favourite recipes appearing on a seperate dedicated page.

6. Recipe searching

	> US#33 - Recipe Searching - As a User, I would like to be able to find recipes, so that I can increase the variety of meals we consume.

* Acceptance Criteria 1
    * Given that I am a user of the website
When I navigate to the homepage
Then I can access a link to all the recipes

This is achieved - any user can access any of the completed recipes.

* Acceptance Criteria 2
    * Given that I am a user of the website
When I enter the recipe section of the site
Then I have options to navigate to different recipe sections

This is achieved through the search functionality

* Acceptance Criteria 3
    * Given that I am a user of the website
When I want to view a specific recipe
Then I can access the full recipe details by clicking on the recipe

This is achieved - the summary cards link to the recipe details page

	> US#34 - Recipe Search - Advanced - As a User, I would like to be able to search the recipes, so that I can find the ones that match my fancy at that point in time

* Acceptance Criteria 1
    * Given that I am a user of the website
When I navigate to the site
Then I can access a search function to access related recipes

The recipe search functionality can be accessed from both the homepage and the recipes page

* Acceptance Criteria 2
    * Given that I am a user of the website
When I search the recipes
Then the search results show relevant recipes

The recipe search functionality applies the search to both the recipe title and recipe authors username.

7. recipe viewing

	> US#39 - Clear Recipe Layout - As a User, I would like clear instructions on how to make each recipe, so that I am able to follow along as an inexperienced cook

* Acceptance Criteria 1
    * Given that I am a user
When I click on a recipe to view the details
Then The instructions on how to make the recipe are clearly accessible

This is achieved - the ingredients and steps are clearly seperated.

* Acceptance Criteria 2
    * Given that I am a user accessing the recipe details
When I access a recipe instructions
Then They should be easily to identify the order in which they should be followed

This is achieved - the recipe steps appear as list items in the order they were submitted by the recipe owner.

	US#36 - Recipe Summary Cards - As a User, I would like to be able to view multiple recipes at the same time, so that I can easily decide which one I want to follow

* Acceptance Criteria 1
    * Given that I am a user
When I search for or navigate to the full list of recipes
Then The recipes are summarised individually

This is achieved - the recipe search results appear as individual summary cards which link to the recipe detail page for each recipe.

* Acceptance Criteria 2
    * Given that I am a user and I have chosen which of the displayed recipes I'd like to select
When I click on the recipe
Then I am taken to the full recipe details

This is achieved - each summary card links to the recipe details page for each recipe.

8. recipe interaction

9. site owner objectives

	> US#47 - Responsive Templates - As a Site Owner, I would like my site to be fully responsive, so that Users accessing the site from different devices have an enjoyable experience

* Acceptance Criteria 1
    * Given that I am a user accessing the site on my smartphone
When I navigate through the site
Then all pages should be formatted to my device

This is achieved - all pages are fully responsive

* Acceptance Criteria 2
    * Given that I am a user accessing the site on my tablet
When I navigate through the site
Then all pages should be formatted to my device

This is achieved - all pages are fully responsive

* Acceptance Criteria 3
    * Given that I am a user accessing the site on my laptop
When I navigate through the site
Then all pages should be formatted to my device screen

This is achieved - all pages are fully responsive

* Acceptance Criteria 4
    * Given that I am a user accessing the site on my desktop computer
When I navigate the site
Then all pages should be formatted to suit my screen size

This is achieved - all pages are fully responsive

	> US#48 - Colour Scheme Preference options - As a Site Owner, I would like the site to havea dark colour option, so that users have the ability to view the site in a colour scheme they prefer.

* Acceptance Criteria 1
    * Given that users visit the site on different devices
When their device has a preferred-colour-scheme set
Then the site should be presented in that scheme

This is achieved - the JavaScript accessess the system preferred colour scheme value where possible.

* Acceptance Criteria 2
    * Given that users visit the site
When they manually set the colour scheme choice
Then the site should remember their preference

This is partially achieved through local session storage. 

* Acceptance Criteria 3
    * Given that users register for the site
When they log in to the site,
Then the site should change to their personal colour preference without setting a new preference on that device

This was not implemented - the prior two options should be sufficient.

10. recipe rating system

	> US#29 - Rate a Recipe - As a User, I can give a recipe a rating, so that I can provide the author feedback and rank recipes that I like

* Acceptance Criteria 1
    * Given that I am a logged in User
When I navigate to a recipe detail page
Then I have the ability to provide a rating

This was partially achieved through the provision of a like button.

* Acceptance Criteria 2
    * Given that I am a logged in User
When I navigate to a recipe detail page for a recipe I have previously given a rating
Then I can not provide an additional rating

This is achieved - user can like, or unlike a recipe. 

* Acceptance Criteria 3
    * Given that I am a logged in user
When I navigate to one of the recipes that I created
Then I can not provide a rating

This is achieved - users only receive the option to like a recipe that they did not create

* Acceptance Criteria 4
    * Given that I am a user that is not logged in
When I navigate to a recipe detail page
Then I do not have the ability to provide a rating

This is achieved- to like a recipe a user needs to be logged in and can not be the recipe owner.