import config
from monero.seed import Seed


def generate_wallets(_quantity, _net=None):
    if not _net:
        net = config.args.net
    else:
        net = _net

    wallets = []
    while _quantity > 0:
        try:
            wallet = Seed()
        except Exception as e:
            config.logger.error(f'unable to create wallet: \n {e}')
            return None

        wallet_dict = {
            "seed_phrase": wallet.phrase,
            "seed_hex": wallet.hex_seed(),
            "secret_spend_key": wallet.secret_spend_key(),
            "secret_view_key": wallet.secret_view_key(),
            "public_spend_key": wallet.public_spend_key(),
            "public_view_key": wallet.public_view_key(),
            "public_address": str(wallet.public_address(net=net))
        }

        config.logger.debug(wallet_dict)
        wallets.append(wallet_dict)
        _quantity -= 1
    config.logger.debug(f'{len(wallets)} {wallets}')
    return wallets
