- [Какое бывает тестирование](#org8443ee9)
- [Ручное тестирование](#orga90fd8d)
- [Performance testing](#org55cb383)
- [Performance testing](#orga536a24)
- [Performance testing](#org0196783)
- [Performance testing](#org438adaa)
- [Performance testing](#orge4c10cf)
- [unit-tests](#org8439bab)
- [Unittest vs Pytest](#orgbe47ed2)
- [functional testing](#orga0b9e75)
- [functional testing](#org1809895)
- [integration testing](#org2e7fda9)
- [BDD](#orgea6bc85)
- [Тестирование GUI](#orga2f90ef)
- [Автоматизация тестирования](#orga8f3aae)
- [Полезные ссылки](#orgfee612d)
- [Вопросы-ответы](#org236e12b)



<a id="org8443ee9"></a>

# Какое бывает тестирование

-   manual testing (ручное тестирование)
-   performance testing (тестирование производительности)
-   unit-testing (юнит-тестирование)
-   functional testing (функциональное тестирование)
-   integration testing (интеграционное тестирование)
-   regression testing (регрессионное тестирование)


<a id="orga90fd8d"></a>

# Ручное тестирование

Обычно у тестировщика есть некоторый план *стандартных задач и действий пользователя*. Тестировщик по этому плану проходит, может пробовать вводить нестандартные значения в формы, пытаться "перехитрить" нашу программу


<a id="org55cb383"></a>

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


<a id="orga536a24"></a>

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

    [6.193993613123894e-06,
     4.436005838215351e-06,
     3.9780279621481895e-06,
     4.007015377283096e-06,
     3.918015863746405e-06]


<a id="org0196783"></a>

# Performance testing

Профилирование по времени

```python
import cProfile

cProfile.run(
    "sum(x for x in range(int(1e2)))"
)
```


<a id="org438adaa"></a>

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


<a id="orge4c10cf"></a>

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


<a id="org8439bab"></a>

# unit-tests

-   Обычно пишутся самими программистами.
-   В идеали сначала программисты пишут тесты, а потом покрывают эти тесты кодом. TDD: Test Driven Development
-   Каждый тест должен быть независим от других, многие фреймворки позволяют запускать тесты параллельно.


<a id="orgbe47ed2"></a>

# Unittest vs Pytest

-   Unittest встроен в Python, pytest надо устанавливать.
-   pytest богаче в плане вывода отчётов, параметризации тестов, поэтому используется чаще.
-   pytest поддерживает запусков тестов для unittest (имеет обратную совместимость с unittest)


<a id="orga0b9e75"></a>

# functional testing

Главное <span class="underline"><span class="underline">[отличие](https://www.educba.com/unit-test-vs-functional-test/)</span></span> от Unit-tests в том, что пишущий такие тесты не знает об устройстве программы. Такой подход называется **black-box**.
Функциональные тесты проверяют, что вызов некоторой функции / <span class="underline"><span class="underline">[API](https://redoc.ly/docs/cli/)</span></span> / HTML-формы с конкретными параметрами вернёт конкретный результат.


<a id="org1809895"></a>

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


<a id="org2e7fda9"></a>

# integration testing

В отличие от unit tests, мы тестируем модули на своместную работу. Например

    Создание комментариев к записям и удаление записей
    в отдельных unit-тестах уже протестировано.
    В интеграционном тесте нам необходимо протестировать
    удаление записей после создания комментария.


<a id="orgea6bc85"></a>

# BDD

Behave Driven Development

    Feature: Rocking with behave and django

        Scenario: тестовый клиент Django
            When django-клиент обращается к адресу "/"
            Then это должно вернуть страницу удачно
            And я увижу заголовок вкладки \
                "Последние обновления | Yatube"


<a id="orga2f90ef"></a>

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


<a id="orga8f3aae"></a>

# Автоматизация тестирования

```shell
vim .git/hooks/pre-commit
```


<a id="orgfee612d"></a>

# Полезные ссылки

-   <span class="underline"><span class="underline">[TDD](https://habr.com/ru/company/ruvds/blog/450316/)</span></span>
-   <span class="underline"><span class="underline">[Selenium & Python](https://selenium-python.readthedocs.io/)</span></span>
-   <span class="underline"><span class="underline">[Selenium & BDD](https://www.bddtesting.com/using-the-behave-framework-for-selenium-bdd-testing-a-tutorial/)</span></span>


<a id="org236e12b"></a>

# Вопросы-ответы

![img](questions.jpg)
