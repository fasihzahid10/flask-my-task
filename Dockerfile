# Simple production Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_SECRET_KEY=change-this-in-production
ENV DATABASE_URL=sqlite:///db.sqlite3
EXPOSE 8000
CMD ["python", "-m", "gunicorn", "-b", "0.0.0.0:8000", "run:app"]
