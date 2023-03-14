FROM python:3.8

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

# 5000 Port 
EXPOSE 5000

CMD ["python","app.py"]