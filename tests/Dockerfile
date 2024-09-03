FROM python:3.12-alpine
RUN apk update && apk add kbd
COPY ../requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . .
CMD ["pytest /tests"]
