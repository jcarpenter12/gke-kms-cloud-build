FROM python:3.6.9
RUN pip install pipenv
RUN mkdir app/
COPY Pipfile* /app/
RUN cd /app && pipenv lock --requirements > requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt
COPY main.py /app/
WORKDIR app/
CMD ["python", "-u", "main.py"]
EXPOSE 8080
