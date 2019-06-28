/**
 * navigation.js
 *
 * Handles navigation menu behaviour
 */

jQuery( document ).ready( function($) {

	'use strict';

    var device_width = $( window ).width();

	// 1 Column layout search.
	$( '#thrive-responsive-search' ).click( function(e){
		e.preventDefault();
			$('#thrive-secondary-menu').toggleClass( 'hide' );
	});

	// Mobile Navigation Event Manager
	$('#mobile-menu a').click(function(e){

		e.preventDefault();

		$('#site-navigation-container').removeClass('inactive-menu');
		$('#site-navigation-container').addClass('active-menu');

		$('#site-navigation').removeClass('inactive');
		$('#site-navigation').addClass('active');

		return;

	});

	// Mobile Search
	$( '#thrive-mobile-search-btn' ).click( function(e){
		e.preventDefault();
			$( '#thrive-mobile-search-btn' ).toggleClass( 'active' );
			$( '#thrive-secondary-menu-search' ).toggleClass( 'active' );
	});


	$('#desktop-menu').prepend("<div id='mobile-close-btn'></div>");

	$('#mobile-close-btn').on('click', function(){
		$('#site-navigation').removeClass('active');
		$('#site-navigation').addClass('inactive');
			$('#site-navigation-container').addClass('inactive-menu');
			$('#site-navigation-container').removeClass('active-menu');
	});

		$(document).mouseup(function(e){
			var container = $("#site-navigation");
		    if (container.is(e.target) // if the target of the click isn't the container...
		        && container.has(e.target).length === 0) // ... nor a descendant of the container
		    {
		      	$('#site-navigation').removeClass('active');
				$('#site-navigation').addClass('inactive');
				$('#site-navigation-container').addClass('inactive-menu');
				$('#site-navigation-container').removeClass('active-menu');
		    }
		});

		$(document).keyup(function(e) {
		  	if (e.keyCode == 27) {
		  		// remove menu
		  		$('#site-navigation').removeClass('active');
				$('#site-navigation').addClass('inactive');
				$('#site-navigation-container').addClass('inactive-menu');
				$('#site-navigation-container').removeClass('active-menu');
		  	}   // escape key maps to keycode `27`
		});

	// Sidenav Navigation Event Manager
	$('#sidenav-menu').click(function(e){

		e.preventDefault();

		$('#page-sidenav').addClass('active').css({
			height: jQuery(document).height() + 'px'
		});


	});

	$(document).mouseup(function(e){
		var container = $("#page-sidenav");
	    if (container.is(e.target) // if the target of the click isn't the container...
	        && container.has(e.target).length === 0) // ... nor a descendant of the container
	    {
	      	$('#page-sidenav').removeClass('active');
			$('#page-sidenav').addClass('inactive');

				$('#site-navigation-container').addClass('inactive-menu');
				$('#site-navigation-container').removeClass('active-menu');
	    }
	});

	$(document).keyup(function(e) {
	  	if (e.keyCode == 27) {
	  		// remove menu
	  		$('#page-sidenav').removeClass('active');
			$('#page-sidenav').addClass('inactive');
	  	}   // escape key maps to keycode `27`
	});

	nano_scroll();

	$( window ).resize( nano_scroll );

	function nano_scroll() {

		var gutter = 150;

		if ( $('#page-sidebar-user-logged-out').length >= 1 ) {
			gutter = 132.5;
		}

		$('#user-content-widget-sidenav').css({
			height: $(window).height() - gutter
		});

		$(".nano").nanoScroller();
	}

	bp_group_description_nano_scroll();

	function bp_group_description_nano_scroll() {

        var group_description = $( '.widget-area #meta-group-description .group-description' );
        var group_meta = $( '.widget-area #meta-group-description #meta-group-description-title' );
        var height = 300;
        var gutter = group_meta.height();

        if ( group_description.length >= 1 ) {
            group_description.addClass('nano');

            if ( $( '.group-description .nano-content' ).length <= 0 ) {
                group_description.wrapInner( "<div class='nano-content'></div>" );
            }
        }

		$('.widget-area #meta-group-description .group-description').css({
			height: height - gutter
		});

		$(".nano").nanoScroller();
	}


    // BuddyPress Mobile DropDown Profile Menu.
    var profile_nav_dropdown_btn = '<span class="profile-nav-dropdown-btn material-icons">keyboard_arrow_down</span>';

    if ( device_width <= 731 ) {
        $( '.single-screen-navs.main-navs > ul' ).prepend( profile_nav_dropdown_btn );
    }

    function resizeProfileDropDownOffset() {
        var resize_device_width = $( window ).width();

        if ( resize_device_width <= 731 ) {
            if ( ! $( '.profile-nav-dropdown-btn' ).length ) {
                $( '.single-screen-navs.main-navs > ul' ).prepend( profile_nav_dropdown_btn );
            }
        }
        if ( resize_device_width > 731 ) {
            $( '.profile-nav-dropdown-btn' ).remove();
        }
    }

    $( 'body' ).on( 'click', '.profile-nav-dropdown-btn', function(e){
		e.preventDefault();
        var dropdown_btn = $( '.profile-nav-dropdown-btn' );
        var dropdown_btn_parent = dropdown_btn.parent();

        dropdown_btn_parent.toggleClass( 'active' );
        if ( dropdown_btn_parent.hasClass( 'active' ) ) {
            dropdown_btn.text( 'keyboard_arrow_up' );
        } else {
            dropdown_btn.text( 'keyboard_arrow_down' );
        }
	});

    var resizeProfileDropDownOffsetDebounce 	= __thrive_debounce( resizeProfileDropDownOffset, 0 );
    window.addEventListener( "resize", resizeProfileDropDownOffsetDebounce );

});
