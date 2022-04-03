const doc = document.firstElementChild;
const nav = document.getElementById('primary-navigation');
const navToggle = document.getElementById('nav-toggle');
const accountToggle = document.getElementById('account-toggle');
const accountMenu = document.getElementById('account-menu');
const pageCover = document.getElementById('mobile-nav-page-cover');
const storageKey = 'theme-preference';
const colorModeToggle = document.getElementById('color-mode');
const pageBtns = document.getElementsByClassName('page-btn');
const searchForm = document.getElementById('search-form');
const imageInput = document.getElementById('id_profile_image');
const recipeImageInput = document.getElementById('id_featured_image');

// listen for click on rest of page when menu open to close menu
pageCover.addEventListener('click', () => {
    nav.setAttribute('data-visible', false);
    navToggle.setAttribute('aria-expanded', false);
    if (accountMenu){
        accountMenu.setAttribute('data-visible', false);
        accountToggle.setAttribute('aria-expanded', false);
    }
    pageCover.style.display = 'none';
});

// toggle the menu open and closed via button
navToggle.addEventListener('click', () => {
    const visibility = nav.getAttribute('data-visible');
    if (visibility === 'false') {
        nav.setAttribute('data-visible', true);
        navToggle.setAttribute('aria-expanded', true);
        pageCover.style.display = 'block';
    } else {
        nav.setAttribute('data-visible', false);
        navToggle.setAttribute('aria-expanded', false);
        if (accountMenu) {
            accountMenu.setAttribute('data-visible', false);
            accountToggle.setAttribute('aria-expanded', false);
        }
        pageCover.style.display = 'none';

    }
});

// toggle the user account menu open and closed via button
if (accountToggle) {
    accountToggle.addEventListener('click', () => {
        const visibility = accountMenu.getAttribute('data-visible');
        if (visibility === 'false') {
            accountMenu.setAttribute('data-visible', true);
            accountToggle.setAttribute('aria-expanded', true);
        } else {
            accountMenu.setAttribute('data-visible', false);
            accountToggle.setAttribute('aria-expanded', false);
        }
    });
}

// color scheme preference code adapted from 
// https://github.com/argyleink/gui-challenges
const changeTheme = () => {
    // flip current value
    theme.value = theme.value === 'light' ? 'dark' : 'light';
    setPreference();
};

const getColorPreference = () => {
    if (localStorage.getItem(storageKey)) {
        return localStorage.getItem(storageKey);
    } else {
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
};

const setPreference = () => {
    localStorage.setItem(storageKey, theme.value);
    reflectPreference();
};

const reflectPreference = () => {
    doc.setAttribute('data-theme', theme.value);
    colorModeToggle ?.setAttribute('aria-label', theme.value);
    if (theme.value === 'light') {
        colorModeToggle.checked = false;
    } else {
        colorModeToggle.checked = true;
    }
};

const theme = {
    value: getColorPreference(),
};

// set early so no page flashes / CSS is made aware
reflectPreference();

window.onload = () => {
    // set on load so screen readers can see latest value on the button
    reflectPreference();
    
    // now this script can find and listen for clicks on the control
    colorModeToggle.addEventListener('click', changeTheme);
};

// sync with system changes
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', ({matches:isDark}) => {
    theme.value = isDark ? 'dark' : 'light';
    setPreference();
});
// end of adapted code from https://github.com/argyleink/gui-challenges

// disables buttons on recipe edit form to prevent multiple forms
// being opened and edited at the same time.
function disableOtherButtons(){
    const editIngredientBtns = document.getElementsByClassName('edit-ingredient-btn');
    const deleteIngredientBtns = document.getElementsByClassName('delete-ingredient-btn');
    const editStepBtns = document.getElementsByClassName('edit-step-btn');
    const deleteStepBtns = document.getElementsByClassName('delete-step-btn');
    for (let i = 0; i < editIngredientBtns.length; i++){
        disableButton(editIngredientBtns[i]);
    }
    for (let i = 0; i < deleteIngredientBtns.length; i++){
        disableButton(deleteIngredientBtns[i]);
    }
    for (let i = 0; i < editStepBtns.length; i++){
        disableButton(editStepBtns[i]);
    }
    for (let i = 0; i < deleteStepBtns.length; i++){
        disableButton(deleteStepBtns[i]);
    }
    const addIngredButton = document.getElementById('add-ingredient-form-button');
    disableButton(addIngredButton);
    
    const addStepButton = document.getElementById('add-step-form-button');
    disableButton(addStepButton);
}

// enables buttons once form has been edited on recipe edit form
function enableOtherButtons(){
    const editIngredientBtns = document.getElementsByClassName('edit-ingredient-btn');
    const deleteIngredientBtns = document.getElementsByClassName('delete-ingredient-btn');
    const editStepBtns = document.getElementsByClassName('edit-step-btn');
    const deleteStepBtns = document.getElementsByClassName('delete-step-btn');
    for (let i = 0; i < editIngredientBtns.length; i++){
        enableButton(editIngredientBtns[i]);
    }
    for (let i = 0; i < deleteIngredientBtns.length; i++){
        enableButton(deleteIngredientBtns[i]);
    }
    for (let i = 0; i < editStepBtns.length; i++){
        enableButton(editStepBtns[i]);
    }
    for (let i = 0; i < deleteStepBtns.length; i++){
        enableButton(deleteStepBtns[i]);
    }
    const addIngredButton = document.getElementById('add-ingredient-form-button');
    enableButton(addIngredButton);

    const addStepButton = document.getElementById('add-step-form-button');
    enableButton(addStepButton);
}

