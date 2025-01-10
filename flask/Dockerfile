FROM python:3.12.6-alpine

# upgrade pip
RUN pip install --upgrade pip

# get curl for healthchecks
RUN apk add curl

# permissions and nonroot user for tightened security
RUN adduser -D nonroot
RUN mkdir /blog/ && chown -R nonroot:nonroot /blog
RUN mkdir -p /var/log/flask-app && touch /var/log/flask-app/flask-app.err.log && touch /var/log/flask-app/flask-app.out.log
RUN chown -R nonroot:nonroot /var/log/flask-app
WORKDIR /blog
USER nonroot

# venv
ENV VIRTUAL_ENV=/blog/venv

# python setup
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY --chown=nonroot:nonroot ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
RUN export FLASK_APP=app.py

# copy all the files to the container
COPY --chown=nonroot:nonroot app /blog/app

CMD ["python", "app.py"]