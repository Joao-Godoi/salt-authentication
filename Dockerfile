FROM python:3.11

WORKDIR /src

COPY requirements.txt .
COPY src/ src/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
