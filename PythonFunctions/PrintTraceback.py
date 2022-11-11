import traceback
import os

def PrintTraceback():
    dash = "-" * os.get_terminal_size().columns
    
    print(f'\033[41m{dash}')
    traceback.print_exc()
    print(f'{dash}\033[0m')

if __name__ == "__main__":
    PrintTraceback()