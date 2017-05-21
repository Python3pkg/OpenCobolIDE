
from future.utils import PY3
__future_module__ = True

if not PY3:
    from tkinter import *
    from tkinter import (_cnfmerge, _default_root, _flatten, _join, _setit,
                         _splitdict, _stringify, _support_default_root, _test,
                         _tkinter)
else:
    from tkinter import *
