FROM python:3
# Install requirements
COPY requirements.txt ./
COPY website/index.html /usr/share/nginx/html/index.html
RUN pip install --no-cache-dir -r requirements.txt
# Install application
COPY perrikulos.py ./
# Run application
CMD python perrikulos.py
MAINTAINER "Gloria Ramirez"