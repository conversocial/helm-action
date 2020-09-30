FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y git curl python3 python3-pip && \
    pip3 install pyyaml && \
    curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash && \
    helm plugin install https://github.com/quintush/helm-unittest --version 0.2.3

COPY helm-repo-add.py /helm-repo-add.py

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
