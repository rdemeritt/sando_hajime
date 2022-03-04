# deployment image
FROM monero-node:latest

USER monero

# Switch to home directory and install newly built xrmblocks binary
WORKDIR /home/monero

RUN mkdir wallets && \
    chown monero:monero wallets

# Start monero-wallet-rpc
ENTRYPOINT ["monero-wallet-rpc"]
CMD ["--testnet", "--rpc-bind-port", "28088", "--wallet-dir", "/home/monero/wallets", "--disable-rpc-login", \
     "--rpc-bind-ip", "0.0.0.0", "--confirm-external-bind", "--daemon-address", "http://node-1:28081", \
     "--log-level", "1"]
