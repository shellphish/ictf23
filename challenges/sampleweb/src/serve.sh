#!/bin/bash
gunicorn --log-level DEBUG -b 0.0.0.0:8080 app:app