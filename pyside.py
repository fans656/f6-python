import ctypes

def get_hwnd(widget):
    pycobject_hwnd = widget.winId()
    ctypes.pythonapi.PyCObject_AsVoidPtr.restype = ctypes.c_void_p
    ctypes.pythonapi.PyCObject_AsVoidPtr.argtypes = [ctypes.py_object]
    hwnd = ctypes.pythonapi.PyCObject_AsVoidPtr(pycobject_hwnd)
    return hwnd
widget2hwnd = get_hwnd
gethwnd = get_hwnd
