const textInput = document.getElementById('text-input');
const submitTextButton = document.getElementById('submit-text');

submitTextButton.addEventListener('click', function () {
    const enteredText = textInput.value;

    fetch('/upload/text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: {
            text: enteredText,
        }
    })
        .then(response => response.json())
        .then(data => {
            fileContents = data['file_contents'];

            console.log(fileContents);
        });
});


const pictureInput = document.getElementById('picture-input');

pictureInput.addEventListener('change', function () {
    const uploadedFile = pictureInput.files[0];

    if (uploadedFile) {
        const formData = new FormData();
        formData.append('image', uploadedFile);

        fetch('/upload/image', {
            method: 'POST',
            body: formData,
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);
            });
    }
});