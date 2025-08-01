# Copyright: Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

# make sure not to optimize imports on this file
# ruff: noqa: F401
"""
PyQt6 imports
"""

from PyQt6 import sip
from PyQt6.QtCore import *

# conflicting Qt and qFuzzyCompare definitions require an ignore
from PyQt6.QtGui import *  # type: ignore[no-redef,assignment]
from PyQt6.QtNetwork import QLocalServer, QLocalSocket, QNetworkProxy
from PyQt6.QtQuick import *
from PyQt6.QtWebChannel import QWebChannel
from PyQt6.QtWebEngineCore import *
from PyQt6.QtWebEngineWidgets import *
from PyQt6.QtWidgets import *
