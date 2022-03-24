const doc = document.firstElementChild;
const nav = document.getElementById('primary-navigation');
const navToggle = document.getElementById('nav-toggle');
const navButtonText = document.getElementById('nav-button-text');
const accountToggle = document.getElementById('account-toggle');
const accountMenu = document.getElementById('account-menu');
const storageKey = 'theme-preference';
const colorModeToggle = document.getElementById('color-mode');
  

navToggle.addEventListener('click', () => {
    const visibility = nav.getAttribute('data-visible');
    if (visibility === 'false') {
        nav.setAttribute('data-visible', true);
        navToggle.setAttribute('aria-expanded', true);
    } else {
        nav.setAttribute('data-visible', false);
        navToggle.setAttribute('aria-expanded', false);
    }
})

// color scheme preference code adapted from 
// https://github.com/argyleink/gui-challenges
const changeTheme = () => {
    // flip current value
    theme.value = theme.value === 'light' ? 'dark' : 'light'
    setPreference()
}

const getColorPreference = () => {
    if (localStorage.getItem(storageKey)) {
        return localStorage.getItem(storageKey)
    } else {
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    }
}

const setPreference = () => {
    localStorage.setItem(storageKey, theme.value)
    reflectPreference()
}

const reflectPreference = () => {
    doc.setAttribute('data-theme', theme.value)
    colorModeToggle ?.setAttribute('aria-label', theme.value)
    if (theme.value === 'light') {
        colorModeToggle.checked = false;
    } else {
        colorModeToggle.checked = true;
    }
}

const theme = {
    value: getColorPreference(),
}

// set early so no page flashes / CSS is made aware
reflectPreference()

window.onload = () => {
    // set on load so screen readers can see latest value on the button
    reflectPreference()
    
    // now this script can find and listen for clicks on the control
    colorModeToggle.addEventListener('click', changeTheme)
}

// sync with system changes
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', ({matches:isDark}) => {
    theme.value = isDark ? 'dark' : 'light'
    setPreference()
})

// when someone clicks the hamburger menu button
// if the nav is closed, open it
// if the nav is open, close it
accountToggle.addEventListener('click', () => {
    const visibility = accountMenu.getAttribute('data-visible');
    if (visibility === 'false') {
        accountMenu.setAttribute('data-visible', true);
        accountToggle.setAttribute('aria-expanded', true);
    } else {
        accountMenu.setAttribute('data-visible', false);
        accountToggle.setAttribute('aria-expanded', false);
    }
})

// adds csrf token to htmx submissions
// document.body.addEventListener('htmx:configRequest', (event) => {
//     event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
// })

// Create or Edit Recipe form
// const deleteIngredientButton = document.getElementById('delete-ingredient');
// const deleteStepButton = document.getElementById('delete-step');

// for (let i = 0; i < editIngredientBtns.length; i++){
//     editIngredientBtns[i].addEventListener('click', disableOtherButtons)
// }
// for (let i = 0; i < editStepBtns.length; i++){
//     editStepBtns[i].addEventListener('click', disableOtherButtons)
// }

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

// document.addEventListener('click', (event)=>{
//     // remove this console log before final push.
//     console.log(event.target, event.target.id,)
//     if (event.target.matches('.edit-ingredient-btn')) {
//         disableOtherButtons();
//     } else if (event.target.matches('.edit-step-btn')){
//         disableOtherButtons();
//     } else if (event.target.id == 'add-ingredient-form-button') {
//         // const button = document.getElementById('add-ingredient-form-button');
//         // disableButton(button);
//         // needs a time interval for the htmx to finish inserting the form.
//         setTimeout(function() {
//             addCancelButton(event)
//         }, 500);
//         disableOtherButtons();
//     } else if (event.target.id == 'cancel-add-ingredient') {
//         const form = document.getElementById('add-ingredient-form');
//         removeForm(form);
//         enableOtherButtons();
//     }  else if (event.target.id == 'add-step-form-button') {
//         setTimeout(function() {
//             addCancelButton(event)
//         }, 500);
//         disableOtherButtons();
//     } else if (event.target.id == 'cancel-add-step') {
//         const form = document.getElementById('add-step-form');
//         removeForm(form);
//         enableOtherButtons();
//     } else if (event.target.id == 'add-step-form-submit') {
//         enableOtherButtons();
//     } else if (event.target.id == 'add-ingredient-form-submit') {
//         enableOtherButtons();
//     }
// })

document.addEventListener('click', (event)=>{
    // remove this console log before final push.
    console.log(event.target, event.target.id,)
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
    };
    
    for (const elementId of disableElementIds){
        if (event.target.id == elementId){
            disableOtherButtons();
            setTimeout(function() {
                addCancelButton(event)
            }, 500);
        }
    };

    for (const elementId of enableElementIds){
        if (event.target.id == elementId){
            enableOtherButtons();
            if (event.target.id == 'cancel-add-ingredient'){
                removeForm('add-ingredient-form');
            } else if (event.target.id == 'cancel-add-step'){
                removeForm('add-step-form');
            };
        };
    };
})

function removeForm(formId) {
    const form = document.getElementById(formId);
    form.remove();
}

function addCancelButton(event) {
    let newButton = document.createElement('button');
    newButton.innerText = 'Cancel';
    newButton.setAttribute('class', 'btn secondary-action mt-2');
    let form;
    if (event.target.id == 'add-ingredient-form-button') {
        form = document.getElementById('add-ingredient-form');
        newButton.setAttribute('id', 'cancel-add-ingredient');
        form.appendChild(newButton)
    } else if (event.target.id == 'add-step-form-button') {
        form = document.getElementById('add-step-form')
        newButton.setAttribute('id', 'cancel-add-step');
        form.appendChild(newButton)
    }
}

function disableButton(button) {
    button.disabled = true;
}

function enableButton(button) {
    button.disabled = false;
}


