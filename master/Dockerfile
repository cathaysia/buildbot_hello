FROM python:3.11

USER root

RUN sed -e 's#http://deb.debian.org/debian-security#https://mirrors.tuna.tsinghua.edu.cn/debian-security/#' /etc/apt/sources.list.d/debian.sources -i \
    && sed -e 's#http://deb.debian.org/debian#https://mirrors.tuna.tsinghua.edu.cn/debian/#' /etc/apt/sources.list.d/debian.sources -i

RUN apt-get update -y \
    && apt-get install -y docker.io dumb-init\
    && apt-get autoremove \
    && apt-get clean

COPY requirements.txt /opt/requirements.txt

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install --no-cache-dir -r /opt/requirements.txt

ENV USER_NAME build_master
ENV DATA_DIR /data
ENV UID 1000
# ENV DOCKER_GID 120

# RUN groupmod -g ${DOCKER_GID} docker \
RUN useradd -u ${UID} -s /bin/bash ${USER_NAME} -U -d ${DATA_DIR} \
    && gpasswd -a ${USER_NAME} docker

COPY ./start_buildbot.sh /data/
RUN chown ${USER_NAME}:${USER_NAME} /data -R \
    && chmod +x /data/start_buildbot.sh

USER ${USER_NAME}

WORKDIR ${DATA_DIR}

CMD ["dumb-init", "/data/start_buildbot.sh"]
