FROM python:latest

# add dependency file to the image
ADD pyproject.toml /app/pyproject.toml

WORKDIR /app/

EXPOSE 5001
EXPOSE 6379

RUN pip install -U setuptools pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction
