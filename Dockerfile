FROM python:3.12-alpine

WORKDIR /app

RUN pip install requests beautifulsoup4 wget

COPY . .
 
CMD ["python","main.py"]