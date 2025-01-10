# Сайт по продаже вин

### Как запустить
Для указания пути по умолчанию к файлу excel с данными по винам создаем файл для переменных окружения `.env` в одной директории с файлом main.py и прописываем в него:
```
FILE_PATH=Ваш путь к файлу по умолчанию без кавычек
```
Вводим в терминале:
```
'python main.py -p {путь до файла excel с категориями, названиями, сортами, ценами вин, названиями картинок для сайта и наличием акций}'
```
Или, для выгрузки данных из файла по умолчанию, вводим в терминале:
```
'python main.py'
``` 

Запускаем файл `index.html`

Картинки с винами хранятся в папке `images`

### Структура программы

#### main
Принимает через терминал путь до файла с данными о винах или использует путь по умолчанию.

#### template
Файл с html-разметкой сайта

### Как установить
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```