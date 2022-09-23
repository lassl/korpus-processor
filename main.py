import os
import warnings
from argparse import ArgumentParser
from pathlib import Path
from typing import List


project_path = Path(__file__).parent.resolve()
SUPPORTED_EXTENSION = [".txt"]


def get_args():
    parser = ArgumentParser()
    parser.add_argument("--file_dir", type=str, required=True)
    parser.add_argument("--task", type=str, choices=["cleanse", "filter"], required=True)
    parser.add_argument("--overwrite", type=bool, required=True)
    parser.add_argument("--output_dir", default=None, type=str, required=False)
    parser.add_argument("--filter_type", default="jaccard", type=str, choices=["jaccard", "lsh", "plm-embed"], required=False)
    parser.add_argument("--filter_ratio", default=0.15, type=float, required=False)
    args = parser.parse_args()
    return args


def get_all_file_path(base_path: str) -> List[str]:
    all_file_path = []
    for path in os.listdir(base_path):
        path = os.path.join(base_path, path)
        if os.path.isdir(path):
            all_file_path.extend(get_all_file_path(path))
        else:
            for ext in SUPPORTED_EXTENSION:
                if path.endswith(ext):
                    all_file_path.append(path)
    return all_file_path


def main():
    args = get_args()
    if args.overwrite:
        warnings.warn("All the files in sub-directories would be overwritten")
        if input("Proceed [y/n]: ").lower() == "n":
            print("Set overwrite argument to <False>")
            return
        assert args.output_dir, "output_dir argument must be included"
        
    file_path: List[str] = get_all_file_path(args.file_dir)
    # TODO: task operate lines below
    if args.task:
        pass
    else:
        pass
    
    


if __name__ == "__main__":
    main()