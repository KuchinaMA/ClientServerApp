# CS_HW2 — Клиент-Сервер с TCP и UDP

Учебный проект в рамках курса курса "современные компьютерные сети". Реализован простой клиент-сервер, который может общаться по протоколам **TCP** и **UDP** с помощью Python-сокетов.  

- Сервер принимает сообщения и отправляет ответ.
- Клиент может отправлять сообщения серверу и получать ответ.
- Протокол сообщений: клиент отправляет строку, сервер отвечает в формате `"Got: <message>"`.

---


---

## Требования

- Python 3.8+  
- `netcat` (`nc`) для ручной проверки UDP/TCP (опционально)  
- Git  

---

## Установка и запуск

1. Клонируем репозиторий:

```bash
git clone https://github.com/KuchinaMA/ClientServerApp.git
cd CLientServerApp
```

2. Запуск сервера или клиента:
- TCP сервер (порт 8888 по умолчанию):

```
python3 main.py --role server --protocol tcp --port 8888
```

- TCP клиент

```
python3 main.py --role client --protocol tcp --host localhost --port 8888
```

- UDP сервер

```
python3 main.py --role server --protocol udp --port 8888
```

- UDP клиент

```
python3 main.py --role client --protocol udp --host localhost --port 8888
```
В клиенте можно писать сообщения, чтобы отправлять их серверу.
Для выхода из клиента введите `exit`.

## Тестирование

1. Убедитесь, что на вашей системе установлен `Python3` и `nc`.

2. Перейдите в папку проекта:

```
cd CS_HW2
```

3. Запуск тестов
```
python3 tests/run_all_tests.py
```

4. Пример вывода тетов:
```
[TCP] small message          PASSED
[TCP] large message          PASSED
[UDP] netcat compatibility   PASSED
```