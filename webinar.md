- [Какое бывает тестирование](#org2b9c754)
- [Ручное тестирование](#org8070b72)
- [Performance testing](#org809ec50)
- [Performance testing](#org06633fb)
- [Performance testing](#org5811c17)
- [Performance testing](#org6c7f773)
- [Performance testing](#org1439eb0)
- [unit-tests](#orgd9b8493)
- [Unittest vs Pytest](#org1682683)
- [functional testing](#org7da8e0a)
- [functional testing](#org641fee4)
- [integration testing](#org54b2db2)
- [BDD](#orgb62f66f)
- [Тестирование GUI](#org3bcbe65)
- [Автоматизация тестирования](#org5c385f9)
- [Полезные ссылки](#org1dc461a)
- [Вопросы-ответы](#org86f4ea3)



<a id="org2b9c754"></a>

# Какое бывает тестирование

-   manual testing (ручное тестирование)
-   performance testing (тестирование производительности)
-   unit-testing (юнит-тестирование)
-   functional testing (функциональное тестирование)
-   integration testing (интеграционное тестирование)
-   regression testing (регрессионное тестирование)


<a id="org8070b72"></a>

# Ручное тестирование

Обычно у тестировщика есть некоторый план *стандартных задач и действий пользователя*. Тестировщик по этому плану проходит, может пробовать вводить нестандартные значения в формы, пытаться "перехитрить" нашу программу


<a id="org809ec50"></a>

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

    Time to summarazie 1E+07: 0.65679


<a id="org06633fb"></a>

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

    [0.6795534949633293,
     0.6839712829678319,
     0.6633882729802281,
     0.7683523200103082,
     0.7122829120489769]


<a id="org5811c17"></a>

# Performance testing

Профилирование по времени

```python
import cProfile

cProfile.run(
    "sum(x for x in range(int(1e7)))"
)
```


<a id="org6c7f773"></a>

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


<a id="org1439eb0"></a>

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


<a id="orgd9b8493"></a>

# unit-tests

-   Обычно пишутся самими программистами.
-   В идеали сначала программисты пишут тесты, а потом покрывают эти тесты кодом. TDD: Test Driven Development
-   Каждый тест должен быть независим от других, многие фреймворки позволяют запускать тесты параллельно.


<a id="org1682683"></a>

# Unittest vs Pytest

-   Unittest встроен в Python, pytest надо устанавливать.
-   pytest богаче в плане вывода отчётов, параметризации тестов, поэтому используется чаще.
-   pytest поддерживает запусков тестов для unittest (имеет обратную совместимость с unittest)


<a id="org7da8e0a"></a>

# functional testing

Главное <span class="underline"><span class="underline">[отличие](https://www.educba.com/unit-test-vs-functional-test/)</span></span> от Unit-tests в том, что пишущий такие тесты не знает об устройстве программы. Такой подход называется **black-box**.
Функциональные тесты проверяют, что вызов некоторой функции / <span class="underline"><span class="underline">[API](https://redoc.ly/docs/cli/)</span></span> / HTML-формы с конкретными параметрами вернёт конкретный результат.


<a id="org641fee4"></a>

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


<a id="org54b2db2"></a>

# integration testing

В отличие от unit tests, мы тестируем модули на своместную работу. Например

    Создание комментариев к записям и удаление записей
    в отдельных unit-тестах уже протестировано.
    В интеграционном тесте нам необходимо протестировать
    удаление записей после создания комментария.


<a id="orgb62f66f"></a>

# BDD

Behave Driven Development

    Feature: Rocking with behave and django

        Scenario: тестовый клиент Django
            When django-клиент обращается к адресу "/"
            Then это должно вернуть страницу удачно
            And я увижу заголовок вкладки \
                "Последние обновления | Yatube"


<a id="org3bcbe65"></a>

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


<a id="org5c385f9"></a>

# Автоматизация тестирования

```shell
vim .git/hooks/pre-commit
```

```shell
#!/bin/bash
pylint .
[ $? -ne 0 ] && exit 1
mypy *.py
[ $? -ne 0 ] && exit 1
pytest .
[ $? -ne 0 ] && exit 1
```

```shell
chmod +x .git/hooks/pre-commit
```


<a id="org1dc461a"></a>

# Полезные ссылки

-   <span class="underline"><span class="underline">[TDD](https://habr.com/ru/company/ruvds/blog/450316/)</span></span>
-   <span class="underline"><span class="underline">[Selenium & Python](https://selenium-python.readthedocs.io/)</span></span>
-   <span class="underline"><span class="underline">[Selenium & BDD](https://www.bddtesting.com/using-the-behave-framework-for-selenium-bdd-testing-a-tutorial/)</span></span>


<a id="org86f4ea3"></a>

# Вопросы-ответы

![img](questions.jpg)
