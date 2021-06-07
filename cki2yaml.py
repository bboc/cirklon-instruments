import argparse
import json
import yaml


def json2yaml(source, target):
    with open(source, 'r') as infile:
        data = json.load(infile)
    with open(target, 'w') as outfile:
        yaml.dump(data, outfile, allow_unicode=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert CKI file to YAML.')

    parser.add_argument('source',
                        help="source filename (CKI)")
    parser.add_argument('target',
                        help="target filename (YAML")
    args = parser.parse_args()
    json2yaml(args.source, args.target)
