import argparse
import os


def parser():
    aparse = argparse.ArgumentParser(
        prog="Python Functions updater",
        description="Update the version in the program",
    )
    aparse.add_argument("version")
    return aparse.parse_args()


os.system(f"python ModuleUploader/Updater.py {parser().version}")
os.system("python ModuleUploader/Uploader.py")
os.system("python ModuleUploader/DocCreator.py")
