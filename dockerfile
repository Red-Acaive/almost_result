FROM python:3.8 as builder

# Setup working directory
WORKDIR /app
COPY . .

# Build
RUN python3 -m venv backend && . backend/bin/activate
RUN pip3 install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3", "-m", "flask", "run"]
CMD ["--host=0.0.0.0"]
