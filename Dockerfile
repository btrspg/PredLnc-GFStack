FROM ubuntu:18.04
MAINTAINER CHEN Yuelong <yuelong.chen.btr@gmail.com>


ARG depends="build-essential python3 python3-dev python3-pip"

RUN apt update && apt install -y $depends


WORKDIR /opt/tmp/
ADD . ./
RUN pip3 install -r requirements.txt && \
    pip3 install . && \
    cp src/txCdsPredict /usr/local/bin/ && \
    chmod +x /usr/local/bin/*



RUN rm -rf /opt/tmp/

