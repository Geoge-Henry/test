FROM centos
LABEL maintainer="czh@us.meitu.com"
LABEL version=1.0.0
ENV APP_HOME /opt/chat_bot
ENV API_HOME ${APP_HOME}/api
ENV PYTHONUNBUFFERED 1
ENV LANG en_US.UTF-8
COPY . ${APP_HOME}
WORKDIR ${APP_HOME}
RUN set -x \
    && yum -y install \
        gcc \
        gcc-c++ \
        epel-release \
        mysql-devel \
    && yum -y install \
        python36 \
        python36-devel \
        python36-pip \
    && ln -sf /usr/bin/python3.6 /usr/bin/python \
    && ln -sf /usr/bin/pip3.6 /usr/bin/pip \
    && pip install -r requirement.txt
WORKDIR ${API_HOME}
EXPOSE 5000
CMD ["python", "app.py"]
