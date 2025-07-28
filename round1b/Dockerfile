FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && python -m nltk.downloader punkt

COPY . .

CMD ["python", "round1b_main.py"]
