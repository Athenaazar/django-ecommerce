(function($) {
    "use strict";
     $(document).on('ready', function() {

    /*==================================
         Product page Quantity Counter
     ===================================*/
    $('.qty-box .quantity-right-plus').on('click', function () {
        var $qty = $('.qty-box .input-number');
        var currentVal = parseInt($qty.val(), 10);
        if (!isNaN(currentVal)) {
            $qty.val(currentVal + 1);
        }
    });
    $('.qty-box .quantity-left-minus').on('click', function () {
        var $qty = $('.qty-box .input-number');
        var currentVal = parseInt($qty.val(), 10);
        if (!isNaN(currentVal) && currentVal > 1) {
            $qty.val(currentVal - 1);
        }
    });
    $("#cart_update").click(function(){
        var attr_id = $(this).attr('attr_id')
        var action_url = $(this).attr('action_url')
        var that = $(this)

        $.ajax({
            url: action_url,
            type: "POST",
            data: {'attr_id': attr_id },
            headers: { "X-CSRFToken": $.cookie("csrftoken") },
            success: function (result) {
                console.log("Success");
            },
            error: function () {
                alert("Please login");
            }

        });
    });

});
})(jQuery);
