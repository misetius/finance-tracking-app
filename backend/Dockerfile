# ---------- Base ----------
FROM python:3.11-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------- Development ----------
FROM base AS development
RUN pip install debugpy
ENV FLASK_ENV=development
COPY app.py .
CMD ["python", "app.py" ]

# ---------- Production ----------
FROM base AS production
ENV FLASK_ENV=production
COPY app.py .
COPY wsgi.py .
ENV FLASK_ENV=production
CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:3001", "--workers", "4"]
