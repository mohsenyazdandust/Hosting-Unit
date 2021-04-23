// LogIn Ajax
$("#login-form").submit(function (evt) {
    evt.preventDefault();
    $(".form-signin .alert").removeClass("alert-danger");
    $(".form-signin .alert").addClass("alert-warning");
    $(".form-signin .alert").text("لطفا صبر کنید...");
    $(".form-signin .alert").slideDown();
    $(".form-signin .btn").prop("disabled", true);
    var url = $(this).attr("action");
    var data = $(this).serialize();
    $.post(url, data, function (response) {
        if (response['validate'] == true) {
            window.location.replace("/done");
        } else {
            $(".form-signin .alert").removeClass("alert-warning");
            $(".form-signin .alert").addClass("alert-danger");
            $(".form-signin .alert").text("اطلاعات نادرست");
            $(".form-signin .btn").prop("disabled", false);
        }
    });
});