FROM python:slim-bullseye

COPY . ./src

WORKDIR src

RUN pip install -r requirements.txt

ENTRYPOINT ["python","app.py"]

EXPOSE 8000