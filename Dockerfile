FROM quay.io/fedora/fedora:34-x86_64 as builder
RUN dnf -y install dnf-plugins-core
RUN dnf -y download --source kiwix-tools
RUN rpm -ivh ./kiwix-tools*
ADD zimlib.spec /root/rpmbuild/SPECS/zimlib.spec
ADD kiwix-lib.spec /root/rpmbuild/SPECS/kiwix-lib.spec
RUN dnf build-dep -y /root/rpmbuild/SPECS/zimlib.spec \
                     /root/rpmbuild/SPECS/kiwix-lib.spec \
                     /root/rpmbuild/SPECS/kiwix-tools.spec
RUN dnf -y install wget rpm-build
WORKDIR /root/rpmbuild/SOURCES
RUN wget https://github.com/openzim/libzim/archive/6971bcf8d292a46b02c38e7cb5565ae0fb7fc5f1.zip
RUN unzip 6971bcf8d292a46b02c38e7cb5565ae0fb7fc5f1.zip && rm -f 6971bcf8d292a46b02c38e7cb5565ae0fb7fc5f1.zip
RUN mv libzim-6971bcf8d292a46b02c38e7cb5565ae0fb7fc5f1 libzim-7.0.0
RUN tar zcvf 7.0.0.tar.gz libzim-7.0.0
RUN wget https://github.com/kiwix/libkiwix/archive/refs/heads/master.zip
RUN unzip master.zip && rm -f master.zip
RUN mv libkiwix-master kiwix-lib-10.0.0
RUN tar zcvf kiwix-lib-10.0.0.tar.gz kiwix-lib-10.0.0
RUN wget https://github.com/kiwix/kiwix-tools/archive/refs/heads/master.zip
RUN unzip master.zip && rm -f master.zip
RUN mv kiwix-tools-master kiwix-tools-3.1.2
RUN tar zcvf kiwix-tools-3.1.2.tar.gz kiwix-tools-3.1.2
WORKDIR /root/rpmbuild/SPECS
RUN rpmbuild -bb zimlib.spec
RUN dnf -y install /root/rpmbuild/RPMS/x86_64/zimlib-devel-7* \
                   /root/rpmbuild/RPMS/x86_64/zimlib-7* \
                   --best --allowerasing
RUN rpmbuild -bb kiwix-lib.spec
RUN dnf -y install /root/rpmbuild/RPMS/x86_64/kiwix-lib-devel-10* \
                   /root/rpmbuild/RPMS/x86_64/kiwix-lib-10*
RUN rpmbuild -bb kiwix-tools.spec

FROM quay.io/fedora/fedora:34-x86_64
COPY --from=builder /root/rpmbuild/RPMS/x86_64/kiwix-lib-10* .
COPY --from=builder /root/rpmbuild/RPMS/x86_64/kiwix-tools-3* .
COPY --from=builder /root/rpmbuild/RPMS/x86_64/zimlib-7* .
RUN dnf -y install ./*.rpm wget && dnf -y update && dnf clean all
EXPOSE 80
VOLUME [/data]
WORKDIR /data
COPY ./start.sh /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/start.sh"]
