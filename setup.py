import cx_Freeze
import sys
import os

base = None

if sys.platform == "win32":
    base = "win32GUI"

os.environ["TCL_LIBRARY:"] = r"C:\Users\Bhanu\AppData\Local\Programs\Python\Python37\tcl\tcl8.6"
os.environ["TK_LIBRARY"] = r"C:\Users\Bhanu\AppData\Local\Programs\Python\Python37\tcl\tk8.6"

executables = [cx_Freeze.Executable("Youtube_Downloader.py", base=base,)]

cx_Freeze.setup(
    name = "Youtube Downloader",
    options = {"bulid.exe":{"packages":["tkinter","os"],"include_files":["tcl86t.dll","tk86t.dll",]}},
    version = "0.1",
    description = "Tkinter GUI Application",
    executables = executables
)
