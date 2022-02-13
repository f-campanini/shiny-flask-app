FROM python:3.9.10
WORKDIR /app
ADD . /app
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
EXPOSE 4444
CMD ["python", "app.py"]