const firstNameInput = document.getElementById('first-name');
const lastNameInput = document.getElementById('last-name');
const emailInput = document.getElementById('email-input');
const passwordInput = document.getElementById('password-input');
const confirmPasswordInput = document.getElementById('confirm-password-input');
const submitButton = document.getElementById('submit-form');
const emailError = document.getElementById('email-error')
const passwordMatchError = document.getElementById('password-match-error')

submitButton.addEventListener('click', function () {
    sendPost();
});

firstNameInput.addEventListener('input', function () {
    emailError.classList.add('hidden');

    if (firstNameInput.value.length > 0 &&
        lastNameInput.value.length > 0 &&
        emailInput.value.length > 0 &&
        passwordInput.value.length > 0 &&
        confirmPasswordInput.value.length > 0 &&
        passwordInput.value === confirmPasswordInput.value &&
        validateEmail(emailInput.value)
    ) {
        submitButton.disabled = false;
    }
    else {
        submitButton.disabled = true;
    }

    if (passwordInput.value !== confirmPasswordInput.value &&
        !passwordInput.value.startsWith(confirmPasswordInput.value)
    ) {
        passwordMatchError.classList.remove('hidden');
    }
    else {
        passwordMatchError.classList.add('hidden')
    }
});

lastNameInput.addEventListener('input', function () {
    emailError.classList.add('hidden');

    if (firstNameInput.value.length > 0 &&
        lastNameInput.value.length > 0 &&
        emailInput.value.length > 0 &&
        passwordInput.value.length > 0 &&
        confirmPasswordInput.value.length > 0 &&
        passwordInput.value === confirmPasswordInput.value &&
        validateEmail(emailInput.value)
    ) {
        submitButton.disabled = false;
    }
    else {
        submitButton.disabled = true;
    }

    if (passwordInput.value !== confirmPasswordInput.value &&
        !passwordInput.value.startsWith(confirmPasswordInput.value)
    ) {
        passwordMatchError.classList.remove('hidden');
    }
    else {
        passwordMatchError.classList.add('hidden')
    }
});

emailInput.addEventListener('input', function () {
    emailError.classList.add('hidden');

    if (firstNameInput.value.length > 0 &&
        lastNameInput.value.length > 0 &&
        emailInput.value.length > 0 &&
        passwordInput.value.length > 0 &&
        confirmPasswordInput.value.length > 0 &&
        passwordInput.value === confirmPasswordInput.value &&
        validateEmail(emailInput.value)
    ) {
        submitButton.disabled = false;
    }
    else {
        submitButton.disabled = true;
    }

    if (passwordInput.value !== confirmPasswordInput.value &&
        !passwordInput.value.startsWith(confirmPasswordInput.value)
    ) {
        passwordMatchError.classList.remove('hidden');
    }
    else {
        passwordMatchError.classList.add('hidden')
    }
});

passwordInput.addEventListener('input', function () {
    emailError.classList.add('hidden');

    if (firstNameInput.value.length > 0 &&
        lastNameInput.value.length > 0 &&
        emailInput.value.length > 0 &&
        passwordInput.value.length > 0 &&
        confirmPasswordInput.value.length > 0 &&
        passwordInput.value === confirmPasswordInput.value &&
        validateEmail(emailInput.value)
    ) {
        submitButton.disabled = false;
    }
    else {
        submitButton.disabled = true;
    }

    if (passwordInput.value !== confirmPasswordInput.value &&
        !passwordInput.value.startsWith(confirmPasswordInput.value)
    ) {
        passwordMatchError.classList.remove('hidden');
    }
    else {
        passwordMatchError.classList.add('hidden')
    }
});

confirmPasswordInput.addEventListener('input', function () {
    emailError.classList.add('hidden');

    if (firstNameInput.value.length > 0 &&
        lastNameInput.value.length > 0 &&
        emailInput.value.length > 0 &&
        passwordInput.value.length > 0 &&
        confirmPasswordInput.value.length > 0 &&
        passwordInput.value === confirmPasswordInput.value &&
        validateEmail(emailInput.value)
    ) {
        submitButton.disabled = false;
    }
    else {
        submitButton.disabled = true;
    }

    if (passwordInput.value !== confirmPasswordInput.value &&
        !passwordInput.value.startsWith(confirmPasswordInput.value)
    ) {
        passwordMatchError.classList.remove('hidden');
    }
    else {
        passwordMatchError.classList.add('hidden')
    }
});

firstNameInput.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        sendPost();
    }
});

lastNameInput.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        sendPost();
    }
});

emailInput.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        sendPost();
    }
});

passwordInput.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        sendPost();
    }
});

confirmPasswordInput.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        sendPost();
    }
});

function validateEmail(email) {
    return String(email)
        .toLowerCase()
        .match(
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        );
};

function sendPost() {
    submitButton.disabled = true;
    submitButton.innerText = 'Signing up...'
    var firstName = firstNameInput.value;
    var lastName = lastNameInput.value;
    var email = emailInput.value;
    var password = passwordInput.value;

    fetch('/signup/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'first_name': firstName,
            'last_name': lastName,
            'email': email,
            'password': password,
        })
    })
        .then(response => {
            if (response.status === 200) {
                window.location.href = response.url;
            }
            else if (response.status === 401) {
                emailError.classList.remove('hidden')
                submitButton.innerText = 'Sign Up'
            }
        })
}