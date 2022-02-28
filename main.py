import json
import config
from wallet_actions import generate_wallets


def main():
    print(json.dumps(generate_wallets(10), indent=4))


# kick off the whole thing
if __name__ == '__main__':
    config.init()
    config.logger.info('Starting')
    main()
