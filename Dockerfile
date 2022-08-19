FROM python:3.9.5-buster

WORKDIR /

COPY . ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "-u", "app/app.py"]