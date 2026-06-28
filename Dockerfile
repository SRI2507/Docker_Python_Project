From python:3.11-slim
MAINTAINER sri
COPY . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirement.txt
ENTRYPOINT ["python","app.py"]
