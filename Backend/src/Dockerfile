FROM python:alpine3.7 
RUN mkdir -p /backend
COPY . /backend
WORKDIR /backend
RUN pip install -r requirements.txt 
EXPOSE 5002
ENTRYPOINT [ "python" ] 
CMD [ "main.py" ] 