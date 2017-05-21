

from future.utils import PY3

if PY3:
    from tkinter.messagebox import *
else:
    try:
        from tkinter.messagebox import *
    except ImportError:
        raise ImportError('The tkMessageBox module is missing. Does your Py2 '
                          'installation include tkinter?')

