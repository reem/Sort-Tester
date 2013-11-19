# Jonathan's Amazing Sort Tester #
==================================

Sort testing made easy. Just put: `from sort_test import sort_test` at the
top of your sorting script then make your main function look like this:

`from sort_test import sort_test

def main():
    sort_test([your_sort])`

It's important you include the brackets, so don't forget them! If you want to
test against python's built-in sort you can do:

`from sort_test import sort_test

def main():
    sort_test([your_sort, sorted])`

In fact, you can pass `sort_test` a list with as many sort functions that you
want and it will test them all!

It has a bunch more options, but if you want to know about them you'll have
to ask me.

## Installing ##
================

All you need to do it put `sort_test.py` in the same folder as your sorting
script so you can import it easily.

You can download this whole folder by clicking the little "download" button
to the right, then just grab `sort_test.py` from the folder and move it. It
should Just Work from there.
