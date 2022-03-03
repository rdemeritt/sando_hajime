FROM monero-builder:latest as builder

# deployment image
FROM monero-node:latest

USER monero

# Switch to home directory and install newly built xrmblocks binary
WORKDIR /home/monero
COPY --chown=monero:monero --from=builder /src/monero/build/Linux/release-v0.17/release/bin/monero-wallet-rpc .
RUN mkdir wallets && \
    chown monero:monero wallets

# Start monerod
#ENTRYPOINT ["./xmrblocks"]
#CMD ["-p 9999"]
ENTRYPOINT ["monero-wallet-rpc"]
CMD ["--testnet", "--rpc-bind-port", "28088", "--wallet-dir", "/home/monero/wallets", "--disable-rpc-login", \
     "--rpc-bind-ip", "0.0.0.0", "--confirm-external-bind", "--daemon-address", "http://node-1:28081", \
     "--log-level", "1"]
