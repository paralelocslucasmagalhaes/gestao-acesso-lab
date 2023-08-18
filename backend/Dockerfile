FROM python:3.8-slim as base

RUN  apt update -y && \
     pip install --upgrade pip

WORKDIR /usr/src/app

COPY requirements.txt .
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

####################### DEBUG ###############################
FROM base as debug
RUN pip install debugpy -t /tmp

####################### PRODUCTION ###############################
FROM base as production
ENTRYPOINT ["uvicorn",  "main:app", "--host", "0.0.0.0"]