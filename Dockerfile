FROM python:3.9.6-alpine


WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN python -m pip install --upgrade pip setuptools pipenv && \
    pipenv install --system --ignore-pipfile && \
    rm -f Pipfile Pipfile.lock

COPY project/ project/

EXPOSE 8000/tcp

ENTRYPOINT [ "gunicorn", "project.wsgi", "--config=project/gunicorn.conf.py" ]
