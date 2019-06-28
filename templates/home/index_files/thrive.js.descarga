jQuery(document).ready(function($){
	"use strict";

	$('#header-style-2-search-toggle').on('click', function(e){
		e.preventDefault();
		$('#hs-2-form-section').toggleClass('active');
	});
	
	$('textarea').autogrow({
		animate: false
	}).focus( function(){
		// Fix the bug which causes the textarea to return to
		// its original size when focus out and focus in
        $( this ).stop().slideDown();
    });

	$('#bp-menu-notifications-dropdown').click(function(e){
		e.preventDefault();
		$('.bp-thrive-dropdown-menu').toggleClass('active');
	});

	// fix all duplicate tags
	var duplicateChk = {};

	$('#dashboard-widgets').imagesLoaded( function(){
		$('#dashboard-widgets').masonry({
			itemSelector: '.widget',
		});
	});


	var $ld_courses_wrappers = $(".thrive-ld-courses-wrapper");

	$.each( $ld_courses_wrappers, function(){

		// Fetch all the children element inside the main wrapper added in filter
		// using add_filter('ld_course_list', 'thrive_fix_ld_container_issue') in extras.php.
		var $categorized_courses = $(this).children('.thrive-ld-course');

			// Wrap all the inner childs so that we could
			// assign a masonry object to each of them
			$categorized_courses.wrapAll("<div class='thrive-ld-courses-category-wrapper'>");

			// Assign the container to variable that we will be used to initiate masonry later.
			var $categorized_courses_wrap = $('.thrive-ld-courses-category-wrapper');

			// Finally, initiate a masonry object.
			$.each( $categorized_courses_wrap, function(){

				var that = $(this);

				that.imagesLoaded( function() {
					setInterval(function(){
						that.masonry({
							itemSelector: '.thrive-ld-course'
						});
					}, 500);
				});
			});
		return;

	});

	/**
	 * Support Gears
	 */
	 if ( $('.gears-carousel-standard').length >= 1 ) {

	 	var $thrive_carousel_standard = $('.gears-carousel-standard');

	 	$.each( $thrive_carousel_standard, function() {

	 		var __this = $(this);
	 		var max_slides  = (__this.attr('data-max-slides') !== undefined && __this.attr('data-max-slides').length >= 1) ? __this.attr('data-max-slides') : 7;
	 		var min_slides  = (__this.attr('data-min-slides') !== undefined && __this.attr('data-min-slides').length >= 1) ? __this.attr('data-min-slides') : 1;
	 		var slide_width = (__this.attr('data-item-width') !== undefined && __this.attr('data-item-width').length >= 1) ? __this.attr('data-item-width') : 85;

	 		var prop = {
	 			minSlides: parseInt(min_slides),
	 			maxSlides: parseInt(max_slides),
	 			slideWidth: parseInt(slide_width),
	 			nextText: '<i class="material-icons">keyboard_arrow_right</i>',
	 			prevText: '<i class="material-icons">keyboard_arrow_left</i>',
	 			pager: false,
	 			moveSlides: 3,
	 			slideMargin: 20
	 		};

	 		__this.bxSlider(prop);

	 		$('.gears-carousel-standard').css({
	 			'opacity': '1'
	 		});
	 	});

	 	//return;
	}

	$('#page-sidebar-toggle').click(function(e){
		e.preventDefault();
		$('#thrive-global-wrapper').toggleClass('toggled');
	});

	$('#toggle-add').click(function(e){
		e.preventDefault();
		$('#thrive-global-wrapper').toggleClass('toggled');
	});

	$('#item-header-navigation-button').on('click', function(){
		$('#item-nav').toggleClass('active');
	});

	// Thrive Wisechat Support.
	if ( $('#thrive-wisechat-support-close-btn') ) {

		$('#thrive-wisechat-support-close-btn i.material-icons').on( 'click', function() {
			$('#thrive-wisechat-support').addClass('inactive');
		});

		$('#thrive-chat-label').on('click', function(){
			$('#thrive-wisechat-support').removeClass('inactive');
		});
	}

	// Side Navigation
	$.each( $('#page-sidebar-menu li.menu-item-has-children > a'), function(){
		$(this).append('<span class="toggle material-icons">arrow_drop_down</span>');
	});

	var $sidenav_toggle = $('#page-sidebar-menu li.menu-item-has-children > a > .toggle');

		$sidenav_toggle.click(function(e){

			e.preventDefault();

			var $toggle = $( this );

			// Change icon.
			if ( $toggle.text().trim() === 'arrow_drop_down' )
			{

				$toggle.text('arrow_drop_up');

			} else {

				$toggle.text('arrow_drop_down');

			}

			// Toggle Menu.
			var $sub_menu = $( '> .sub-menu', $(this).parent().parent() );

				if ( $sub_menu.hasClass('active') ) {
					$sub_menu.removeClass('active');
				} else {
					$( $sub_menu ).addClass('active');
				}
		});

	/**
	 * Fix Dashboard Issue
	 */
	$('#toggle-add').on('click', function(e){
        dunhakdis_thrive_fix_masonry_issue(e);
    });

    $('#sidenav-toggle').on('click', function(e){
		// redraw slider
		if ( typeof revapi1 != 'undefined' ) {
			setTimeout(function(){
				revapi1.revredraw();
			}, 1500);

		}
        dunhakdis_thrive_fix_masonry_issue(e);
    });

	var dunhakdis_thrive_fix_masonry_issue = function(e) {
        e.preventDefault();
        setTimeout(function(){
            $('#dashboard-widgets').imagesLoaded( function(){
                $('#dashboard-widgets').masonry({
                    itemSelector: '.widget',
                });
            });
        }, 500);
    }

		/**
		 * Thrive Register
		 */
		 $('.thrive-register-fields-xprofile input').on('focus', function(){
			 $(this).parent().addClass('active');
			 $(this).parent().find('>label').addClass('primary');
		 }).on('blur',function(){
			 if ( $(this).val().length == 0 ) {
			 	$(this).parent().removeClass('active');
			 }
			 	$(this).parent().find('>label').removeClass('primary');
		 });

		 $(document).on('change', '.thrive-register-fields-xprofile input', function() {
			 $(this).parent().addClass('active');
  		   	 $(this).parent().find('>label').addClass('primary');
		 });

		 $(window).load(function(){
			 $.each( $('.thrive-register-fields-xprofile input'), function(){
				 if ( $(this).val().length !== 0 ) {
				 	$(this).parent().addClass('active');
				 }
			 });
		 });

    if ($('.entry-content').find('.wcContainer').length != 0) {
        $('#thrive-wisechat-support').addClass('has-wise-chat');
    } else {
        $('#thrive-wisechat-support').removeClass('has-wise-chat');
    }

    if ($('#thrive-global-wrapper').find('#thrive-wisechat-support.fb-mode-enabled').length != 0) {
        var device_width = $( window ).width();

        if ( device_width <= 768 ) {
            $('#thrive-wisechat-support.fb-mode-enabled .wcContainer > .wcWindowTitle:first-of-type').addClass('inactive');
        }

        $('#thrive-wisechat-support.fb-mode-enabled .wcContainer > .wcWindowTitle:first-of-type .wcWindowTitleMinMaxLink:not(.wcWindowTitleMinimized)').click(function(e){
            e.preventDefault();
            var $button = $( this );
            var device_width = $( window ).width();
            if ( device_width <= 768 ) {
                if ( $button.parent().hasClass('inactive') ) {
                    $button.parent().removeClass('inactive');
                } else {
                    $button.parent().addClass('inactive');
                }
            }
        });
    }

    var documentWidth = $(document).width();

    $(".sidenav-toggle-control").click( function(e) {
        e.preventDefault();
        $("#document-wrapper").toggleClass("active");
        $('#site-footer-section').toggleClass("active");

    	// check if the document is active or not.
    	// clean any cookies.
    	//$.removeCookie('thrive-layout', { path: '/' });
    	Cookies.remove('thrive-layout');
    	// disable on mobile
        if ( documentWidth <= 768 ) { return; }

    	if ( $('#document-wrapper').hasClass('active')  ) {
    		// Set the cookie to active when document is not.
    		// $.cookie('thrive-layout', '1-column', {path: '/', expires: 1 });
    		Cookies.set('thrive-layout', '1-column', { expires: 7 });

    	} else {
    		// $.cookie('thrive-layout', '2-columns', {path: '/', expires: 1 });
    		Cookies.set('thrive-layout', '2-column', { expires: 7 });
    	}
    	// Trigger the resize event.
    	setTimeout( function(){
    		$(window).resize();
    	}, 265 );
    	
    	return;
    });

    // remove sidenav active state when in mobile
    if ( documentWidth <= 768 ) {
		$("#document-wrapper").removeClass("active");
        $('#site-footer-section').removeClass("active");
    }

    //woocommerce cross-sells
    $('.cross-sells ul.products').bxSlider({
    	pager: false,
    	mode: 'fade',
    });

    // Back to top functionality.
    $('#thrive-scroll-to-top > a').on("click", function(e){
    	e.preventDefault();
		$("html, body").animate({scrollTop: 0}, 200);
	});

    var backToTop = __thrive_debounce(function(){
    	var top = $(document).scrollTop();
			if ( top > 300 ) {
				$('#thrive-scroll-to-top > a').addClass('active');
			} else {
				$('#thrive-scroll-to-top > a').removeClass('active');
			}
    }, 250);

	$(window).on('scroll', backToTop);

    // BuddyPress Widget Ellipsis.
    var bp_ellipsis_text = $( '.widget.buddypress #friends-list > li .item-title > a, .widget.buddypress #groups-list > li .item-title > a, .widget.buddypress #members-list > li .item-title > a' );

    bp_ellipsis_text.ellipsis({
        lines: 2,
        ellipClass: 'ellip',
        responsive: true
    });

});

