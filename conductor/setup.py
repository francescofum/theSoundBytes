from cx_Freeze import setup,Executable
import dbm

build_exe_options = {'packages': ['dbm']}
setup(name = "theSoundBytes" ,
      version = "0.1" ,
      description = "Executable for the soundBytes orchestra" ,
      executables = [Executable("main.py")])
