document.addEventListener("DOMContentLoaded", function() {
    let signupForm = document.getElementById('signup_form');

    if (signupForm){
        let firstNameInput = document.getElementById('first-name');

        firstNameInput.addEventListener('blur', function() {
            if (!firstNameInput.checkValidity()){
                firstNameInput.style.border = '2px solid rgba(255, 0, 0, .5)'
                console.log("Got here");
            }
        });

        firstNameInput.addEventListener('input', function() {
            if (firstNameInput.checkValidity()){
                firstNameInput.style.border = '2px solid rgba(255, 255, 255, .2)'
                console.log("Got here also");
            }
        });
        
        let password = document.getElementById('password');
        let confirm_password = document.getElementById('confirm_password');
        let message = document.querySelector(".password_msg");

        confirm_password.addEventListener('input', function(){
            if (password.value !== confirm_password.value) {
                message.innerHTML = 'Passwords do not match';
                confirm_password.setCustomValidity('Passwords do not match');
            } else {
                message.innerHTML = '';
                confirm_password.setCustomValidity('');
            }
        });

        document.getElementById('signup-form').addEventListener('submit', function(event){
            if (password.value !== confirm_password.value) {
                event.preventDefault();
            }
        });
    }

})