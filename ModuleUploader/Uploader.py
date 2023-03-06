import concurrent.futures
import os


def getVersion():
    with open("Version.txt", "r", encoding="utf-8") as f:
        return f.read()


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor: concurrent.futures.Executor
    build = executor.submit(os.system, "python -m build")
    future = executor.submit(getVersion)
    version = future.result()
    print(f"Version: {version}")
    print(f"Build Result: {build.result()}")
    targz = f"dist/PythonFunctions-{version}.tar.gz"
    whl = f"dist/PythonFunctions-{version}-py3-none-any.whl"
    twine = executor.submit(
        os.system,
        f"twine upload {targz} {whl}",
    )
    print(f"Twine: {twine.result()}")
