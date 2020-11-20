Config package
=================================================

Пакет общих утилит, использующихся в разных модулях проекта.

Скрипт decos.py
---------------

.. automodule:: config.decos
	:members:
	
Скрипт descryptors.py
---------------------

.. autoclass:: config.descryptors.Port
    :members:
   
Скрипт errors.py
---------------------
   
.. autoclass:: config.errors.ServerError
   :members:
   
Скрипт metaclasses.py
-----------------------

.. autoclass:: config.metaclasses.ServerMaker
   :members:
   
.. autoclass:: config.metaclasses.ClientMaker
   :members:
   
Скрипт utils.py
---------------------

common.utils. **get_message** (client)


	Функция приёма сообщений от удалённых компьютеров. Принимает сообщения JSON,
	декодирует полученное сообщение и проверяет что получен словарь.

config.utils. **send_message** (sock, message)


	Функция отправки словарей через сокет. Кодирует словарь в формат JSON и отправляет через сокет.


Скрипт dict.py
---------------------

Содержит разные глобальные переменные проекта.