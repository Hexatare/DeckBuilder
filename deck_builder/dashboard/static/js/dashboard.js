const textInput = document.getElementById('text-input');
const submitTextButton = document.getElementById('submit-text');


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