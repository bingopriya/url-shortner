FROM python:latest
WORKDIR /
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install fastapi uvicorn
COPY . /
EXPOSE 8000
CMD ["uvicorn", "main:app", "--reload",  "--host", "0.0.0.0", "--port", "8000"]
