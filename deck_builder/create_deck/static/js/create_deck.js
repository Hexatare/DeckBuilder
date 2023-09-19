const uploadTextInput = document.getElementById('upload-text-input');

uploadTextInput.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = this.scrollHeight + 'px';
});

const selectImage = document.getElementById('select-image-upload');
const selectText = document.getElementById('select-text-input');
const uploadImageWrapper = document.getElementById('upload-image-wrapper');
const uploadTextWrapper = document.getElementById('upload-text-wrapper');
const imageProgress = document.getElementById('image-progress');
const imageTextResult = document.getElementById('image-text-result');
const imageTextResultSection = document.getElementById('image-text-result-section');

selectImage.addEventListener('click', function () {
    selectText.classList.remove('selected');
    selectImage.classList.add('selected');

    uploadTextWrapper.classList.add('hidden');
    uploadImageWrapper.classList.remove('hidden');
});

selectText.addEventListener('click', function () {
    selectText.classList.add('selected');
    selectImage.classList.remove('selected');

    uploadTextWrapper.classList.remove('hidden');
    uploadImageWrapper.classList.add('hidden');
});

const imageInput = document.getElementById('image-input');
const imageInputLabel = document.getElementById('image-input-label');

imageInput.addEventListener('change', function () {
    sendImage();
});

function sendImage() {
    const uploadedFile = imageInput.files[0];
    imageInputLabel.classList.add('hidden');
    imageProgress.classList.remove('hidden');

    if (uploadedFile) {
        const formData = new FormData();
        formData.append('image', uploadedFile);

        fetch('/create/upload/image', {
            method: 'POST',
            body: formData,
        })
            .then(response => response.json())
            .then(data => {
                imageProgress.classList.add('hidden');
                imageTextResultSection.classList.remove('hidden');
                imageTextResult.value = data['text']
                imageTextResult.style.height = imageTextResult.scrollHeight + 'px';
            });
    }
}

imageInputLabel.addEventListener('dragenter', function (event) {
    event.preventDefault();
    imageInputLabel.classList.add('active');
});

imageInputLabel.addEventListener('dragover', function (event) {
    event.preventDefault();
});

imageInputLabel.addEventListener('dragleave', function (event) {
    event.preventDefault();
    imageInputLabel.classList.remove('active');
});

imageInputLabel.addEventListener('drop', function (event) {
    event.preventDefault();
    imageInputLabel.classList.remove('active');
    sendImage();
});


const textInput = document.getElementById('upload-text-input');
const submitTextButton = document.getElementById('submit-text');
const buttonText = document.getElementById('submit-button-text');
const loadingIcon = document.getElementById('loading-icon');
const submitImageTextButton = document.getElementById('submit-image-text');
const submitImageTextButtonText = document.getElementById('submit-button-image-text');
const loadingIconImageText = document.getElementById('loading-icon-image-text');

textInput.addEventListener('input', function () {
    if (textInput.value.length > 0) {
        submitTextButton.disabled = false;
    } else {
        submitTextButton.disabled = true;
    }
});

submitTextButton.addEventListener('click', function () {
    submitTextButton.disabled = true;
    buttonText.classList.add('hidden');
    loadingIcon.classList.remove('hidden');
    const enteredText = textInput.value;

    fetch('/create/upload/text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            text: enteredText,
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data['success']);
        });
});

imageTextResult.addEventListener('input', function () {
    if (imageTextResult.value.length > 0 && !submitImageTextButton.classList.contains('loading')) {
        submitImageTextButton.disabled = false;
    } else {
        submitImageTextButton.disabled = true;
    }
});

submitImageTextButton.addEventListener('click', function () {
    submitImageTextButton.disabled = true;
    submitImageTextButton.classList.add('loading');
    submitImageTextButtonText.classList.add('hidden');
    loadingIconImageText.classList.remove('hidden');
    const enteredText = imageTextResult.value;

    fetch('/create/upload/text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            text: enteredText,
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data['success']);
        });
});