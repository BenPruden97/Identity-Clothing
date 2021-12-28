/* 

    Core logic/payment flow taken from here:
    https://stripe.com/docs/js/elements_object/update

    CSS taken from Boutique Ado walkthrough project and
    updated to match my project styling

*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();
var style = {
    base: {
        color: '#152238',
        fontFamily: '"Cabin", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#152238',
            iconColor: '#152238',
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');