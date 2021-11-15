FROM python:3.8
WORKDIR /workspace/SE

COPY . .

RUN python3.8 build-system-script.py install-depends

EXPOSE 8000

CMD ["python3.8", "-m", "uvicorn", "main:app", "--reload"]
