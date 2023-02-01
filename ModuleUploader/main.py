import argparse
import os


def parser():
    ARGparser = argparse.ArgumentParser(
        prog="Python Functions updater",
        description="Update the version in the program",
    )
    ARGparser.add_argument("version")
    return ARGparser.parse_args()


os.system(f"python ModuleUploader/Updater.py {parser().version}")
os.system("python ModuleUploader/Uploader.py")
