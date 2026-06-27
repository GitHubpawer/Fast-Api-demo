FROM python:3.9-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /src


RUN pip install poetry

COPY pyproject.toml poetry.lock ./

# ←重要
RUN poetry config virtualenvs.create false

RUN poetry install --no-root

COPY . .

ENTRYPOINT ["uvicorn","api.main:app","--host","0.0.0.0","--port","8000","--reload"]