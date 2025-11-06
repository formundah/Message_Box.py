import ctypes


message = "Hello, World!"
title = "Simple Message Box"

MB_OK = 0x00000000
MB_ICONERROR = 0x00000030


ctypes.windll.user32.MessageBoxW(0, message, title, MB_OK | MB_ICONERROR)