// listen for click on edit ingredient or step buttons
// calls functions to disable or enable other buttons as necessary
document.addEventListener('click', (event)=>{
    const elementClass = ['.edit-ingredient-btn', '.edit-step-btn'];
    const disableElementIds = ['add-ingredient-form-button', 'add-step-form-button'];
    const enableElementIds = ['cancel-add-ingredient',
                              'cancel-add-step',
                              'add-step-form-submit',
                              'add-ingredient-form-submit'];
    
    for (let i = 0; i < elementClass.length; i++) {
        if (event.target.matches(elementClass[i])){
            disableOtherButtons();
        }
    }
    
    for (const elementId of disableElementIds){
        if (event.target.id == elementId){
            disableOtherButtons();
            setTimeout(function() {
                addCancelButton(event);
            }, 500);
        }
    }

    for (const elementId of enableElementIds){
        if (event.target.id == elementId){
            enableOtherButtons();
            if (event.target.id == 'cancel-add-ingredient'){
                removeForm('add-ingredient-form');
            } else if (event.target.id == 'cancel-add-step'){
                removeForm('add-step-form');
            }
        }
    }
});

// removes the form when users cancels action
function removeForm(formId) {
    const form = document.getElementById(formId);
    form.remove();
}

// inserts a cancel option for user experience improvements
function addCancelButton(event) {
    let newButton = document.createElement('button');
    newButton.innerText = 'Cancel';
    newButton.setAttribute('class', 'btn secondary-action mt-2');
    let form;
    if (event.target.id == 'add-ingredient-form-button') {
        form = document.getElementById('add-ingredient-form');
        newButton.setAttribute('id', 'cancel-add-ingredient');
        form.appendChild(newButton);
    } else if (event.target.id == 'add-step-form-button') {
        form = document.getElementById('add-step-form');
        newButton.setAttribute('id', 'cancel-add-step');
        form.appendChild(newButton);
    }
}

// tags button element with disabled state
function disableButton(button) {
    button.disabled = true;
}

// removes disabled state from button element
function enableButton(button) {
    button.disabled = false;
}

// listener for inputs in form fields to update remaining character text
document.addEventListener('input', (event) => {
    const elementIds = ['id_username',
                        'id_headline',
                        'id_bio',
                        'id_location',
                        'id_social_youtube',
                        'id_social_website',
                        'id_title',
                        'id_description',
                        'id_youtube_link',
                        'id_ingredient',
                        'id_quantity',
                        'id_step'];
    for (const elementId of elementIds) {
        if (event.target.id == elementId) {
            const field = document.getElementById(elementId);
            updateCharContainer(field);
        }
    }
});

// updates value of remaining character text
function updateCharContainer(field) {
    const max = field.getAttribute('maxlength');
    const remaining = max - field.value.length;
    const charContainer = field.nextElementSibling;
    charContainer.textContent = `${remaining} Characters Remaining`;
    if (remaining < (max * 0.1)) {
        charContainer.style.color = 'var(--alert-primary)';
    } else if (remaining >= (max * 0.1)) {
        charContainer.style.color = 'var(--text-primary)';
    }

    if (remaining == 0){
        charContainer.style.fontSize = '1.25rem';
    } else {
        charContainer.style.fontSize = '0.8rem';
    }
}

// auto dismiss messages
window.setTimeout(function(){
    let message = document.getElementsByClassName('alert');
    Array.from(message).forEach(ele => {
        // prevent error messages from being removed automatically
        if (!ele.classList.contains('alert-error')){
            ele.remove();
        }
    });
}, 3000);

// controls the pagination buttons to ensure they go to correct part of dataset
if (searchForm){
    for (let i = 0; i < pageBtns.length; i++) {
        pageBtns[i].addEventListener('click', function(e){
            e.preventDefault();
            let page = this.dataset.page;
            searchForm.innerHTML += `<input value=${page} name="page" hidden />`;
            searchForm.submit();
        });
    }
}

// looks for the image input field in the edit profile form
// then captures the image href and inserts it as an image and modifies the attributes of the link.
if (imageInput) {
    if (imageInput.parentElement.matches(".edit-profile-form-input-container")) {
        let secondPreviousSibling = imageInput.previousElementSibling.previousElementSibling;
        let source = secondPreviousSibling.getAttribute('href');
        secondPreviousSibling.innerHTML = `<img src=${source} alt="current profile image">`;
        secondPreviousSibling.setAttribute('target', '_blank');
        secondPreviousSibling.setAttribute('aria-label', 'opens the current profile image in a new window');
    }
}

// looks for the image input field in the recipe form
// then captures the image href and inserts it as an image and modifies the attributes of the link.
if (recipeImageInput) {
    if (recipeImageInput.parentElement.matches(".form-pair")) {
        let secondPreviousSibling = recipeImageInput.previousElementSibling.previousElementSibling;
        let source = secondPreviousSibling.getAttribute('href');
        secondPreviousSibling.innerHTML = `<img src=${source} alt="current recipe featured image">`;
        secondPreviousSibling.setAttribute('target', '_blank');
        secondPreviousSibling.setAttribute('aria-label', 'opens the current recipe image in a new window');
    }
}