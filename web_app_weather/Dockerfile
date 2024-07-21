FROM python:3.9

WORKDIR /app

COPY ../requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY .. .

# Для отладки
#CMD ["python", "web_app_weather/manage.py", "runserver", "0:8000"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "web_app_weather.wsgi"]