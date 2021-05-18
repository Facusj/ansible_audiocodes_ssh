FROM ubuntu:18.04

ENV TZ=America/Argentina/Buenos_Aires
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN sed -i'' 's/archive\.ubuntu\.com/us\.archive\.ubuntu\.com/' /etc/apt/sources.list
RUN apt update -y && \
    apt install -y apt-transport-https && \
    apt install python-pip -y && \
    apt install python3-pip -y && \
    apt install python-influxdb -y
RUN pip install pip --upgrade && \
    pip install ansible==2.9.1 && \
    pip install influxdb && \
    pip3 install influxdb && \
    pip install textfsm && \
    pip3 install textfsm && \
    pip install paramiko && \
    pip install netmiko==3.3.3

RUN apt install openssh-server -y && \
    apt install telnet -y && \
    apt install sshpass -y && \
    apt install cron -y && \
    apt install nano -y

WORKDIR /
RUN mkdir -p /code/telemetry/ansible/sbc

COPY /crontab/telemetry-cron /etc/cron.d/telemetry-cron
RUN crontab /etc/cron.d/telemetry-cron
CMD ["cron", "-f"]
