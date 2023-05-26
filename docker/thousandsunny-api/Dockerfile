FROM python:3.9-slim

WORKDIR /usr/src/thousandsunny

# Copiando APP para Container
COPY . .

RUN apt-get update && apt-get install -y python3-dev bash vim curl telnet htop wget \
    && pip3 install --upgrade pip

RUN python3 -m pip install boto3 flask

RUN apt-get update && apt-get install -y bash vim curl telnet htop wget

#expondo porta da api-Flask
EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["api/app.py"]