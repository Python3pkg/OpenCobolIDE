

from future.utils import PY3

if PY3:
    from tkinter.font import *
else:
    try:
        from tkinter.font import *
    except ImportError:
        raise ImportError('The tkFont module is missing. Does your Py2 '
                          'installation include tkinter?')

