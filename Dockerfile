FROM python:3.11-slim

COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir --timeout=600 -r requirements.txt

COPY . .

WORKDIR /src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5001", "--reload"]