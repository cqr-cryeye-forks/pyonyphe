import json
from argparse import ArgumentParser

from onyphe import Onyphe


def cli(parser: ArgumentParser):
    parser.add_argument(
        "-k", "--api-key",
        required=True,
        dest="api_key",
        type=str,
    )
    parser.add_argument(
        "-i", "--ip",
        required=True,
        type=str,
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="output.json"
    )
    return parser.parse_args()


def run(api_key: str, ip: str):
    on_client = Onyphe(api_key)
    try:
        return on_client.summary_ip(ip).get('results', [])
    except Exception as e:
        return []


def main():
    parser = ArgumentParser()
    args = cli(parser)
    output = run(args.api_key, args.ip)
    with open(args.output, 'w', encoding='utf8') as f:
        json.dump(output, f, ensure_ascii=False)


if __name__ == '__main__':
    main()
