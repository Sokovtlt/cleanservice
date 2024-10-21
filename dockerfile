# Используем базовый образ с Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /usr/src/app

# Копируем файл зависимостей проекта
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . .

# Открываем порт для доступа к приложению
EXPOSE 8000

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && python populate_db.py && python manage.py runserver 0.0.0.0:8000"]
