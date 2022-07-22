FROM   python:3 
ENV  PYTHONUNBUFFERED 1
WORKDIR  /app2
ADD    . /app2
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY  . /app2
