FROM python:latest

# add dependency file to the image
ADD pyproject.toml /app/pyproject.toml

WORKDIR /app/

RUN pip install -U setuptools pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction
