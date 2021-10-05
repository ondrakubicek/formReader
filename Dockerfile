FROM python:3.8

WORKDIR /src

RUN apt-get update 
RUN apt-get install tesseract-ocr tesseract-ocr-ces  ffmpeg libsm6 libxext6  -y

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "src/main.py" ]