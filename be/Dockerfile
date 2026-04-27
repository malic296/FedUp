FROM python:3.12-slim
WORKDIR /api

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY be/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY be/ .

CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000"]