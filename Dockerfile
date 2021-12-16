FROM python:3.10-slim-bullseye
LABEL version="0.6.0" maintainer="morevi" repo="jobcontrol"

WORKDIR /app/test
COPY pyproject.toml ./

RUN useradd --create-home jb \
    && chown -R jb:jb /app/test
USER jb

ENV PATH="$PATH:/home/jb/.local/bin"
RUN pip install poetry \
    # docker already gives an isolated enviroment
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction

ENTRYPOINT ["inv", "test"] 
