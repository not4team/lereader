#!/bin/bash
pipenv run gunicorn -c owllook/config/gunicorn.py --worker-class sanic.worker.GunicornWorker owllook.server:app
