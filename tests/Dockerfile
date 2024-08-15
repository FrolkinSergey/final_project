FROM python:3.12-alpine
COPY ../requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x /wait-for-it.sh
CMD ["pytest /tests"]
