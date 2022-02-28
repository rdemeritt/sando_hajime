#!/bin/bash

monero-wallet-cli --testnet --trusted-daemon --wallet-file ~/testnet/wallet_0$1.bin --password '' \
                  --log-file ~/testnet/wallet_0$1.log
