FROM python:3.11

ENV PYTHONUNBUFFERED True \
    APP_HOME /app \
    POETRY_VIRTUALENVS_CREATE false



RUN apt-get update && apt-get install -y curl poppler-utils git openssh-client

WORKDIR $APP_HOME

ENV PATH="/root/.local/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -  && poetry config virtualenvs.create false

COPY pyproject.toml ./

#RUN poetry install --without dev
RUN poetry install --no-root

COPY ./slides_llm ./slides_llm

CMD exec uvicorn slides_llm.main:app --host 0.0.0.0 --port ${PORT} --workers 1
