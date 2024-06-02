FROM python:3.9

WORKDIR /product_api

COPY ./app /app/app
COPY requirements.txt /product_api

RUN pip install --no-cache-dir --upgrade -r /product_api/requirements.txt

CMD ["uvicorn", "product_api.main:app", "--host", "0.0.0.0", "--port", "8000"]

