FROM python:3.9

RUN apt-get update -y
RUN apt-get install -y --no-install-recommends g++ protobuf-compiler libprotobuf-dev
RUN pip install gcld3>=3.0.13 flask>=2.0.1 waitress>=2.0.0

WORKDIR /usr/src/app
COPY src .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 9000
CMD ["python", "server.py"]