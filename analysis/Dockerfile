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
COPY app.py .
COPY wsgi.py .
ENV FLASK_ENV=production
CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:3002", "--workers", "4"]