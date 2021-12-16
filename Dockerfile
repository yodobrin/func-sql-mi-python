FROM mcr.microsoft.com/azure-functions/python:3.0-python3.9

RUN apt-get update \
 && apt-get install unixodbc -y \
 && apt-get install --reinstall build-essential -y

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
AzureFunctionsJobHost__Logging__Console__IsEnabled=true
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /home/site/wwwroot

