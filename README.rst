HabraFavorites
==============


.. image:: https://badge.fury.io/py/habra-favorites.png
    :alt: Последняя версия
    :target: https://pypi.python.org/pypi/habra-favorites/

.. image:: https://pypip.in/download/habra-favorites/badge.png
    :alt: Загрузки
    :target: https://pypi.python.org/pypi/habra-favorites/

.. image:: https://gemnasium.com/ykalchevskiy/habra-favorites.png
    :alt: Состояние зависимостей
    :target: https://gemnasium.com/ykalchevskiy/habra-favorites

.. image:: https://pypip.in/license/habra-favorites/badge.png
    :alt: Лицензия
    :target: https://pypi.python.org/pypi/habra-favorites/


.. image:: http://beta.hstor.org/files/24c/1d3/0d6/24c1d30d62d84d7eb7fb9647d6a0e960.png
    :alt: Статистика

Статистика избранных статей с сайтов `Хабрахабр <http://habrahabr.ru>`_ и  `Geektimes <http://geektimes.ru>`_ в виде HTML страницы или данных в различных форматах.


Установка
---------

Приложение сделано с помощью `Scrapy <http://www.scrapy.org>`_. 
Для полноценной работы Scrapy лучше всего обратиться к соответствующей `инструкции <http://doc.scrapy.org/en/latest/intro/install.html#pre-requisites>`_. 
Обратите внимание, что требуется **Python 2.7**, ветка 3.x не поддерживается.
После настройки для Scrapy выполните:

.. code-block:: bash

    $ pip install -U habra-favorites

Протестировано на Ubuntu 12.04, на других UNIX/Linux системах тоже должно работать. Теоретически и на Windows :)


Использование
-------------

.. code-block:: bash

    $ habra_favorites [-h] [--version] [-d DOMAIN] [-f FORMAT] [-o NAME] username

Один обязательный параметр -- *username*. Логин пользователя, чьи избранные статьи будут собраны. Это может быть как Ваш логин, так и логин любого другого пользователя. 

Опции:

* DOMAIN -- сайт: *habrahabr.ru* (по умолчанию), *geektimes.ru*;
* FORMAT -- формат результата: *html* (по умолчанию), *json*, *csv*, *xml*;
* NAME -- имя файла для сохранения: по умолчанию *favorites.html* .

Подсказку можно посмотреть, воспользовавшись опцией *-h* или *--help*.


Результат
---------

Если Вы сгенерировали данные (json, csv), то Вы сами знаете, что с ними делать.
Если же Вы создали HTML страничку, то, нажимая на заголовки колонок, можно сортировать посты в соответствующем порядке.
При повторном нажатии на активный заголовок, посты будут отсортированы в обратном порядке.


To-do
-------

* Badges/shields: https://travis-ci.org/, https://coveralls.io/, http://shields.io/ .
* Добавить вывод информации о парсинге.
* Изменить лицензию на BSD (?).
* Объединить результаты для сайтов (?).
