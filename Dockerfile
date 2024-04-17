FROM python:3.12-slim

RUN apt-get update && apt-get upgrade -y

COPY ./backend/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./backend/. app/
# COPY .env .

WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

