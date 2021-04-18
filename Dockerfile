FROM python:3-alpine
RUN pip install flask
WORKDIR /usr/app/
COPY . .
EXPOSE 3030
CMD ["python","/usr/app/app.py"]
