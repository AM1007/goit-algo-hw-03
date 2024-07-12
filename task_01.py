import argparse
import shutil
from pathlib import Path


def parse_argv():
    parser = argparse.ArgumentParser("Image sorting")
    parser.add_argument( "-S", "--sourse", type=Path, required=True, help="Images directory")
    parser.add_argument( "-O", "--output", type=Path, default=Path("output"), help="Sorted images directory")
    return parser.parse_args()

def recursive_copy(src: Path, dst: Path):
    try:
        for item in src.iterdir():
            if item.is_dir():
                recursive_copy(item, dst / item.name)
            else:
                file_extension = item.suffix.lower()[1:]
                folder = dst / file_extension
                folder.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, folder)
    except (FileNotFoundError, PermissionError) as e:
        print(f"An error occurred: {e}")
    

def main():
    args = parse_argv()
    print(args)
    recursive_copy(args.sourse, args.output)

if __name__ == "__main__":
    main()


