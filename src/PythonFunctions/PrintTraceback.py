"""Prints the traceback if an error is caught from an try except statement"""
import os
import traceback


def PrintTraceback():
    """Prints the traceback in a foramated way"""
    dash = "-" * os.get_terminal_size().columns

    print(f"\033[41m{dash}")
    traceback.print_exc()
    print(f"{dash}\033[0m")


if __name__ == "__main__":
    PrintTraceback()
