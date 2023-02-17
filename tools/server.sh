#!/bin/bash
source /opt/eldertek/scovie/virtualenv/bin/activate
cd /opt/eldertek/scovie
gunicorn --workers 3 --bind unix:/tmp/scovie.sock scovie.wsgi