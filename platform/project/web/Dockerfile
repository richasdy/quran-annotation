FROM python:latest
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt
COPY . .
CMD ["python", "app.py"]