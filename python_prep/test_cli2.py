import argparse
from datetime import datetime

def ingest():
    print('Ingesting raw files for this pipeline')
    pass
    
def transform(*args):
    print('Tranforming loaded raw files for this pipeline')
    print(f'Arguments for transform: {args.start_date}')
    pass

def valid_date(date_str: str) -> str:
    print(f'converting date: {date_str} to YYYY-MM-DD format')
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        return date
    except ValueError:
        raise argparse.ArgumentTypeError(f'invalid date format {date_str} expected date format is  YYYY-MM-DD ')

def parse_config():
    parser =argparse.ArgumentParser(description='Setting up sub parsers')
    subparser = parser.add_subparsers(dest='command',required=True,description='creating subcommands for script to run in')

    ingest_subparser = subparser.add_parser('ingest',description='Ingest/ load raw files')
    ingest_subparser.add_argument('--file-path', required=True)

    transform_subparser =subparser.add_parser('transform', description='Transform file data')
    transform_subparser.add_argument('--conf',required=True)
    transform_subparser.add_argument('--start-date',type=valid_date,required=True,help='settig up custom type for the flag variable')

    args = parser.parse_args()
    
    if args.command == 'ingest':
        ingest(args)
    elif args.command == 'transform':
        transform(args)

if __name__ == '__main__':
    print('Starting pipelin')
    parse_config()