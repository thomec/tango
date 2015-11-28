Comments on 'Test-Driven Web Development with Python'


Chapter 1
========

create project and `funtional_tests.py`


Chapter 2
=========

create class `NewVisitorTest` in `funtional_tests.py`

-> no need for `warnings='ignore'` at the end


Chapter 3
========

create lists app and `views.home_page`


Chapter 4
=========

extend `functional_test.py` to test saveing and retriving an item
refactor to use templates
add template `home.html`


Chapter 5
=========

input form with post
extended `functional_test.py` to test saving more items
refactor `functional_tests.py` using helper function `check_for_row_in_list_table`
add Item model


Chapter 6
=========

cleaning up test after ft

in "Capturing Parameters from URLs":
-> `sqlite3.IntegrityError: NOT NULL constraint failed: lists_item.list_id`

remove db-file, makemigrations, migrate didn't help
set `null=True` in item.model solved the issue

-> url parttern `(.+)` doesn't work, use `(P?<list_id>[0-9]+)`


Chapter 9
=========

in `def _get_latest_source()`
-> what does `git log -n 1 --format=%H`? ... Hash?


Chapter 15
==========

    python manage.py makemigrations
	SystemCheckError: System check identified some issues:

	ERRORS:
	accounts.ListUser.groups: (fields.E304) Reverse accessor for 'ListUser.groups' clashes with reverse accessor for 'User.groups'.
        HINT: Add or change a related_name argument to the definition for 'ListUser.groups' or 'User.groups'.
	accounts.ListUser.user_permissions: (fields.E304) Reverse accessor for 'ListUser.user_permissions' clashes with reverse accessor for 'User.user_permissions'.
        HINT: Add or change a related_name argument to the definition for 'ListUser.user_permissions' or 'User.user_permissions'.
	auth.User.groups: (fields.E304) Reverse accessor for 'User.groups' clashes with reverse accessor for 'ListUser.groups'.
        HINT: Add or change a related_name argument to the definition for 'User.groups' or 'ListUser.groups'.
	auth.User.user_permissions: (fields.E304) Reverse accessor for 'User.user_permissions' clashes with reverse accessor for 'ListUser.user_permissions'.
        HINT: Add or change a related_name argument to the definition for 'User.user_permissions' or 'ListUser.user_permissions'.
	(tango)thomec@beule:~/devel/tango$`



because I forgot in settings.py

    AUTH_USER_MODEL = 'accounts.ListUser'
    AUTHENTICATION_BACKENDS = (
        'accounts.authentication.PersonaAuthenticationBackend',
    )


