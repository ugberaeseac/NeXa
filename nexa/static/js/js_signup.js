document.addEventListener("DOMContentLoaded", function() {

    function input_check(input_id){
        let name = document.getElementById(input_id);

        console.log(name)
        console.log(name.checkValidity())
        
        name.addEventListener('blur', function() {
            if (!name.checkValidity()){
                name.style.border = '2px solid rgba(255, 0, 0, .5)'
                console.log(name.validationMessage);
                console.log(name.reportValidity());
            }
        });

        name.addEventListener('input', function() {
            if (name.checkValidity()){
                name.style.border = '2px solid rgba(0, 0, 255, .2)'
                console.log("Got here also");
            }
        });
    }

    let signupForm = document.getElementById('signup_form');

    if (signupForm){

        input_check('first-name');
        input_check('last-name');
        input_check('user-name');

        function emailValidator(){
            let emailCheck = document.getElementById('email');
            const emailValidate = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            emailCheck.addEventListener('blur', function(){
                if (!emailValidate.test(emailCheck.value)){
                    emailCheck.setCustomValidity('Invalid email format')
                    emailCheck.reportValidity();
                    emailCheck.style.border = '2px solid rgba(255, 0, 0, .5)';
                    console.log("Invalid email format");
                    return (false);
                }
                else{
                    emailCheck.setCustomValidity('');
                    emailCheck.style.border = '2px solid rgba(0, 0, 255, .2)';
                    console.log("valid email format");
                    return (true);
                }
            });
        }

        emailValidator();
        
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
            else if (!emailValidator()){
                event.preventDefault();
            }
            else{
                console.log('Form submitted successfully!')
            }
        });
    }


})