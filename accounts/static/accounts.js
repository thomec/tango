// accounts/static/accounts.js


var initialize = function (navigator, user, token, urls) {
    console.log(navigator);
    $('#id_login').on('click', function () {
        navigator.id.request();
    });

    $('#id_logout').on('click', function () {
        navigator.id.logout();
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
        onlogout: function () {
            $.post(
                urls.logout,
                { csrfmiddlewaretoken: token }
            )
                .done(function () { window.location.reload(); })
                .fail(function () { navigator.id.logout(); });
            }
    });
};

window.Tango = {
    Accounts: {
        initialize: initialize
    }
};
