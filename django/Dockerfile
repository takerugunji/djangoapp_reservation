FROM django2.1:latest

ENV APP_PATH /opt/apps

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . $APP_PATH/
RUN pip install --no-cache-dir -r $APP_PATH/requirements.txt

WORKDIR $APP_PATH
RUN python manage.py collectstatic --noinput