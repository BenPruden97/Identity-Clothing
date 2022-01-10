/* ----- Email JS Contact Form Code ----- */

form = document.querySelector('#contact-form');

form.addEventListener("submit", function() {

    event.preventDefault();
    const target = event.target;

    const templateParams = {
        member_name: target.name.value,
        member_email: target.email.value,
        member_message: target.message.value
    };

    emailjs.send('gmail', 'identity_clothing', templateParams)
    .then(function(response) {

        swal({
            title: "Thank You!",
            text: "Your message was sent successfully",
            icon: "success",
            button: false,
            timer: 3500
        });

    }, function(error) {

        swal({
            title: "Unfortunately Your Message Was Not Sent!",
            text: "Please Try Again or Contact Us via our Contact Page!",
            icon: "error",
            button: false,
            timer: 3500
        });

    });

});