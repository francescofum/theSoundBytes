from cx_Freeze import setup,Executable


build_exe_options = {'packages': ['dbm']}
setup(name = "theSoundBytes" ,
      version = "0.1" ,
      options = {"build_exe": build_exe_options},
      description = "Executable for the soundBytes orchestra" ,
      executables = [Executable("main.py")])
