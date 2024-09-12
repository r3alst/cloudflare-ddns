FROM python:3.12.6-slim

# Required for Capturing Container logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir "/app"
WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD ["tail", "-f", "/dev/null"]