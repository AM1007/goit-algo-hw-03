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
                recursive_copy(item, dst)
            else:
                folder = dst / item.name[:1]  
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

# # ANSI escape codes for colored output
# COLOR_BLUE = "\033[94m"
# COLOR_RESET = "\033[0m"

# def display_tree(path: Path, indent: str = "", prefix: str = "") -> None:
#     if path.is_dir():
#         # Use blue color for directories
#         print(indent + prefix + COLOR_BLUE + str(path.name) + COLOR_RESET)
#         indent += "    " if prefix else ""

#         # Get a sorted list of children, with directories last
#         children = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))

#         for index, child in enumerate(children):
#             # Check if the current child is the last one in the directory
#             is_last = index == len(children) - 1
#             display_tree(child, indent, "└── " if is_last else "├── ")
#     else:
#         print(indent + prefix + str(path.name))

# if __name__ == "__main__":
#     root = Path("picture")
#     display_tree(root)
