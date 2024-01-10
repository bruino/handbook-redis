FROM python:3.8
RUN pip install pipx
RUN pipx install poetry==1.2.2
ENV PATH="${PATH}:/root/.local/bin"

# COPY . .
COPY ./pyproject.toml /app/pyproject.toml
COPY ./sensor-generator.py /app/sensor-generator.py

WORKDIR /app
RUN poetry install
