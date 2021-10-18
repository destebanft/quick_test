FROM python:3.7.7-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install packages needed to run your application (not build deps):
# We need to recreate the /usr/share/man/man{1..8} directories first because
# they were clobbered by a parent image.
RUN set -ex \
    && RUN_DEPS=" \
        postgresql-client \
    " \
    && seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{} \
    && apt-get update \
    && apt-get install -y --no-install-recommends $RUN_DEPS \
    && rm -rf /var/lib/apt/lists/*

# Install build deps, then run `pip install`, then remove unneeded build deps all in a single step.
COPY requirements.txt requirements.txt

RUN set -ex \
    && BUILD_DEPS=" \
        gcc \
        libpcre3-dev \
        libpq-dev \
    " \
    && apt-get update \
    && apt-get install -y --no-install-recommends $BUILD_DEPS \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
ARG APP_USER=django
RUN useradd -ms /bin/bash ${APP_USER}
WORKDIR /home/${APP_USER}/src

# Copy source code
COPY docker-entrypoint.sh .
RUN chmod +x docker-entrypoint.sh
COPY manage.py .
COPY api api


# Change to non-root user
USER ${APP_USER}

ENTRYPOINT ["sh","./docker-entrypoint.sh"]

CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5500", "api.wsgi:application"]
