import argparse


from blackjack.server import BlackjackServer
from blackjack.client import BlackjackClient


def get_parser():  # pragma: no coverage
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="cmd")

    server = subparsers.add_parser("serve", description="Start a blackjack game server")
    client = subparsers.add_parser("join", description="Join a Blackjack server")

    client.add_argument("server", type=str, help="The server to join")

    return parser


def main():
    parser = get_parser()
    options = parser.parse_args()
    if not options.cmd:
        parser.print_help()

    if options.cmd == 'serve':
        with BlackjackServer() as server:
            server.serve_forever()

    if options.cmd == 'join':
        BlackjackClient(options.server).run()


