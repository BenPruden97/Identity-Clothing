/* 

    Core logic/payment flow taken from here:
    https://stripe.com/docs/js/elements_object/update

    CSS taken from Boutique Ado walkthrough project and
    updated to match my project styling

*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
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

// Handle realtime validation errors on the card element

card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span>
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
            `
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
})

// Handle form submit

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddletoken': csrfToken,
        'client_secret': clientSecret,
        'saveInfo': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form_full_name.value),
                    email: $.trim(form_email.value),
                    phone: $.trim(form_phone_number.value),
                    address: {
                        line1: $.trim(form_street_address1.value),
                        line2: $.trim(form_street_address2.value),
                        city: $.trim(form_town_or_city.value),
                        country: $.trim(form_country.value),
                        county: $.trim(form_county.value),
                    }
    
                }
            },
            shipping: {
                name: $.trim(form_full_name.value),
                phone: $.trim(form_phone_number.value),
                address: {
                    line1: $.trim(form_street_address1.value),
                    line2: $.trim(form_street_address2.value),
                    city: $.trim(form_town_or_city.value),
                    country: $.trim(form_country.value),
                    postcode: $.trim(form_postcode.value),
                    county: $.trim(form_county.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span>
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>
                `;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        location.reload();
    })
});