## issue-01

1. Команда:
```python
python -m doctest -v morse.py   
```
результат:
```doctest
Trying:
    encode('MAI-PYTHON-2019')
Expecting:
    '-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.'
ok
Trying:
    encode('A B')
Expecting:
     '.-   -...'
**********************************************************************
File "/Users/margaritaudalova/PycharmProjects/pythonProjectnew/test_morse.py", line 35, in morse.encode
Failed example:
    encode('A B')
Expected:
     '.-   -...'
Got:
    '.-   -...'
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('a b')
Expecting:
    Traceback (most recent call last):
    ...
    KeyError: 'a'
ok
2 items had no tests:
    morse
    morse.decode
**********************************************************************
1 items had failures:
   1 of   4 in morse.encode
4 tests in 3 items.
3 passed and 1 failed.
***Test Failed*** 1 failures.
```

2.  Команда:
```python
python -m doctest -o NORMALIZE_WHITESPACE -v morse.py
```
результат:
```doctest
Trying:
    encode('MAI-PYTHON-2019')
Expecting:
    '-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.'
ok
Trying:
    encode('A B')
Expecting:
     '.-   -...'
ok
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('a b')
Expecting:
    Traceback (most recent call last):
    ...
    KeyError: 'a'
ok
2 items had no tests:
    morse
    morse.decode
1 items passed all tests:
   4 tests in morse.encode
4 tests in 3 items.
4 passed and 0 failed.
Test passed.
```




## issue-02

```python
python -m pytest morse.py
```

результат:
```pytest
=========================================================================== test session starts ============================================================================
platform darwin -- Python 3.10.0, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/margaritaudalova/PycharmProjects/pythonProjectnew
collected 5 items                                                                                                                                                          

morse.py ....F                                                                                                                                                       [100%]

================================================================================= FAILURES =================================================================================
________________________________________________________________________ test_func[.-   -...-A B ] _________________________________________________________________________

msg = '.-   -...', exp = 'A B '

    @pytest.mark.parametrize('msg, exp', [
        ('... --- ...', 'SOS'),
        ('-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.', 'MAI-PYTHON-2019'),
        ('.-   -...', 'A B ')
    ])
    def test_func(msg, exp):
>       assert decode(msg) == exp
E       AssertionError: assert 'AB' == 'A B '
E         - A B 
E         + AB

morse.py:75: AssertionError
========================================================================= short test summary info ==========================================================================
FAILED morse.py::test_func[.-   -...-A B ] - AssertionError: assert 'AB' == 'A B '
======================================================================= 1 failed, 4 passed in 0.07s ========================================================================
```

## issue-03
1. Команда:
```python
python -m unittest one_hot_encoder.py
```
результат:

```doctest
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

```

2. Команда:
```python
 python -m unittest -v one_hot_encoder.py
```
результат:

```doctest
test_exception (one_hot_encoder.TestOneHot) ... ok
test_in (one_hot_encoder.TestOneHot) ... ok
test_is_istance (one_hot_encoder.TestOneHot) ... ok
test_not_in (one_hot_encoder.TestOneHot) ... ok
test_tf (one_hot_encoder.TestOneHot) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

3. Команда:
```python
  python -m unittest one_hot_encoder.TestOneHot.test_is_istance
```

результат:

```doctest
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```


## issue-04
1. Команда:
```python
 python -m pytest one_hot_encoder.py
```
результат:
```pytest
=========================================================================== test session starts ============================================================================
platform darwin -- Python 3.10.0, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/margaritaudalova/PycharmProjects/pythonProjectnew
collected 9 items                                                                                                                                                          

one_hot_encoder.py .........                                                                                                                                         [100%]

============================================================================ 9 passed in 0.02s =============================================================================
```


