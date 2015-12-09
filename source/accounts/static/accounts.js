// accounts/static/accounts.js


var initialize = function (navigator, user, token, urls) {
    console.log(navigator);
    $('#id_login').on('click', function () {
        navigator.id.request();
    });

    navigator.id.watch({
        loggedInUser: user,
        onlogin: function (assertion) {
            $.post(
                urls.login,
                { assertion: assertion, csrfmiddlewaretoken: token }
            )
                .done(function () { window.location.reload(); })
                .fail(function () { navigator.id.logout(); });
        },
        onlogout: function () {}
    });
};

window.Tango = {
    Accounts: {
        initialize: initialize
    }
};

