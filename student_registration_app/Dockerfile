FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x wait-for-it.sh

CMD ["python", "app/app.py"]
