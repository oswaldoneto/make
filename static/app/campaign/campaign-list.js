$(document).ready(function() {

    $(".ui .button").click(function(){
        console.info('button pressed!')
        redirect('/campaign/create');
    });

	$("a[rel=uic_item_link]").click(function(){
		redirect(sprintf('/campaign/update/%s',$(this).attr('href')));
		return false;
	});

});


function redirect(url) {
    location = url;
}