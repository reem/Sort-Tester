# Jonathan's Amazing Sort Tester! #

Sort testing made easy. Just make your main function in your sorting script
look like this:

``` python
from sort_test import sort_test

def main():
    sort_test([your_sort])

# Don't forget this! You need it everywhere, even though
# I'm not including it in other places in this guide.
if __name__ == '__main__':
    main()
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

## Options ##

`sort_test` has tons of optional arguments and setting, these are some
instructions for them:

The first optional argument is `max_size_order`, which lets you control how
large the largest list you will test on is. It's default value is 7, meaning
that if you ignore it `sort_test()` will test your sort on lists of length
10^2, 10^3 .. 10^7.

If you want to change that, you should call `sort_test()` like this:

``` python
from sort_test import sort_test

def main():
    sort_test([your_sort, sorted], max_size_order=N)
```

Where N is just the max size you want.

The second option argument is `mult_list_size` which just lets you set if you
want to test more than one list size or just the max list size. True means you
want more than one list size, False means you want just the max.

Called like:

``` python
from sort_test import sort_test

def main():
    sort_test([your_sort, sorted], mult_list_size=True/False)
```

The third option, `check_sort`, lets you tell `sort_test` if you want it to
check if your sorts are correct instead of just giving you timing data. True
means you want it to check, False means you don't. Again,
called like:

``` python
from sort_test import sort_test

def main():
    sort_test([your_sort, sorted], check_sort=True/False)
```

The last option is defaulted to False, but if you turn `verbose_timing` to True
it will tell you what sort it is testing as it tests it for each list size.
Called like so:

``` python
from sort_test import sort_test

def main():
    sort_test([your_sort, sorted], verbose_timing=True/False)
```

You can combine these options however you want, just separate each assignment
by a comma like you would a regular argument. The default settings are:

``` python
max_size_order = 7
mult_list_size = True
check_sort = True
verbose_timing = False
```

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
