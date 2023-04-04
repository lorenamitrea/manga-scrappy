FROM python:3.11-slim-buster
WORKDIR /code
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
WORKDIR /code/scrappy
EXPOSE 8000
CMD ["/code/run.sh"]