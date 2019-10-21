#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn my_blog.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