/**
 * Natives
 */

/*
 * Debouncing function to prevent unnecessary
 * firing of an events. Taken from underscore.js
 *
 * @return void
 */
function __thrive_debounce(func, wait, immediate) {
	var timeout;
	return function() {
		var context = this, args = arguments;
		var later = function() {
			timeout = null;
			if (!immediate) func.apply(context, args);
		};
		var callNow = immediate && !timeout;
		clearTimeout(timeout);
		timeout = setTimeout(later, wait);
		if (callNow) func.apply(context, args);
	};
};

(function(){
		/**
		 * User Navigation Controls
		 */
		var userNotificationControls = document.getElementsByClassName('user-notification-action');
		if ( userNotificationControls ) {
			for ( var i = 0; i <= userNotificationControls.length; i++ ) {
				var userNotificationControl = userNotificationControls[i];
					if ( userNotificationControl && userNotificationControl.nodeType == 1 ) {
						userNotificationControl.addEventListener('click', function(e){
							if( ! jQuery(e.target).parents('.user-notifications').length > 0) {
							   e.preventDefault();
							}
							if (this.classList.contains('active')) {
								this.classList.remove('active');
							} else {
								this.classList.add('active');
							}
						});
					}
			}
		}


		function resizeContentOffset()
		{
			// Disable if blank page template
			var isBlank = document.getElementById('blank-template-content');
			if ( isBlank ) {
				return;
			}
			var w=window,d=document,e=d.documentElement,g=d.getElementsByTagName('body')[0],x=w.innerWidth||e.clientWidth||g.clientWidth,y=w.innerHeight||e.clientHeight||g.clientHeight;
			
			/*
			var referenceNavigation = document.querySelector('.reference-navigation');

			if ( referenceNavigation ) {
				referenceNavigation.innerHTML = document.querySelector('.reference-navigation').innerHTML.trim();
			}*/

			var masthead = document.getElementById('masthead');
			var footer = document.getElementById('thrive_footer');
			var content = document.getElementById('content');
			var footerWidget = document.getElementById('thrive_footer_widget');
			var wpAdminBar = document.getElementById('wpadminbar');
			var wpAdminBarHeight = 0;

			if ( wpAdminBar ) {
				wpAdminBarHeight = wpAdminBar.offsetHeight;
			}

			if ( footerWidget ) {
				content.style.minHeight = y - ( (masthead.offsetHeight + footer.offsetHeight + footerWidget.offsetHeight) + wpAdminBarHeight ) + "px";
			} else {
				content.style.minHeight = y - ( (masthead.offsetHeight + footer.offsetHeight) + wpAdminBarHeight ) + "px";
			}

			return;

		}

		/**
		 * Fix Mobile View on render
		 */
		function reCalculateThemeHeader() {

			var wpAdminBar = document.getElementById('wpadminbar');
			var thriveBar = document.getElementById('thrive-bar');

			// Disable if blank page template
			var isBlank = document.getElementById('blank-template-content');
			
			if ( isBlank ) {
				return;
			}

			if ( ! thriveBar ) { return }

			var doc = document.documentElement;
			var top = (window.pageYOffset || doc.scrollTop)  - (doc.clientTop || 0);

			var adminBarheight = 0;

			if ( wpAdminBar ) {
				adminBarheight = wpAdminBar.clientHeight;
			}

			var sidebar = document.getElementById('sidebar-wrap');
			var gutterHeight = thriveBar.clientHeight + adminBarheight;

			thriveBar.style.top = adminBarheight;

			var finalTop = gutterHeight - top;

			if ( finalTop >= 0 ) {
				if ( window.getComputedStyle(thriveBar).position != 'fixed' ) {
					sidebar.style.top = gutterHeight - top + 'px';
				} else {
					sidebar.style.top = gutterHeight + 'px';
				}
			} else {
				if ( window.getComputedStyle(thriveBar).position == 'fixed' ) {
					sidebar.style.top = gutterHeight + 'px';
				} else {
					sidebar.style.top = 0 + 'px';
				}
			}
			return;
		}

		document.addEventListener("DOMContentLoaded", function() {

			reCalculateThemeHeader();

			// footer
			resizeContentOffset();

		});

		var resizeContentOffsetDebounce 	= __thrive_debounce( resizeContentOffset, 100 );
		var reCalculateThemeHeaderDebounce 	= __thrive_debounce( reCalculateThemeHeader, 250 );

		window.addEventListener('scroll', resizeContentOffsetDebounce);

		window.addEventListener('resize', reCalculateThemeHeaderDebounce);

		// use jQuery scroll event, fires on mobile.
		jQuery(window).on('scroll', reCalculateThemeHeaderDebounce);

})();

