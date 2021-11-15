FROM python:3.8
WORKDIR /workspace/SE

RUN apt-get update && apt-get install git
RUN git clone https://github.com/DF5HSE/SE2021Practice.git

WORKDIR /workspace/SE/SE2021Practice
RUN python3.8 build-system-script.py install-depends

CMD ["python3.8", "build-system-script.py", "test"]
