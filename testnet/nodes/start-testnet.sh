#!/bin/bash -x

# first time running
if [ ! -d ~/testnet ]
then
  mkdir ~/testnet && cd ~/testnet
fi

# start nodes
monerod --testnet --no-igd --hide-my-port --data-dir ~/testnet/node_01 --p2p-bind-ip 127.0.0.1 --log-level 0 \
        --add-exclusive-node 127.0.0.1:38080 --add-exclusive-node 127.0.0.1:48080 --fixed-difficulty 100 \
        --start-mining 9wq792k9sxVZiLn66S3Qzv8QfmtcwkdXgM5cWGsXAPxoQeMQ79md51PLPCijvzk1iHbuHi91pws5B7iajTX9KTtJ4bh2tCh \
        --detach

monerod --testnet --p2p-bind-port 38080 --rpc-bind-port 38081 --zmq-rpc-bind-port 38082 --no-igd --hide-my-port  \
        --log-level 0 --data-dir ~/testnet/node_02 --p2p-bind-ip 127.0.0.1 --add-exclusive-node 127.0.0.1:28080 \
        --add-exclusive-node 127.0.0.1:48080 --fixed-difficulty 100 --detach \
        --start-mining 9wq792k9sxVZiLn66S3Qzv8QfmtcwkdXgM5cWGsXAPxoQeMQ79md51PLPCijvzk1iHbuHi91pws5B7iajTX9KTtJ4bh2tCh

monerod --testnet --p2p-bind-port 48080 --rpc-bind-port 48081 --zmq-rpc-bind-port 48082 --no-igd --hide-my-port  \
        --log-level 0 --data-dir ~/testnet/node_03 --p2p-bind-ip 127.0.0.1 --add-exclusive-node 127.0.0.1:28080 \
        --add-exclusive-node 127.0.0.1:38080 --fixed-difficulty 100 --detach \
        --start-mining 9wviCeWe2D8XS82k2ovp5EUYLzBt9pYNW2LXUFsZiv8S3Mt21FZ5qQaAroko1enzw3eGr9qC7X1D7Geoo2RrAotYPwq9Gm8

# start xmrblocks
cd /src/onion-monero-blockchain-explorer/build
xmrblocks -t -p 9999 -b ~/testnet/node_01/testnet/lmdb/ --no-blocks-on-index 50 --enable-as-hex  --enable-pusher > /dev/null 2>&1 &

tail -f /root/testnet/node_01/testnet/bitmonero.log \
        /root/testnet/node_02/testnet/bitmonero.log \
        /root/testnet/node_03/testnet/bitmonero.log
