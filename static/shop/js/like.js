$(document).ready(function(){
    $("#like").click(function(){
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
                if (that.hasClass('fa fa-heart')) {
                    that.removeClass('fa fa-heart').addClass('ti-heart');
                    that.attr("title","Add To Wishlist");
                } else if (that.hasClass('ti-heart')) {
                    that.removeClass('ti-heart').addClass('fa fa-heart');
                    that.attr("title","Remove From Wishlist");
                }
            },
            error: function () {
                alert("Please login");
            }

        });
    });
});
