#!/bin/bash -x

# first time running and do we have wallets
if [ ! -d ~/testnet ]
then
  mkdir ~/testnet && cd ~/testnet

  monero-wallet-cli --testnet --generate-new-wallet ~/testnet/wallet_01.bin  --restore-deterministic-wallet \
  --electrum-seed="sequence atlas unveil summon pebbles tuesday beer rudely snake rockets different fuselage woven tagged bested dented vegan hover rapid fawns obvious muppet randomly seasons randomly" \
  --password "" --log-file ~/testnet/wallet_01.log

  monero-wallet-cli --testnet --generate-new-wallet ~/testnet/wallet_02.bin  --restore-deterministic-wallet \
  --electrum-seed="deftly large tirade gumball android leech sidekick opened iguana voice gels focus poaching itches network espionage much jailed vaults winter oatmeal eleven science siren winter" \
  --password "" --log-file ~/testnet/wallet_02.log

  monero-wallet-cli --testnet --generate-new-wallet ~/testnet/wallet_03.bin  --restore-deterministic-wallet \
  --electrum-seed="upstairs arsenic adjust emulate karate efficient demonstrate weekday kangaroo yoga huts seventh goes heron sleepless fungal tweezers zigzags maps hedgehog hoax foyer jury knife karate" \
  --password "" --log-file ~/testnet/wallet_03.log;
fi

# start nodes
monerod --testnet --no-igd --hide-my-port --data-dir ~/testnet/node_01 --p2p-bind-ip 127.0.0.1 --log-level 0 \
        --add-exclusive-node 127.0.0.1:38080 --add-exclusive-node 127.0.0.1:48080 --fixed-difficulty 100 \
        --start-mining 9wviCeWe2D8XS82k2ovp5EUYLzBt9pYNW2LXUFsZiv8S3Mt21FZ5qQaAroko1enzw3eGr9qC7X1D7Geoo2RrAotYPwq9Gm8 \
        --detach

monerod --testnet --p2p-bind-port 38080 --rpc-bind-port 38081 --zmq-rpc-bind-port 38082 --no-igd --hide-my-port  \
        --log-level 0 --data-dir ~/testnet/node_02 --p2p-bind-ip 127.0.0.1 --add-exclusive-node 127.0.0.1:28080 \
        --add-exclusive-node 127.0.0.1:48080 --fixed-difficulty 100 --detach \
        --start-mining 9wviCeWe2D8XS82k2ovp5EUYLzBt9pYNW2LXUFsZiv8S3Mt21FZ5qQaAroko1enzw3eGr9qC7X1D7Geoo2RrAotYPwq9Gm8

monerod --testnet --p2p-bind-port 48080 --rpc-bind-port 48081 --zmq-rpc-bind-port 48082 --no-igd --hide-my-port  \
        --log-level 0 --data-dir ~/testnet/node_03 --p2p-bind-ip 127.0.0.1 --add-exclusive-node 127.0.0.1:28080 \
        --add-exclusive-node 127.0.0.1:38080 --fixed-difficulty 100 --detach \
        --start-mining 9wviCeWe2D8XS82k2ovp5EUYLzBt9pYNW2LXUFsZiv8S3Mt21FZ5qQaAroko1enzw3eGr9qC7X1D7Geoo2RrAotYPwq9Gm8


