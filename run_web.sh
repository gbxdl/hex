#!/bin/sh

gunicorn web:app -w 1 --threads 1 --timeout 180 -b 0.0.0.0:7000
