FROM python:3.10-slim

WORKDIR /usr/src/thousandsunny

# Copiando APP para Container
COPY . .

RUN python3 -m pip install boto3 flask

#expondo porta da api-Flask
EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["api/app.py"]