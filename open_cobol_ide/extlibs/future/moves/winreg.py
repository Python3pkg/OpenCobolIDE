
from future.utils import PY3

if PY3:
    from winreg import *
else:
    __future_module__ = True
    from winreg import *
