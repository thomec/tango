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


After spiking and changing back to `master`, the changes in `urls.py` and `base.html` where still there. I uncommented them after getting 'cannot import accounts' error.

later in the chapter, when copying the `lists/static` folder to `superlists/static` the tests do pass, but

    * I get `Not Found: /favicon.ico` from every test.
    * When I load test.html, the second test fails and passes alternating on every reload.


Later in 'A Simple Mock to Unit Test Our initialize Function' - the test `accounts/static/tests/test.html` passes from the beginning.

copy the code from `https://github.com/hjwp/book-example/tree/chapter_15`


Chapter 16
==========

The link to the [docs](https://docs.python.org/3/library/unittest.mock-magicmethods.html) in Note 31 is not working
