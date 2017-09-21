jQuery(document).ready(function($){
	//get current path and find target link
	var path=window.location.pathname.split("/").pop();

	var target= $('nav a[href="'+path+'"]');
	//Add active class to target link
	target.addClass('active');
});