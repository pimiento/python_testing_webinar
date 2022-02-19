- [Какое бывает тестирование](#orgf9700f9)
- [Ручное тестирование](#orgd78a9fa)
- [Performance testing](#orgeb5d4ba)
- [Performance testing](#orgdd4e9ca)
- [Performance testing](#orgaec9de4)
- [Performance testing](#org5bef33e)
- [Performance testing](#org57be9ce)
- [unit-tests](#org5c4fcd4)
- [Unittest vs Pytest](#org701b3fa)
- [functional testing](#org2629c8a)
- [functional testing](#org32aa87b)
- [integration testing](#org339d521)
- [BDD](#orgcc117ec)
- [Тестирование GUI](#orgfc0c109)
- [Автоматизация тестирования](#orgf3b0c15)
- [Полезные ссылки](#orgcc80414)
- [Вопросы-ответы](#org5c7d964)



<a id="orgf9700f9"></a>

# Какое бывает тестирование

-   manual testing (ручное тестирование)
-   performance testing (тестирование производительности)
-   unit-testing (юнит-тестирование)
-   functional testing (функциональное тестирование)
-   integration testing (интеграционное тестирование)
-   regression testing (регрессионное тестирование)


<a id="orgd78a9fa"></a>

# Ручное тестирование

Обычно у тестировщика есть некоторый план *стандартных задач и действий пользователя*. Тестировщик по этому плану проходит, может пробовать вводить нестандартные значения в формы, пытаться "перехитрить" нашу программу


<a id="orgeb5d4ba"></a>

# Performance testing

Время работы

```python
import time
start = time.time()
COUNT = int(1e2)
result = sum(x for x in range(COUNT))
finish = time.time()
print(
    f"Time to summarazie {COUNT:.0E}: "
    f"{finish-start:.5f}"
)
```

    Time to summarazie 1E+02: 0.00001


<a id="orgdd4e9ca"></a>

# Performance testing

Время работы

```python
import timeit
from pprint import pp
pp(timeit.repeat(
    "sum(x for x in range(int(1e2)))",
    number=1,
    globals=globals()
))
```

    [7.2160037234425545e-06,
     4.334026016294956e-06,
     3.87697946280241e-06,
     3.8879807107150555e-06,
     3.934954293072224e-06]


<a id="orgaec9de4"></a>

# Performance testing

Профилирование по времени

```python
import cProfile

cProfile.run(
    "sum(x for x in range(int(1e2)))"
)
```


<a id="org5bef33e"></a>

# Performance testing

Профилирование по памяти

```python
@profile
def my_func():
    a = (x for x in range(int(1e2)))
    b = [x for x in range(int(1e2))]
    del b
    return a

if __name__ == '__main__':
    my_func()
```

```shell
python -m memory_profiler mem_prof.py
```


<a id="org57be9ce"></a>

# Performance testing

Apache Benchmark

```shell
sudo apt install apache2-utils
ab -V
# ab -c 10 -n 8000 http://localhost:8000/
```

    This is ApacheBench, Version 2.3 <$Revision: 1843412 $>
    Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
    Licensed to The Apache Software Foundation, http://www.apache.org/


<a id="org5c4fcd4"></a>

# unit-tests

-   Обычно пишутся самими программистами.
-   В идеали сначала программисты пишут тесты, а потом покрывают эти тесты кодом. TDD: Test Driven Development
-   Каждый тест должен быть независим от других, многие фреймворки позволяют запускать тесты параллельно.


<a id="org701b3fa"></a>

# Unittest vs Pytest

-   Unittest встроен в Python, pytest надо устанавливать.
-   pytest богаче в плане вывода отчётов, параметризации тестов, поэтому используется чаще.
-   pytest поддерживает запусков тестов для unittest (имеет обратную совместимость с unittest)


<a id="org2629c8a"></a>

# functional testing

Главное <span class="underline"><span class="underline">[отличие](https://www.educba.com/unit-test-vs-functional-test/)</span></span> от Unit-tests в том, что пишущий такие тесты не знает об устройстве программы. Такой подход называется **black-box**.
Функциональные тесты проверяют, что вызов некоторой функции / <span class="underline"><span class="underline">[API](https://redoc.ly/docs/cli/)</span></span> / HTML-формы с конкретными параметрами вернёт конкретный результат.


<a id="org32aa87b"></a>

# functional testing

<span class="underline"><span class="underline">[Doctest](https://docs.python.org/3/library/doctest.html)</span></span>

```python
import doctest
def square(x):
    """Return the square of x.

    >>> square(2)
    4
    >>> square(-2)
    0
    """
    return x * x
if __name__ == "__main__":
    doctest.testmod()
```


<a id="org339d521"></a>

# integration testing

В отличие от unit tests, мы тестируем модули на своместную работу. Например

    Создание комментариев к записям и удаление записей
    в отдельных unit-тестах уже протестировано.
    В интеграционном тесте нам необходимо протестировать
    удаление записей после создания комментария.


<a id="orgcc117ec"></a>

# BDD

Behave Driven Development

    Feature: Rocking with behave and django

        Scenario: тестовый клиент Django
            When django-клиент обращается к адресу "/"
            Then это должно вернуть страницу удачно
            And я увижу заголовок вкладки \
                "Последние обновления | Yatube"


<a id="orgfc0c109"></a>

# Тестирование GUI

```shell
pip install selenium
```

```python
from selenium import webdriver
from selenium.webdriver.common.keys \
    import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
```


<a id="orgf3b0c15"></a>

# Автоматизация тестирования

```shell
vim .git/hooks/pre-commit
```


<a id="orgcc80414"></a>

# Полезные ссылки

-   <span class="underline"><span class="underline">[TDD](https://habr.com/ru/company/ruvds/blog/450316/)</span></span>
-   <span class="underline"><span class="underline">[Selenium & Python](https://selenium-python.readthedocs.io/)</span></span>
-   <span class="underline"><span class="underline">[Selenium & BDD](https://www.bddtesting.com/using-the-behave-framework-for-selenium-bdd-testing-a-tutorial/)</span></span>


<a id="org5c7d964"></a>

# Вопросы-ответы

![img](questions.jpg)
