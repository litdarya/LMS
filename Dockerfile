FROM python:3.6

EXPOSE 8000

RUN mkdir -p /app/src
WORKDIR /app/src
COPY . .
RUN python3 setup.py install
WORKDIR /app/src/lms
CMD python3 client.py --port 8000
