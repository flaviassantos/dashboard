#!/bin/sh
# this script is used to boot a Docker container

source venv/bin/activate

# It takes a few seconds for this container to be fully running and ready to
# accept database connections. Therefore, the retry loop is there to make the
# solution robust.

while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done
exec gunicorn -b :5000 --access-logfile - --error-logfile - dashboard:app