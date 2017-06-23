FROM python:3-alpine
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP todo.py
RUN mkdir /code
WORKDIR /code
RUN pip install Flask
RUN pip install todoist-python
ADD . /code/
