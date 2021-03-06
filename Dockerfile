FROM python:3.8.5

WORKDIR /hi

COPY . .

ENTRYPOINT ["python3", "hello.py", "-n", "stranger"]