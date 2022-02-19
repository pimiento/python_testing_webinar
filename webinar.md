- [Какое бывает тестирование](#org1480cde)
- [Ручное тестирование](#org9aba748)
- [Performance testing](#orgef1c228)
- [Performance testing](#orgc1cc448)
- [Performance testing](#orgd575f90)
- [Performance testing](#orgd495525)
- [Performance testing](#orgf0550bf)
- [unit-tests](#orgf1fb390)
- [Unittest vs Pytest](#org5e60d8b)
- [functional testing](#orgbfafec4)
- [functional testing](#orgd30c04c)
- [integration testing](#org652cf22)
- [BDD](#org4deb161)
- [Тестирование GUI](#orgbd07aaf)
- [Автоматизация тестирования](#orgcc40d2c)
- [Полезные ссылки](#org62a11f2)
- [Вопросы-ответы](#orgc4e657b)



<a id="org1480cde"></a>

# Какое бывает тестирование

-   manual testing (ручное тестирование)
-   performance testing (тестирование производительности)
-   unit-testing (юнит-тестирование)
-   functional testing (функциональное тестирование)
-   integration testing (интеграционное тестирование)
-   regression testing (регрессионное тестирование)


<a id="org9aba748"></a>

# Ручное тестирование

Обычно у тестировщика есть некоторый план *стандартных задач и действий пользователя*. Тестировщик по этому плану проходит, может пробовать вводить нестандартные значения в формы, пытаться "перехитрить" нашу программу


<a id="orgef1c228"></a>

# Performance testing

Время работы

```python
import time
start = time.time()
COUNT = int(1e7)
result = sum(x for x in range(COUNT))
finish = time.time()
print(
    f"Time to summarazie {COUNT:.0E}: "
    f"{finish-start:.5f}"
)
```

    Time to summarazie 1E+07: 0.68405


<a id="orgc1cc448"></a>

# Performance testing

Время работы

```python
import timeit
from pprint import pp
pp(timeit.repeat(
    "sum(x for x in range(int(1e7)))",
    number=1,
    globals=globals()
))
```

    [0.7027079269755632,
     0.6599279140355065,
     0.6704874390270561,
     0.6661182870157063,
     0.8078089479822665]


<a id="orgd575f90"></a>

# Performance testing

Профилирование по времени

```python
import cProfile

cProfile.run(
    "sum(x for x in range(int(1e7)))"
)
```


<a id="orgd495525"></a>

# Performance testing

Профилирование по памяти

```python
@profile
def my_func():
    a = (x for x in range(int(1e7)))
    b = [x for x in range(int(1e7))]
    del b
    return a

if __name__ == '__main__':
    my_func()
```

```shell
python -m memory_profiler mem_prof.py
```


<a id="orgf0550bf"></a>

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


<a id="orgf1fb390"></a>

# unit-tests

-   Обычно пишутся самими программистами.
-   В идеали сначала программисты пишут тесты, а потом покрывают эти тесты кодом. TDD: Test Driven Development
-   Каждый тест должен быть независим от других, многие фреймворки позволяют запускать тесты параллельно.


<a id="org5e60d8b"></a>

# Unittest vs Pytest

-   Unittest встроен в Python, pytest надо устанавливать.
-   pytest богаче в плане вывода отчётов, параметризации тестов, поэтому используется чаще.
-   pytest поддерживает запусков тестов для unittest (имеет обратную совместимость с unittest)


<a id="orgbfafec4"></a>

# functional testing

Главное <span class="underline"><span class="underline">[отличие](https://www.educba.com/unit-test-vs-functional-test/)</span></span> от Unit-tests в том, что пишущий такие тесты не знает об устройстве программы. Такой подход называется **black-box**.
Функциональные тесты проверяют, что вызов некоторой функции / <span class="underline"><span class="underline">[API](https://redoc.ly/docs/cli/)</span></span> / HTML-формы с конкретными параметрами вернёт конкретный результат.


<a id="orgd30c04c"></a>

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


<a id="org652cf22"></a>

# integration testing

В отличие от unit tests, мы тестируем модули на своместную работу. Например

    Создание комментариев к записям и удаление записей
    в отдельных unit-тестах уже протестировано.
    В интеграционном тесте нам необходимо протестировать
    удаление записей после создания комментария.


<a id="org4deb161"></a>

# BDD

Behave Driven Development

    Feature: Rocking with behave and django

        Scenario: тестовый клиент Django
            When django-клиент обращается к адресу "/"
            Then это должно вернуть страницу удачно
            And я увижу заголовок вкладки \
                "Последние обновления | Yatube"


<a id="orgbd07aaf"></a>

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
assert "No results found." not in \
    driver.page_source
driver.close()
```


<a id="orgcc40d2c"></a>

# Автоматизация тестирования

```shell
vim .git/hooks/pre-commit
```


<a id="org62a11f2"></a>

# Полезные ссылки

-   <span class="underline"><span class="underline">[TDD](https://habr.com/ru/company/ruvds/blog/450316/)</span></span>
-   <span class="underline"><span class="underline">[Selenium & Python](https://selenium-python.readthedocs.io/)</span></span>
-   <span class="underline"><span class="underline">[Selenium & BDD](https://www.bddtesting.com/using-the-behave-framework-for-selenium-bdd-testing-a-tutorial/)</span></span>


<a id="orgc4e657b"></a>

# Вопросы-ответы

![img](questions.jpg)
