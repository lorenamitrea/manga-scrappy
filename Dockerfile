FROM python:3.11-slim-buster
WORKDIR /code
COPY requirements.txt requirements.txt
COPY run.sh run.sh
RUN pip3 install -r requirements.txt
COPY . .
WORKDIR /code/scrappy
EXPOSE 8000
CMD ["./run.sh"]