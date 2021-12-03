## issue-01

####1. Команда ниже которая импортирует файл `morse.py` для запуска для него ` testmod()`

```python
python -m doctest -v morse.py   
```
####2. Команда ниже запускает тесты с флагом `NORMALIZE_WHITESPACE`, который приравнивает любую последовательность пробелов,переносов строк и новых строк. 

```python
python -m doctest -o NORMALIZE_WHITESPACE -v morse.py
```





## issue-02

####Команда запускающая все тесты в файле `morse.py`
```python
python -m pytest morse.py
```



## issue-03
####Команда для запуска всех тестов в командной строке

```python
python -m unittest one_hot_encoder.py
```

####Также можно запустить такие варианты:

- выведет более детальную информацию по каждому тесту
```python
 python -m unittest -v one_hot_encoder.py
```
- выведет результат для конкретного теста
```python
  python -m unittest one_hot_encoder.TestOneHot.test_is_istance
```


## issue-04
####Команда запускающая все тесты в файле `one_hot_encoder.py`
```python
 python -m pytest one_hot_encoder.py
```



