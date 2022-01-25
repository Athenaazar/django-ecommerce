(function($) {
    "use strict";
     $(document).on('ready', function() {	

		/*=======================
		  Home Slider JS
		=========================*/ 
		$('.home-slider').owlCarousel({
			items:1,
			autoplay:true,
			autoplayTimeout:5000,
			smartSpeed: 400,
			animateIn: 'fadeIn',
			animateOut: 'fadeOut',
			autoplayHoverPause:true,
			loop:true,
			nav:true,
			merge:true,
			dots:false,
			navText: ['<i class="ti-angle-left"></i>', '<i class="ti-angle-right"></i>'],
			responsive:{
				0: {
					items:1,
				},
				300: {
					items:1,
				},
				480: {
					items:2,
				},
				768: {
					items:3,
				},
				1170: {
					items:4,
				},
			}
		});
	});

    /*=======================
      Popular Slider JS
    =========================*/
    $('.popular-slider').owlCarousel({
        items:1,
        autoplay:true,
        autoplayTimeout:5000,
        smartSpeed: 400,
        animateIn: 'fadeIn',
        animateOut: 'fadeOut',
        autoplayHoverPause:true,
        loop:true,
        nav:true,
        merge:true,
        dots:false,
        navText: ['<i class="ti-angle-left"></i>', '<i class="ti-angle-right"></i>'],
        responsive:{
            0: {
                items:1,
            },
            300: {
                items:1,
            },
            480: {
                items:2,
            },
            768: {
                items:3,
            },
            1170: {
                items:4,
            },
        }
    });

    /*====================================
        Mobile Menu
    ======================================*/
    $('.menu').slicknav({
        prependTo:".mobile-nav",
        duration:300,
        animateIn: 'fadeIn',
        animateOut: 'fadeOut',
        closeOnClick:true,
    });

    /*====================================
      Sticky Header JS
    ======================================*/
    jQuery(window).on('scroll', function() {
        if ($(this).scrollTop() > 200) {
            $('.header').addClass("sticky");
        } else {
            $('.header').removeClass("sticky");
        }
    });
    /*=======================
      Search JS JS
    =========================*/
    $('.top-search a').on( "click", function(){
        $('.search-top').toggleClass('active');
    });

})(jQuery);
