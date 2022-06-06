- [Какое бывает тестирование](#org811ee29)
- [Ручное тестирование](#org8976c1e)
- [Performance testing](#org7597548)
- [Performance testing](#org8e52e44)
- [Performance testing](#org0495b32)
- [Performance testing](#org54241d9)
- [Performance testing](#org26c1cd9)
- [unit-tests](#org1c770c7)
- [Unittest vs Pytest](#orgafff265)
- [fixtures](#org5b431fc)
- [Faker](#org39069ea)
- [FactoryBoy](#org61987e2)
- [functional testing](#org2ca237f)
- [functional testing](#orgeae24e9)
- [integration testing](#orgda582f3)
- [BDD](#org82f65f5)
- [Тестирование GUI](#org74ad022)
- [Автоматизация тестирования](#orgb60401a)
- [Полезные ссылки](#org9b50ec1)
- [Вопросы-ответы](#orgf3cf50e)



<a id="org811ee29"></a>

# Какое бывает тестирование

-   manual testing (ручное тестирование)
-   performance testing (тестирование производительности)
-   unit-testing (юнит-тестирование)
-   functional testing (функциональное тестирование)
-   integration testing (интеграционное тестирование)
-   regression testing (регрессионное тестирование)


<a id="org8976c1e"></a>

# Ручное тестирование

Обычно у тестировщика есть некоторый план *стандартных задач и действий пользователя*. Тестировщик по этому плану проходит, может пробовать вводить нестандартные значения в формы, пытаться "перехитрить"  нашу программу


<a id="org7597548"></a>

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

    Time to summarazie 1E+07: 0.41940


<a id="org8e52e44"></a>

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

    [0.4033556989961653,
     0.44113256099808495,
     0.4357005010024295,
     0.443697044000146,
     0.4051942619989859]


<a id="org0495b32"></a>

# Performance testing

Профилирование по времени

```python
import cProfile

cProfile.run(
    "sum(x for x in range(int(1e7)))"
)
```


<a id="org54241d9"></a>

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


<a id="org26c1cd9"></a>

# Performance testing

Apache Benchmark

```shell
sudo apt install apache2-utils
ab -V
ab -c 10 -n 8000 http://localhost:8000/
```


<a id="org1c770c7"></a>

# unit-tests

-   Обычно пишутся самими программистами.
-   В идеале, сначала программисты пишут тесты, а потом покрывают эти тесты кодом. TDD: Test Driven Development
-   Каждый тест должен быть независим от других, многие фреймворки позволяют запускать тесты параллельно.


<a id="orgafff265"></a>

# Unittest vs Pytest

-   Unittest встроен в Python, pytest надо устанавливать.
-   pytest богаче в плане вывода отчётов, параметризации тестов, поэтому используется чаще.
-   pytest поддерживает запуск тестов для unittest (имеет обратную совместимость с unittest)


<a id="org5b431fc"></a>

# fixtures

<span class="underline"><span class="underline">[фикстуры](https://django-testing-docs.readthedocs.io/en/latest/fixtures.html)</span></span>

-   Описывают данные, которые должны быть созданы в тестовой базе данных.
-   Можно выгрузить данные из реальной базы и затем добавить их в тестовые данные.


<a id="org39069ea"></a>

# Faker

<span class="underline"><span class="underline">[pip install faker](https://faker.readthedocs.io/en/stable/)</span></span>

```python
from faker import Faker

fake = Faker("ru_RU.UTF-8")
print(fake.address())
print(fake.phone_number())
print(fake.ipv4())
```

    к. Лянтор, ул. Лесхозная, д. 92, 992435
    +7 428 501 84 99
    95.188.223.145


<a id="org61987e2"></a>

# FactoryBoy

<span class="underline"><span class="underline">[документация](https://factoryboy.readthedocs.io/en/stable/)</span></span>

-   Описывает фикстуры как Python-код
-   Возможность использовать Faker для создания случайных данных


<a id="org2ca237f"></a>

# functional testing

Главное <span class="underline"><span class="underline">[отличие](https://www.educba.com/unit-test-vs-functional-test/)</span></span> от Unit-tests в том, что пишущий такие тесты не знает об устройстве программы. Такой подход называется **black-box**.
Функциональные тесты проверяют, что вызов некоторого API с конкретными параметрами вернёт конкретный результат.


<a id="orgeae24e9"></a>

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


<a id="orgda582f3"></a>

# integration testing

В отличие от unit tests, мы тестируем модули на своместную работу. Например

    Создание комментариев к записям и удаление записей
    в отдельных unit-тестах уже протестировано.
    В интеграционном тесте нам необходимо протестировать
    удаление записей после создания комментария.


<a id="org82f65f5"></a>

# BDD

Behave Driven Development

    Feature: Rocking with behave and django

        Scenario: тестовый клиент Django
            When django-клиент обращается к адресу "/"
            Then это должно вернуть страницу удачно
            And я увижу заголовок вкладки \
                "Последние обновления | Yatube"


<a id="org74ad022"></a>

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


<a id="orgb60401a"></a>

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


<a id="org9b50ec1"></a>

# Полезные ссылки

-   <span class="underline"><span class="underline">[TDD](https://habr.com/ru/company/ruvds/blog/450316/)</span></span>
-   <span class="underline"><span class="underline">[MDN. Тестирование Django](https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Testing)</span></span>
-   <span class="underline"><span class="underline">[Pytest + Django](https://lexover.ru/2021/03/07/test-django-using-pytest/)</span></span>
-   <span class="underline"><span class="underline">[Selenium & Python](https://selenium-python.readthedocs.io/)</span></span>
-   <span class="underline"><span class="underline">[Selenium & BDD](https://www.bddtesting.com/using-the-behave-framework-for-selenium-bdd-testing-a-tutorial/)</span></span>
-   <span class="underline"><span class="underline">[Начнём работу с Mock в Python](https://nuancesprog.ru/p/1161/)</span></span>
-   <span class="underline"><span class="underline">[Модуль Mock: макеты пустышки в тестировании](https://habr.com/ru/post/141209/)</span></span>


<a id="orgf3cf50e"></a>

# Вопросы-ответы

![img](questions.jpg)