/**
 * Sharer Links
 */
jQuery(document).ready(function($){

	// Sharer
	$('.facebook-share a').click(function(e){
        e.preventDefault();
        ThriveSharerPopup( thrive_nouveau_sharer_js_vars.fb_sharer_url );
    });
    // TWitter
    $('.twitter-share a').click(function(e){
        e.preventDefault();
        ThriveSharerPopup( thrive_nouveau_sharer_js_vars.tw_sharer_url );
    });

     // LinkedIn
    $('.linkedin-share a').click(function(e){
        e.preventDefault();
        ThriveSharerPopup( thrive_nouveau_sharer_js_vars.li_sharer_url );
    });

    //Google+
    $('.google-plus-share a').click(function(e){
        e.preventDefault();
        ThriveSharerPopup( thrive_nouveau_sharer_js_vars.gp_sharer_url );
    });

    // Redit
    $('.reddit-share a').click(function(e){
        e.preventDefault();
        ThriveSharerPopup( thrive_nouveau_sharer_js_vars.rd_sharer_url );
    });

     // Whatsapp
    $('.whatsapp-share a').click(function(e){
        e.preventDefault();
        ThriveSharerPopup( thrive_nouveau_sharer_js_vars.whatsapp_sharer_url );
    });

     function ThriveSharerPopup( url ) {

        var winTop = (screen.height / 2) - (520 / 2);
        var winLeft = (screen.width / 2) - (350 / 2);

        window.open( url, 'sharer', 'top='+winTop + ',left=' + winLeft
            + ',toolbar=0,status=0,width=520,height=350'
        );
    }
    $('#whats-new').on('focus', function(){
    	
	 	if ( $('#whats-new-post-in-box').length == 0 ) {
	    	$('#whats-new-submit').css('width', '100%');
	    }
	    // Fix RTMedia mess...
	    $('#rtmedia-action-update').css('top', '-80px');
    });
    $('body').on('focusout', '#whats-new', function(){
    	setTimeout(function(){
    		// Fix Another RTMedia mess...
	    	if( $('#whats-new-submit').length == 0 ){

			    $('#rtmedia-action-update').css('top', '');
	    		$('#bp-nouveau-activity-form').removeClass('active');
	    	} 
    	}, 100);
    
    });

    // Magnific Popup.
    if ( typeof $.magnificPopup === 'object' ) {
	    $('.magnific-popup').magnificPopup({ type: 'image'});
	}

	$('#bbp_search').attr('placeholder', 'Search Forums')
   
   	// Mobile Menu
   	var thriveHideElement = function( element ) {
   		element.removeClass('active');
   		return;
   	}
   	var $parent_menus = $('#main-menu-mobile-wrap ul.menu li.menu-item-has-children');
	$.each( $parent_menus, function () {
		$(this).find(' > a').after('<span class="thrive-mobile-toggle-submenu"><i class="material-icons">arrow_drop_down</i></span');
	});
	$('.thrive-mobile-toggle-submenu').on('click', function(e){
		e.preventDefault();
		var arrow = $(this).find('.material-icons').text();
		if ( 'arrow_drop_down' === arrow ) {
			$(this).find('.material-icons').text('arrow_drop_up');
		} else {
			$(this).find('.material-icons').text('arrow_drop_down');
		}
		$(this).parent().find('> ul.sub-menu').toggle();
	});

	// Show menu.
	$('.main-menu-mobile-show-button').on('click', function(){
		$('#main-menu-mobile-wrap').addClass('active');
	});
	// Hide menu when clicked on the shaded area.
	$('#main-menu-mobile-wrap').on('click', function(){
		thriveHideElement( $(this) );
	});
	// Hide menu on escape.
	$(document).keyup(function(e) {
		if (e.keyCode === 27)  {
			thriveHideElement( $('#main-menu-mobile-wrap') );
		}
	});
	$(".main-menu-mobile-wrap__inner-wrap").on('click',function(event){
	    event.stopPropagation();
	}); 

});
// End Theme JS.