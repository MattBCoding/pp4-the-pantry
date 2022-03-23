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
    if (localStorage.getItem(storageKey))
    return localStorage.getItem(storageKey)
    else
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
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
const deleteIngredientButton = document.getElementById('delete-ingredient');
const deleteStepButton = document.getElementById('delete-step');


document.addEventListener('click', (event)=>{
    console.log(event.target, event.target.id)
    // if (event.target.id == 'add-ingredient' || event.target.id == 'add-step') {
    //     addNewForm(event);
    // }
    if (event.target.id == 'add-ingredient-form-button') {
        // insert name of function here
        const button = document.getElementById('add-ingredient-form-button');
        disableButton(button);
        // needs a time interval for the htmx to finish inserting the form.
        setTimeout(function() {
            addCancelButton(event)
        }, 500);
        // addCancelButton();
    } else if (event.target.id == 'cancel-add-ingredient'){
        const form = document.getElementById('add-ingredient-form');
        const button = document.getElementById('add-ingredient-form-button');
        removeForm(form);
        enableButton(button);
    } else if (event.target.id == 'add-ingredient-form-submit'){
        const button = document.getElementById('add-ingredient-form-button');
        enableButton(button);
    } else if (event.target.id == 'add-step-form-button') {
        const button = document.getElementById('add-step-form-button');
        disableButton(button);
        setTimeout(function() {
            addCancelButton(event)
        }, 500);
    } else if (event.target.id == 'cancel-add-step'){
        const form = document.getElementById('add-step-form');
        const button = document.getElementById('add-step-form-button');
        removeForm(form);
        enableButton(button);
    } else if (event.target.id == 'add-step-form-submit'){
        const button = document.getElementById('add-step-form-button');
        enableButton(button);
    }
})

function removeForm(form) {
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



// function addNewForm(event) {
//     const regex = new RegExp('__prefix__', 'g');
//     if (event) {
//         event.preventDefault();
//         if (event.target.id == 'add-ingredient') {
//             const currentIngredientForms = document.getElementsByClassName('ingredient-form-container');
//             const currentIngredientCount = currentIngredientForms.length;
//             const ingredientTotalForms = document.getElementById('ingredient-management-form').firstElementChild;
//             const ingredientFormList = document.getElementById('ingredient-form-list');
//             const emptyIngredientForm = document.getElementById('empty-ingredient-form').cloneNode(true);
//             emptyIngredientForm.setAttribute('class', 'flex ingredient-form-container mt-2');
//             emptyIngredientForm.setAttribute('id', `form-${currentIngredientCount}`);
//             emptyIngredientForm.innerHTML = emptyIngredientForm.innerHTML.replace(regex, currentIngredientCount);
//             ingredientTotalForms.setAttribute('value', currentIngredientCount + 1);
//             ingredientFormList.append(emptyIngredientForm)
            
//             console.log('it was the ingredient button')
//         } else if (event.target.id == 'add-step') {
//             const currentStepForms = document.getElementsByClassName('step-form-container');
//             const currentStepCount = currentStepForms.length
//             const stepTotalForms = document.getElementById('step-management-form').firstElementChild;
//             const stepFormList = document.getElementById('step-form-list');
//             const emptyStepForm = document.getElementById('empty-step-form').cloneNode(true);
//             emptyStepForm.setAttribute('class', 'flex step-form-container mt-2');
//             emptyStepForm.setAttribute('id', `form-${currentStepCount}`);
//             emptyStepForm.innerHTML = emptyStepForm.innerHTML.replace(regex, currentStepCount);
//             stepTotalForms.setAttribute('value', currentStepCount + 1);
//             stepFormList.append(emptyStepForm)

//             console.log('it was the step button')
//         }

//     }
// }

// message alert box 
// let alertWrapper = document.querySelector('.alert');
// let alertClose = document.querySelector('.alert__close');

// if (alertWrapper) {
//     alertClose.addEventListener('click', ()=> {
//         alertWrapper.style.display = 'none';
//     })
// }