# Jonathan's Amazing Sort Tester #

Sort testing made easy. Just put: `from sort_test import sort_test` at the
top of your sorting script then make your main function look like this:

``` python
from sort_test import sort_test

def main():
    sort_test([your_sort])
```

It's important you include the brackets, so don't forget them! If you want to
test against python's built-in sort you can do:

``` python
from sort_test import sort_test

def main():
    sort_test([your_sort, sorted])
```

In fact, you can pass `sort_test` a list with as many sort functions that you
want and it will test them all!

It has a bunch more options, which you can either figure out from the source or
ask me about. Please see the warning section if your sort is O(n^2)!!

## Installing ##

All you need to do it put `sort_test.py` in the same folder as your sorting
script so you can import it easily.

You can download this whole folder by clicking the little "download" button
to the right, then just grab `sort_test.py` from the folder and move it. It
should Just Work from there.

## WARNING ##

If your sort is O(n^2) *do not* just run this plain. You have to add
something to the `sort_test()` call or your computer is going to stall.

Your `main()` should look like this:

``` python
from sort_test import sort_test

def main():
    sort_test([your_sort, sorted], max_size_order=4)
```

What you're doing here is limiting the size of the lists you are testing
to 10.000, so you don't stall your computer trying to do effectively 10^10
comparisons.

## License ##

MIT License
