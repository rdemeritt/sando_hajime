# build image
FROM monero-builder:latest as builder

#WORKDIR /src
#
#RUN cd monero &&  \
#    git checkout release-v0.17 && \
#    git submodule update --init --force && \
#    make -j 6 release

# deployment image
FROM ubuntu:20.04

# Install remaining dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y curl libnorm-dev libpgm-dev libgssapi-krb5-2 libboost-chrono-dev \
                libboost-date-time-dev libboost-filesystem-dev libboost-locale-dev  \
                libboost-program-options-dev libboost-regex-dev libboost-serialization-dev  \
                libboost-system-dev libboost-thread-dev libzmq3-dev libreadline6-dev libhidapi-dev libunbound-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add user and setup directories for monerod
RUN useradd -ms /bin/bash monero && \
    mkdir -p /home/monero/.bitmonero && \
    chown -R monero:monero /home/monero/.bitmonero
USER monero

# Switch to home directory and install newly built monerod binary
WORKDIR /home/monero
COPY --chown=monero:monero --from=builder /src/monero/build/Linux/release-v0.17/release/bin /usr/local/bin

# copy node config files to running host
COPY --chown=monero:monero *.conf /home/monero/

# Add HEALTHCHECK against get_info endpoint
HEALTHCHECK --interval=30s --timeout=5s CMD curl --fail http://localhost:28081/get_info || exit 1

# Start monerod
ENTRYPOINT ["monerod", "--non-interactive"]
CMD ["--config-file", "node.conf"]
