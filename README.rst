HabraFavorites
==============


.. image:: https://img.shields.io/pypi/v/habra-favorites.svg
    :alt: Последняя версия
    :target: https://pypi.python.org/pypi/habra-favorites/

.. image:: https://img.shields.io/pypi/dm/habra-favorites.svg
    :alt: Загрузки
    :target: https://pypi.python.org/pypi/habra-favorites/


Статистика избранных статей с сайта `Хабр <http://habr.com>`_
в виде HTML-страницы или данных в различных форматах.

.. image:: https://habrastorage.org/files/24c/1d3/0d6/24c1d30d62d84d7eb7fb9647d6a0e960.png
    :alt: Статистика


Установка
---------

.. code-block:: bash

    $ pip install habra-favorites

Приложение основано на фреймворке `Scrapy <http://scrapy.org>`_.
При возникновении ошибок при установке обратитесь к
`инструкции по установке Scrapy <http://doc.scrapy.org/en/latest/intro/install.html#pre-requisites>`_.


Использование
-------------

.. code-block:: bash

    $ habra_favorites [-h] [--version] [-f FORMAT] [-o NAME] username

Один обязательный параметр -- *username*. Логин пользователя, чьи избранные статьи будут собраны.
Это может быть как Ваш логин, так и логин любого другого пользователя.

Опции:

* FORMAT -- формат результата: *html* (по умолчанию), *json*, *csv*, *xml*;
* NAME -- имя файла для сохранения: по умолчанию *favorites.html* .


Результат
---------

При нажатии на заголовки колонок созданной HTML-страницы посты отсортируются в соответствующем порядке.
Повторное нажатие на активный заголовок пересортирует посты в обратном порядке.
