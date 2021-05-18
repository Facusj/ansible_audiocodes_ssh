#!/bin/bash

if [ ! -f /code/telemetry/ansible/sbc/scripts/SSH.pyc ]; then
    cd /code/telemetry/ansible/sbc/scripts
    /usr/bin/python3 -m py_compile /code/telemetry/ansible/sbc/scripts/SSH_calls.py
    mv /code/telemetry/ansible/sbc/scripts/__pycache__/SSH_calls.cpython-36.pyc /code/telemetry/ansible/sbc/scripts/SSH_calls.pyc
fi

cd /code/telemetry/ansible/sbc

/usr/bin/python3 /code/telemetry/ansible/sbc/scripts/newcos-calls.py >> /code/telemetry/ansible/sbc/log/cron.log &

exit 0
