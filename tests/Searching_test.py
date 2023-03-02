from . import search

hidden = [".venv", "*.pyc", "docs", "dist", "typings", ".git", ".github"]
srch = search()


def test_find_watermark():
    result = srch.Locate("Watermark.py", hidden=hidden, layers=0, logging=True)
    assert len(result) == 1


def test_find_Multiple():
    srch.Clear()
    result = srch.Locate(
        ["Board.py", "Check.py", "Updater.py", "main.py", "__init__.py"],
        hidden=hidden,
        layers=0,
        logging=True,
    )
    print(result)
    assert len(result) == 8
