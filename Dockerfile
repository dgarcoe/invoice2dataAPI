FROM python:3.9.4-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  pkg-config \
  poppler-utils \
  libpoppler-cpp-dev \
  tesseract-ocr

COPY main.py app/
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

CMD ["uvicorn","app.main:invoice_api", "--host", "0.0.0.0", "--port", "80"]
