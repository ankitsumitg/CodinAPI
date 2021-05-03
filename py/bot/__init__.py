"""
Discord Bot
"""

from typing import NamedTuple

VersionInfo = NamedTuple(
    "VersionInfo", major=int, minor=int, micro=int, releaselevel=str, serial=int
)

version_info = VersionInfo(major=0, minor=0, micro=1, releaselevel="", serial=0)

__title__ = "disocrdbot"
__author__ = "ankitsumitg"
__version__ = "0.0.1"