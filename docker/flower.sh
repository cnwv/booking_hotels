#!/bin/bash

celery -A app.tasks.celery_app:celery flower --loglevel=INFO



