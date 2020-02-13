FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /${dockerimage}
WORKDIR /${dockerimage}
ADD . /${dockerimage}/
RUN pip3 install --upgrade pip
RUN pip3 install pipenv
ONBUILD COPY Pipfile Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock
RUN pipenv install --deploy --ignore-pipfile
RUN pipenv update
EXPOSE 5000
CMD ["pipenv", "run", "python3", "wsgi.py"]
