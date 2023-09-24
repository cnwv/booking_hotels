#!/bin/bash

celery -A app.tasks.celery_app:celery worker --loglevel=INFO


