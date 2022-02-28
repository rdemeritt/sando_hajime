# build image
FROM monero-builder:latest as builder

# build xmrblocks
WORKDIR /src
RUN git clone https://github.com/moneroexamples/onion-monero-blockchain-explorer.git && \
    mkdir onion-monero-blockchain-explorer/build && \
    cd onion-monero-blockchain-explorer/build && \
    cmake -DMONERO_DIR=/src/monero -DMONERO_BUILD_DIR=/src/monero/build/Linux/release-v0.17/release .. && \
    make -j 6

# deployment image
FROM monero-node:latest

# Install remaining dependencies
USER root
RUN apt-get update && \
    apt-get install --no-install-recommends -y libunwind8-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add user
#RUN useradd -ms /bin/bash monero && \
USER monero

# Switch to home directory and install newly built xrmblocks binary
WORKDIR /home/monero
COPY --chown=monero:monero --from=builder /src/onion-monero-blockchain-explorer/build/xmrblocks .
COPY --chown=monero:monero --from=builder /src/onion-monero-blockchain-explorer/build/templates ./templates/

# Start monerod
#ENTRYPOINT ["./xmrblocks"]
#CMD ["-p 9999"]
ENTRYPOINT ["/bin/sh", "-cx"]
CMD ["./xmrblocks --enable-json-api --enable-autorefresh-option  --enable-pusher"]
