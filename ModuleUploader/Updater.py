import argparse


def parser():
    ARGparser = argparse.ArgumentParser(
        prog="Python Functions updater",
        description="Update the version in the program",
    )
    ARGparser.add_argument("version")
    return ARGparser.parse_args()


def main():
    version = parser().version
    print(f"Updating to {version}")

    print("Updating Version.txt")
    with open("Version.txt", "w", encoding="utf-8") as f:
        f.write(version)

    print("Updating pyproject.toml")
    data = None
    with open("pyproject.toml", "r", encoding="utf-8") as f:
        data = f.readlines()

    fI, fV = None, None
    for i, v in enumerate(data):
        if v.startswith("version = "):
            fI = i
            fV = v
            break

    fV = f'version = "{version}"\n'
    data[fI] = fV
    with open("pyproject.toml", "w", encoding="utf-8") as f:
        f.writelines(data)

    print("Updating src/PythonFunctions/Version.py")
    path = "src/PythonFunctions/Version.py"
    data = None
    with open(path, "r", encoding="utf-8") as f:
        data = f.readlines()

    fI, fV = None, None
    for i, v in enumerate(data):
        if v.startswith('    return "'):
            fI = i
            fV = v
            break

    fV = f'    return "{version}"\n'
    data[fI] = fV

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(data)


main()
