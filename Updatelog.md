# Update log

This file contains all the updates that were removed from [read me](README.md) to save space in the main file.
The only update in the main file, is the latest update.

## 1.1.6

- Fixed issue where `CleanFolderData.RemoveReserved()` would not remove files with `*`

## 1.1.5

- Fixed another issue with `CleanFolderdata.clean()` causing reserved file not to be removed (or everything got removed).

## 1.1.4

- Fixed issue with `CleanFolderData.clean()` not working due to resvered not being a string

## 1.1.3

- Added `*.txt` (wildcard) support to `CleanFolderData.RemoveReserved()`
- Added str support to `CleanFolderData.RemoveReserved()` (You can pass in a string now without it breaking)
- Updated testing to include `*.txt` support

## 1.1.2

- Fixed issue with getting server version.

## 1.1.1

- Fixed issue with how i did the update check (also made a new function because of it)
- Added documentation for how to mute the update output

## 1.1.0

- Created documentation on readthedocs
- Added dependencies to pyproject.toml
- Renamed some stuff
- Improved some checks
- Fixed some bugs
- Added Version.txt to inform people of outdated versions.
- Removed loading all the modules on __init__
- Updated and fixed tests

## 1.0.1

- Attempting to fix no description on testpypi

## 1.0.0

- Actually uploading it now
