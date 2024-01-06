FROM fedora:39

USER root

RUN sed -e 's|^metalink=|#metalink=|g' \
         -e 's|^#baseurl=http://download.example/pub/fedora/linux|baseurl=https://mirrors.ustc.edu.cn/fedora|g' \
         -i.bak \
         /etc/yum.repos.d/fedora.repo \
         /etc/yum.repos.d/fedora-updates.repo

RUN dnf up -y \
    && dnf -y in automake autoconf make binutils glibc-devel pkgconf ccache \
    gcc gcc-c++ clang ccache cmake ninja-build lld rustup \
    python3-pip git \
    && dnf autoremove \
    && dnf clean all

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install --no-cache-dir 'buildbot[bundle]'

ENV USER_NAME fedora_worker
ENV DATA_DIR /data

ENV UID 1000

# RUN groupmod -g ${DOCKER_GID} docker \
RUN useradd -u ${UID} -s /bin/bash ${USER_NAME} -U -d ${DATA_DIR}

RUN chown ${USER_NAME}:${USER_NAME} /data -R

USER ${USER_NAME}

WORKDIR ${DATA_DIR}

CMD ["twistd", "--pidfile=", "-ny", "/data/buildbot/buildbot.tac"]
