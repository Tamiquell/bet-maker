FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update \
    && apt-get --yes --no-install-recommends install \
    python3 python3-dev

RUN pip install --upgrade pip
RUN pip install poetry

COPY pyproject.toml .

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi



EXPOSE 8085

COPY . .

RUN chmod a+x /app/docker/*.sh


WORKDIR /app/src 

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
