# ---------- Base ----------
FROM python:3.11-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Development ----------
FROM base AS development
COPY app.py .
RUN pip install debugpy
ENV FLASK_ENV=development



CMD ["python","app.py" ]

# ---------- Production ----------
FROM base AS production
ENV FLASK_ENV=production
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:8001", "--workers", "4"]