FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy backend source code and requirements
COPY backend/requirements.txt ./backend/requirements.txt
RUN pip install --no-cache-dir -r backend/requirements.txt

COPY backend/ ./backend/

# Expose FastAPI port (default 8000)
EXPOSE 8000

# Environment variables (can be overridden at runtime)
ENV PYTHONUNBUFFERED=1

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]