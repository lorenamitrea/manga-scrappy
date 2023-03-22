FROM python:3.11-slim-buster
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
WORKDIR /code/scrappy
EXPOSE 8000
CMD ["python" , "manage.py", "runserver", "0.0.0.0:8000"]
