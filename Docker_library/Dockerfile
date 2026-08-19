FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY 03_Library_Systembook.csv /app

COPY library_data_cleaning.py /app
ENTRYPOINT ["python3", "library_data_cleaning.py"]