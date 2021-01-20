// Copy To Clipboard AJAX

$(".copy-link").click(function(evt) {
    evt.preventDefault();
	var link = $(this).attr("href");
	var host = window.location.origin;
	link = host + link;
	$.get("/copy_link", {"link": link}, function (response) {
        if (response['done'] == true) {
            $(".copied").fadeIn("fast").delay(1000).fadeOut();
        }
    });
});