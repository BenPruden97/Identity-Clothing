// Add product review form

$('#addProductReviewForm').submit(function(e){
    $.ajax({
        data:$(this).serialize(),
        method:$(this).attr('method'),
        url:$(this).attr('action'),
        dataType:'json',
        success: function(res) {
            if (res.bool == true) {
                console.log("Success")
                $(".ajaxRes").html('Review has been added');
                form.reset();
            }
        }
    });
    e.preventDefault();
});
