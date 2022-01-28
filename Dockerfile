FROM quay.io/fedora/fedora:36-x86_64
RUN dnf -y install kiwix-tools findutils wget && dnf -y update && dnf clean all
EXPOSE 80
VOLUME /data
WORKDIR /data
COPY ./start.sh /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/start.sh"]
