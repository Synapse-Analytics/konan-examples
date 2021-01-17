FROM python:3.7-slim-stretch

# install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential make gcc gnupg \
    python3-dev unixodbc-dev

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app

# install requirements
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt

# copy relevant files and directories
COPY . /app

EXPOSE 8000

CMD ["uvicorn", "endpoints:app", "--host", "0.0.0.0", "--port", "8000"]

