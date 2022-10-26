# 1 - Скачать данные через API по заданному URL

# Вам нужно написать функцию, которая обратится GET-запросом к
# веб-сервису и вернёт содержимое. Адрес веб-сервиса указан
# в параметре url. Веб-сервис отдаёт данные в виде JSON.

# Выберите все способы решения этой задачи.

import requests

def load_json(url):
    response = requests.get(url)
    return response.json()

##########################################
# Библиотеку requests можно использовать и с проверкой кода ответа,
# а также с обязательным закрытием сессии после выхода из блока.
# Так тоже сработает.

import requests

def load_json2(url):
    with requests.Session() as s:
        response = s.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

##########################################
# Задачу можно решить и с помощью модуля urllib.requests.
# В нём есть функции и классы для обращения к URL-адресам.

import urllib.request
import json

def load_json3(url):
    with urllib.request.urlopen(url) as response:
        if(response.getcode() == 200):
            data = response.read()
            jsonData = json.loads(data)
        else:
            print("Error receiving data", response.getcode())

    return jsonData
##########################################
# Используйте urllib3, если нужен более низкоуровневый контроль
# над пулом соединений, потокобезопасность и другие гибкие настройки.
import json
from urllib3 import PoolManager

def load_json4(url):
    manager = PoolManager(10)
    response = manager.request('GET', url)
    payload = response.data.decode()

    return json.loads(payload)

