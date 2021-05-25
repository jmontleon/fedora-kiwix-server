FROM quay.io/fedora/fedora:34-x86_64 as builder
RUN dnf -y install dnf-plugins-core
RUN dnf -y download --source kiwix-tools
RUN rpm -ivh ./kiwix-tools*
ADD zimlib.spec /root/rpmbuild/SPECS/zimlib.spec
ADD kiwix-lib.spec /root/rpmbuild/SPECS/kiwix-lib.spec
ADD 537.patch /root/rpmbuild/SOURCES/537.patch
RUN dnf build-dep -y /root/rpmbuild/SPECS/zimlib.spec \
                     /root/rpmbuild/SPECS/kiwix-lib.spec \
                     /root/rpmbuild/SPECS/kiwix-tools.spec
RUN dnf -y install wget rpm-build
WORKDIR /root/rpmbuild/SOURCES
RUN wget https://github.com/openzim/libzim/archive/refs/heads/master.zip
RUN unzip master.zip && rm -f master.zip
RUN mv libzim-master libzim-7.0.0
RUN tar zcvf 7.0.0.tar.gz libzim-7.0.0
RUN wget https://github.com/kiwix/libkiwix/archive/refs/heads/master.zip
RUN unzip master.zip && rm -f master.zip
RUN mv libkiwix-master kiwix-lib-10.0.0
RUN tar zcvf kiwix-lib-10.0.0.tar.gz kiwix-lib-10.0.0
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
RUN dnf -y install ./*.rpm wget && dnf clean all
EXPOSE map[80/tcp:{}]
VOLUME [/data]
WORKDIR /data
COPY ./start.sh /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/start.sh"]
