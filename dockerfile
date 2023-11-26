FROM python
COPY ./app
WORKDIR /app
COPY requirements.txt .
CMD ["python","app.py"]