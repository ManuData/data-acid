
FROM python:3.11

WORKDIR /data_acid

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "data_acid.wsgi:application", "--bind", "0.0.0.0:8000"] 

