FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app/

COPY . /app/

RUN pip install -r requirements.txt

RUN python3 manage.py migrate

RUN python3 manage.py makemigrations api

RUN python3 manage.py migrate api

COPY . /app/

EXPOSE 5000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:5000"]