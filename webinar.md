- [Какое бывает тестирование](#orgcde77e7)
- [Ручное тестирование](#org29f8e3e)
- [Performance testing](#org37765ad)
- [Performance testing](#orgd71c11c)
- [Performance testing](#org797dd86)
- [Performance testing](#org1b66de0)
- [Performance testing](#org4b5841f)
- [unit-tests](#orga227e3a)
- [Unittest vs Pytest](#org1a960c6)
- [functional testing](#org6a94a0f)
- [functional testing](#org52001b7)
- [integration testing](#org5f62c8b)
- [BDD](#org8849d84)
- [Тестирование GUI](#org3a7a1c9)
- [Автоматизация тестирования](#org9916db1)
- [Полезные ссылки](#org95f2f83)
- [Вопросы-ответы](#org96e478d)



<a id="orgcde77e7"></a>

# Какое бывает тестирование

-   manual testing (ручное тестирование)
-   performance testing (тестирование производительности)
-   unit-testing (юнит-тестирование)
-   functional testing (функциональное тестирование)
-   integration testing (интеграционное тестирование)
-   regression testing (регрессионное тестирование)


<a id="org29f8e3e"></a>

# Ручное тестирование

Обычно у тестировщика есть некоторый план *стандартных задач и действий пользователя*. Тестировщик по этому плану проходит, может пробовать вводить нестандартные значения в формы, пытаться "перехитрить" нашу программу


<a id="org37765ad"></a>

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


<a id="orgd71c11c"></a>

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

    [6.076006684452295e-06,
     4.481000360101461e-06,
     4.092988092452288e-06,
     3.982975613325834e-06,
     3.857014235109091e-06]


<a id="org797dd86"></a>

# Performance testing

Профилирование по времени

```python
import cProfile

cProfile.run(
    "sum(x for x in range(int(1e2)))"
)
```


<a id="org1b66de0"></a>

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


<a id="org4b5841f"></a>

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


<a id="orga227e3a"></a>

# unit-tests

-   Обычно пишутся самими программистами.
-   В идеали сначала программисты пишут тесты, а потом покрывают эти тесты кодом. TDD: Test Driven Development
-   Каждый тест должен быть независим от других, многие фреймворки позволяют запускать тесты параллельно.


<a id="org1a960c6"></a>

# Unittest vs Pytest

-   Unittest встроен в Python, pytest надо устанавливать.
-   pytest богаче в плане вывода отчётов, параметризации тестов, поэтому используется чаще.
-   pytest поддерживает запусков тестов для unittest (имеет обратную совместимость с unittest)


<a id="org6a94a0f"></a>

# functional testing

Главное <span class="underline"><span class="underline">[отличие](https://www.educba.com/unit-test-vs-functional-test/)</span></span> от Unit-tests в том, что пишущий такие тесты не знает об устройстве программы. Такой подход называется **black-box**.
Функциональные тесты проверяют, что вызов некоторой функции / <span class="underline"><span class="underline">[API](https://redoc.ly/docs/cli/)</span></span> / HTML-формы с конкретными параметрами вернёт конкретный результат.


<a id="org52001b7"></a>

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


<a id="org5f62c8b"></a>

# integration testing

В отличие от unit tests, мы тестируем модули на своместную работу. Например

    Создание комментариев к записям и удаление записей
    в отдельных unit-тестах уже протестировано.
    В интеграционном тесте нам необходимо протестировать
    удаление записей после создания комментария.


<a id="org8849d84"></a>

# BDD

Behave Driven Development

    Feature: Rocking with behave and django

        Scenario: тестовый клиент Django
            When django-клиент обращается к адресу "/"
            Then это должно вернуть страницу удачно
            And я увижу заголовок вкладки \
                "Последние обновления | Yatube"


<a id="org3a7a1c9"></a>

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


<a id="org9916db1"></a>

# Автоматизация тестирования

```shell
vim .git/hooks/pre-commit
```


<a id="org95f2f83"></a>

# Полезные ссылки

-   <span class="underline"><span class="underline">[TDD](https://habr.com/ru/company/ruvds/blog/450316/)</span></span>
-   <span class="underline"><span class="underline">[Selenium & Python](https://selenium-python.readthedocs.io/)</span></span>
-   <span class="underline"><span class="underline">[Selenium & BDD](https://www.bddtesting.com/using-the-behave-framework-for-selenium-bdd-testing-a-tutorial/)</span></span>


<a id="org96e478d"></a>

# Вопросы-ответы

![img](/home/pimiento/yap/questions.jpg)
