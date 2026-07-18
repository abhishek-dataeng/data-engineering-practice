import argparse
from dataclasses import dataclass

@dataclass
class SalesPipelineConfig:
    input_file: str
    filepath: str
    batch_size: int
    dry_run: bool
    log_level: str

def main():
    parser = argparse.ArgumentParser(description="process daily sales data")
    parser.add_argument('--input-file',type=str,required=True,help='Sales input file')
    parser.add_argument('--filepath',type=str,required=True,help='filepath for sales file')
    parser.add_argument('--batch-size',type=int,default=1000,help='process no of rows at a time')
    parser.add_argument('--dry-run',action='store_true',help='run without writing output')
    parser.add_argument('--log-level',choices=['INFO','DEBUG','WARNING','ERROR','CRITICAL'],default='INFO',
                        help='logging level')
    args = parser.parse_args()

    config = SalesPipelineConfig(**vars(args))

    print(f"Inside test_cli function, module name is: {__name__}")

    # print(f'Printing flags from parser:\n {args}')
    # print(f'Printing configs for dataclass:\n {config}')
    # # print(args.input_file,args.filepath,args.batch_size,args.log_level,args.dry_run,args.log_level)

    # # Now you have full IDE autocomplete and type safety!
    # print(f"✅ Secure Dataclass Object Built Successfully!")
    # print(f"Target file: {config.input_file}")
    # print(f"Batch settings: {config.batch_size} rows per loop")

if __name__ == '__main__':
    main()
