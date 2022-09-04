# https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

FROM python:3.9

# set environment variables
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# set working directory
WORKDIR /code

# copy dependencies
COPY requirements.txt /code/

# install dependencies
RUN pip install -r requirements.txt

# copy project
COPY . /code/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]