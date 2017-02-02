FROM python:2.7
ENV PYTHONUNBUFFERED 1

# Create App Folder
WORKDIR /var/app

# Bundle Src
COPY . .

# Expose Port
EXPOSE 8005

RUN pip install -r requirements/development.txt
