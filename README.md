# scrapy_parser_pep

Парсер на Scrapy, который собирает все PEP и информацию о них с сайта https://peps.python.org/.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:Stepan22042004/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить проект:

```
scrapy crawl pep
```

Данные сохраняются в два csv файла в папку results.



### Стек использованных технологий
### Язык программирования и фреймворк:
  Python: основной язык программирования.\
  Scrapy
### Тестирование:
  Pytest: для написания тестов.

### Информация об авторе
Герасимов Степан
