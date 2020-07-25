
FROM python:alpine3.7
COPY /src /src
WORKDIR /src
RUN pip install -r requirements.txt
EXPOSE 5001
CMD [ "python", "main.py" ]