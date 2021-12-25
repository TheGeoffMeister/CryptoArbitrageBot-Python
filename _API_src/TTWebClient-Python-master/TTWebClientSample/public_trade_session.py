#!/usr/bin/python3
__author__ = 'ivan.shynkarenka'


import argparse
from TTWebClient.TickTraderWebClient import TickTraderWebClient


def main():
    parser = argparse.ArgumentParser(description='TickTrader Web API sample')
    parser.add_argument('web_api_address', help='TickTrader Web API address')
    args = parser.parse_args()

    # Create instance of the TickTrader Web API client
    client = TickTraderWebClient(args.web_api_address)

    # Public trade session status
    public_trade_session = client.get_public_trade_session()
    print('TickTrader name: {0}'.format(public_trade_session['PlatformName']))
    print('TickTrader company: {0}'.format(public_trade_session['PlatformCompany']))
    print('TickTrader address: {0}'.format(public_trade_session['PlatformAddress']))
    print('TickTrader timezone offset: {0}'.format(public_trade_session['PlatformTimezoneOffset']))
    print('TickTrader session status: {0}'.format(public_trade_session['SessionStatus']))


if __name__ == '__main__':
    main()