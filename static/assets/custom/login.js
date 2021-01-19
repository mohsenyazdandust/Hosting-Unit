// LogIn Ajax
$("#login-form").submit(function (evt) {
    evt.preventDefault();
    $(".form-signin .alert").removeClass("alert-danger");
    $(".form-signin .alert").addClass("alert-warning");
    $(".form-signin .alert").text("Please Wait...");
    $(".form-signin .alert").slideDown();
    $(".form-signin .btn").prop("disabled", true);
    var url = $(this).attr("action");
    var data = $(this).serialize();
    $.post(url, data, function (response) {
        if (response['validate'] == true) {
            window.location.replace("/files");
        } else {
            $(".form-signin .alert").removeClass("alert-warning");
            $(".form-signin .alert").addClass("alert-danger");
            $(".form-signin .alert").text("Wrong Information! Please Try Again");
            $(".form-signin .btn").prop("disabled", false);
        }
    });
});