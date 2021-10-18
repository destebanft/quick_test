#!/bin/bash

echo "Container started!"

python manage.py collectstatic --no-input
python manage.py migrate --no-input

exec "$@"
