FROM python:3.12-slim AS base


WORKDIR /app


# Устанавливаем зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# Копируем приложение
COPY app ./app


EXPOSE 8000


# Команда для dev переопределяется в compose (с --reload)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]