FROM python:3-slim

ADD . /app/
WORKDIR /app
RUN pip install -r requirements.txt

# run CMD command python with arguments
CMD ["python", "-u", "main.py", "--auto"]


