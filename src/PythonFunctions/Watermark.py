import datetime
import inspect
import os

from colorama import Style

BROKENSHELL = ('/bin/zsh')
SHELL = os.environ.get('SHELL')


def LINKCODE(link: str, text: str = None) -> str:
    """Returns the text as a clickable link

    Args:
        link (str): The link to send the user to on click 
        text (str, optional): The text to mask the linke. Defaults to None.

    Returns:
        str: The clickable text
    """
    if SHELL in BROKENSHELL:
        return f'{text} ({link})'

    if text is None:
        text = link
    return f"\u001b]8;;{link}\u001b\\{text}\u001b]8;;\u001b\\"


def TIME():
    def convertToFull(value):
        vs = str(value)
        if value < 10:
            vs = f"0{value}"

        return vs

    ctime = datetime.datetime.now()
    h = ctime.hour
    m = ctime.minute
    s = ctime.second

    hs = convertToFull(h)
    ms = convertToFull(m)
    ss = convertToFull(s)

    return hs, ms, ss


def watermark(
    name: str,
    twitter: str = None,
    youtube: str = None,
    github: str = None,
    *,
    colour: str = "",
):
    """
    Prints off a watermark / header style thing on call.

    Args:
        name (str): The username
        twitter (str, optional): Twitter link
        youtube (str, optional): Youtube link
        github (str, optional): Github link
        colour (str, optional): Colour of the watermark
    """
    fileName: str = "__main__"

    for frame in inspect.stack()[1:]:
        if frame.filename[0] != "<":
            fileName = os.path.basename(frame.filename)[:-3]
            break

    line = "-" * os.get_terminal_size().columns

    data = ""
    if twitter is not None:
        data += LINKCODE(twitter, "Twitter")
    if youtube is not None:
        data += LINKCODE(youtube, "Youtube")
    if github is not None:
        data += LINKCODE(github, "Github")

    if data == "":
        data = "Nothing linked"

    mydata = ""
    mydata += LINKCODE("https://twitter.com/DragMine149", "Twitter") + ","
    mydata += LINKCODE("https://youtube.com/@dragmine", "Youtube") + ","
    mydata += LINKCODE("https://github.com/dragmine149", "Github")

    h, m, s = TIME()

    print("\x1b[2J\x1b[H", end="")
    print(
        f"""{colour}{line}{Style.RESET_ALL}
{fileName} made by {name} ({data}).
Contains Functions.py made by dragmine149 ({mydata}).
Activation Time: {h}:{m}:{s}
{colour}{line}{Style.RESET_ALL}"""
    )
