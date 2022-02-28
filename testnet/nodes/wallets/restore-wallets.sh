#!/bin/bash

monero-wallet-cli --testnet --generate-new-wallet ~/wallet_01.bin  --restore-deterministic-wallet \
--electrum-seed="sequence atlas unveil summon pebbles tuesday beer rudely snake rockets different fuselage woven tagged bested dented vegan hover rapid fawns obvious muppet randomly seasons randomly" \
--password "" --log-file ~/wallet_01.log

monero-wallet-cli --testnet --generate-new-wallet ~/wallet_02.bin  --restore-deterministic-wallet \
--electrum-seed="deftly large tirade gumball android leech sidekick opened iguana voice gels focus poaching itches network espionage much jailed vaults winter oatmeal eleven science siren winter" \
--password "" --log-file ~/wallet_02.log

monero-wallet-cli --testnet --generate-new-wallet ~/wallet_03.bin  --restore-deterministic-wallet \
--electrum-seed="upstairs arsenic adjust emulate karate efficient demonstrate weekday kangaroo yoga huts seventh goes heron sleepless fungal tweezers zigzags maps hedgehog hoax foyer jury knife karate" \
--password "" --log-file ~/wallet_03.log

monero-wallet-cli --testnet --generate-new-wallet ~/wallet_04.bin  --restore-deterministic-wallet \
--electrum-seed="zigzags lodge giddy narrate toffee efficient washing paper betting obliged plywood upgrade broken afar mews agile younger dedicated rumble irony fences mocked budget useful younger" \
--password "" --log-file ~/wallet_04.log