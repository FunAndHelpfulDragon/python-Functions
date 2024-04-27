import typing
import os

from .CleanFolderData import Clean
from . import Message


def decode(s: str) -> int:
    # Thanks to Guy_732
    # changes letter to number based in the alphabet
    s = s.lower()
    ref = ord("a") - 1
    v = 0
    exp = 1
    for c in reversed(s):
        v += (ord(c) - ref) * exp
        exp *= 26

    return v


def Location(value: str) -> typing.Tuple:
    """Convert a letter number location into two numbers.

    Args:
        value (str): The letter number value to convert.

    Returns:
        typing.Tuple: The result of the conversion.
    """
    letters = ""
    y = ""

    if len(value) >= 2:
        value = value.lower().strip()

        for v in value:
            if v.isdigit():
                y += v
                continue

            letters += v

        if letters == value:
            return (
                Message.clear(
                    "Input must contain at least 1 letter and at least 1 integer.",
                    timeS=1,
                ),
                None,
            )

        return decode(letters) - 1, int(y) - 1

    return (
        Message.clear(
            "Input must contain at least 1 letter and at least 1 integer.", timeS=1
        ),
        None,
    )


def AudioExtractor(path: str, destination: str = "mp3"):
    """Convert a mp4 file to mp3. Supports whole folders.
    Credit: https://stackoverflow.com/questions/55081352/how-to-convert-mp4-to-mp3-using-python

    Args:
        path (str): The path to convert the data.
        destination (str, optional): The destination of the data. Defaults to 'mp3'.
    """
    try:
        # pylint: disable=C0415
        import moviepy.editor as mpyEditor

        # pylint: enable=C0415
    except ModuleNotFoundError:
        return Message.warn(
		f"Failed to convert files due to missing 'moviepy' module"
	)

    data = [path]
    directory: str = ""
    if os.path.isdir(path):
        data = Clean().clean(path)
        directory = path

    if len(data) == 0:
        return "No files found!"

    if not os.path.exists(destination):
        os.makedirs(destination)

    for i in data:
        # avoid repeating the same things
        if i.replace(".mp4", ".mp3") in os.listdir(destination):
            continue

        if i.endswith(".mp4"):
            FILE = mpyEditor.AudioFileClip(f"{directory}/{i}")
            FILE.write_audiofile(f'{destination}/{i.replace(".mp4", ".mp3")}')
            FILE.close()

    return Message.warn(
        f"Finished making mp3 files. Check: {os.path.abspath(destination)}", timeS=0.5
    )
