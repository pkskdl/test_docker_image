FROM python:3
WORKDIR /workspace
COPY cleanup.py /workspace

ENTRYPOINT ["python", "./cleanup.py"]
