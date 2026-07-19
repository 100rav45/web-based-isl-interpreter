FROM python:3.10-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Show logs immediately
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install Linux libraries required by OpenCV and MediaPipe
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libglvnd0 \
    libegl1 \
    libgles2 \
    libsm6 \
    libxext6 \
    libxrender1 \
    libgl1-mesa-glx \
    libglu1-mesa \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better build caching
COPY requirements-render.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements-render.txt

# Copy the rest of the project
COPY . .

EXPOSE 10000

CMD ["uvicorn", "app.backend.main:app", "--host", "0.0.0.0", "--port", "10000"]