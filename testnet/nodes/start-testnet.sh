#!/bin/bash -x

# first time running
if [ ! -d ~/testnet ]
then
  mkdir ~/testnet && cd ~/testnet
fi

# start nodes
monerod --config-file /src/testnet/node-1.conf --detach
monerod --config-file /src/testnet/node-2.conf --detach
monerod --config-file /src/testnet/node-3.conf --detach

# start xmrblocks
cd /src/onion-monero-blockchain-explorer/build
xmrblocks -t -p 9999 -b ~/testnet/node_01/testnet/lmdb/ --no-blocks-on-index 50 --enable-as-hex  --enable-pusher > /dev/null 2>&1 &

tail -f /root/testnet/node_01/testnet/bitmonero.log \
        /root/testnet/node_02/testnet/bitmonero.log \
        /root/testnet/node_03/testnet/bitmonero.log
