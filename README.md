# Онлайн платформа торговой сети электроники

## Задача

* Создать веб-приложение с API-интерфейсом и админ-панелью.
* Создать базу данных, используя миграции Django.

## Требуемый стэк

 * Python 3.8+
 * Django 3+
 * DRF 3.10+
 * PostgreSQL 10+

### Запуск проекта:

 * клонировать из Git-репозитория
 * установить venv
```python
python3 -m venv venv
```
 * активировать venv
```python
source venv/bin/activate
```
 * установить файл с зависимостями
```python
pip install -r requirements.txt
```
 * создать БД в PGAdmin.
 * создать в корне проекта файл ".env". Внести в файл данные на основе шаблона ".env.sample"
 * создать миграции командами:
```python
python manage.py makemigrations
python manage.py migrate
```
* проект запускается командой
```python
python manage.py runserver
```


### Создание суперпользователя:
```python
python manage.py csu
```
