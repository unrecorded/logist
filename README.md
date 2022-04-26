Менеджер перевозок

Первоначальные действия для запуска:
1) Создаем виртуальное окружение: python -m venv env
2) Активируем виртуальное окружение
3) Устанавливаем необходимые зависимости: pip install -r requirements.txt
4) В settings.py правим подключение к базе данных под себя
5) Производим миграции
    5.1) python manage.py makemigrations
    5.2) python manage.py migrate
6) Создаем суперпользователя: python manage.py createsuperuser
7) Запускаем веб сервер: python manage.py runserver
9) Читаем вывод команды из пункта №7 и радуемся жизни