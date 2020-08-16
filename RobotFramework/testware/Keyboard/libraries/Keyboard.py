# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_Keyboard')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_Keyboard')
    _Keyboard = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Keyboard', [dirname(__file__)])
        except ImportError:
            import _Keyboard
            return _Keyboard
        try:
            _mod = imp.load_module('_Keyboard', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _Keyboard = swig_import_helper()
    del swig_import_helper
else:
    import _Keyboard
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _Keyboard.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _Keyboard.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _Keyboard.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _Keyboard.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _Keyboard.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _Keyboard.SwigPyIterator_equal(self, x)

    def copy(self):
        return _Keyboard.SwigPyIterator_copy(self)

    def next(self):
        return _Keyboard.SwigPyIterator_next(self)

    def __next__(self):
        return _Keyboard.SwigPyIterator___next__(self)

    def previous(self):
        return _Keyboard.SwigPyIterator_previous(self)

    def advance(self, n):
        return _Keyboard.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _Keyboard.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _Keyboard.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _Keyboard.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _Keyboard.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _Keyboard.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _Keyboard.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _Keyboard.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class vectori(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectori, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectori, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _Keyboard.vectori_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _Keyboard.vectori___nonzero__(self)

    def __bool__(self):
        return _Keyboard.vectori___bool__(self)

    def __len__(self):
        return _Keyboard.vectori___len__(self)

    def __getslice__(self, i, j):
        return _Keyboard.vectori___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _Keyboard.vectori___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _Keyboard.vectori___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _Keyboard.vectori___delitem__(self, *args)

    def __getitem__(self, *args):
        return _Keyboard.vectori___getitem__(self, *args)

    def __setitem__(self, *args):
        return _Keyboard.vectori___setitem__(self, *args)

    def pop(self):
        return _Keyboard.vectori_pop(self)

    def append(self, x):
        return _Keyboard.vectori_append(self, x)

    def empty(self):
        return _Keyboard.vectori_empty(self)

    def size(self):
        return _Keyboard.vectori_size(self)

    def swap(self, v):
        return _Keyboard.vectori_swap(self, v)

    def begin(self):
        return _Keyboard.vectori_begin(self)

    def end(self):
        return _Keyboard.vectori_end(self)

    def rbegin(self):
        return _Keyboard.vectori_rbegin(self)

    def rend(self):
        return _Keyboard.vectori_rend(self)

    def clear(self):
        return _Keyboard.vectori_clear(self)

    def get_allocator(self):
        return _Keyboard.vectori_get_allocator(self)

    def pop_back(self):
        return _Keyboard.vectori_pop_back(self)

    def erase(self, *args):
        return _Keyboard.vectori_erase(self, *args)

    def __init__(self, *args):
        this = _Keyboard.new_vectori(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _Keyboard.vectori_push_back(self, x)

    def front(self):
        return _Keyboard.vectori_front(self)

    def back(self):
        return _Keyboard.vectori_back(self)

    def assign(self, n, x):
        return _Keyboard.vectori_assign(self, n, x)

    def resize(self, *args):
        return _Keyboard.vectori_resize(self, *args)

    def insert(self, *args):
        return _Keyboard.vectori_insert(self, *args)

    def reserve(self, n):
        return _Keyboard.vectori_reserve(self, n)

    def capacity(self):
        return _Keyboard.vectori_capacity(self)
    __swig_destroy__ = _Keyboard.delete_vectori
    __del__ = lambda self: None
vectori_swigregister = _Keyboard.vectori_swigregister
vectori_swigregister(vectori)

class KeyboardController(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, KeyboardController, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, KeyboardController, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        getCurrentInstance = staticmethod(_Keyboard.KeyboardController_getCurrentInstance)
    else:
        getCurrentInstance = _Keyboard.KeyboardController_getCurrentInstance

    def pingKeyboard(self):
        return _Keyboard.KeyboardController_pingKeyboard(self)

    def addAutoDispatch(self, command):
        return _Keyboard.KeyboardController_addAutoDispatch(self, command)

    def getFirmwareVersion(self):
        return _Keyboard.KeyboardController_getFirmwareVersion(self)

    def getDebounce(self):
        return _Keyboard.KeyboardController_getDebounce(self)

    def setDebounce(self, time):
        return _Keyboard.KeyboardController_setDebounce(self, time)

    def getRandomNumber(self, dataSize):
        return _Keyboard.KeyboardController_getRandomNumber(self, dataSize)

    def eventMonitorThread(self, usbConnection):
        return _Keyboard.KeyboardController_eventMonitorThread(self, usbConnection)

    def signalGetKeyboardEvent(self):
        return _Keyboard.KeyboardController_signalGetKeyboardEvent(self)

    def checkEvent(self):
        return _Keyboard.KeyboardController_checkEvent(self)

    def initialize(self, startEventMonitorThread=True):
        return _Keyboard.KeyboardController_initialize(self, startEventMonitorThread)
    __swig_destroy__ = _Keyboard.delete_KeyboardController
    __del__ = lambda self: None
KeyboardController_swigregister = _Keyboard.KeyboardController_swigregister
KeyboardController_swigregister(KeyboardController)

def KeyboardController_getCurrentInstance(libUsb=None):
    return _Keyboard.KeyboardController_getCurrentInstance(libUsb)
KeyboardController_getCurrentInstance = _Keyboard.KeyboardController_getCurrentInstance

KeyboardSingleByte_PING_COMMAND = _Keyboard.KeyboardSingleByte_PING_COMMAND
KeyboardSingleByte_GET_FREQUENCY_COMMAND = _Keyboard.KeyboardSingleByte_GET_FREQUENCY_COMMAND
KeyboardSingleByte_GET_FW_VERSION_COMMAND = _Keyboard.KeyboardSingleByte_GET_FW_VERSION_COMMAND
KeyboardSingleByte_GET_DEBOUNCE_COMMAND = _Keyboard.KeyboardSingleByte_GET_DEBOUNCE_COMMAND
KeyboardSingleByte_KEYPAD_DIAGNOSTIC_COMMAND = _Keyboard.KeyboardSingleByte_KEYPAD_DIAGNOSTIC_COMMAND
KeyboardSingleByte_KEYPAD_CHECK_EVENT_COMMAND = _Keyboard.KeyboardSingleByte_KEYPAD_CHECK_EVENT_COMMAND
KeyboardMultiByte_SET_SLEEP_MODE_COMMAND = _Keyboard.KeyboardMultiByte_SET_SLEEP_MODE_COMMAND
KeyboardMultiByte_SET_MCU_FREQUENCY_COMMAND = _Keyboard.KeyboardMultiByte_SET_MCU_FREQUENCY_COMMAND
KeyboardMultiByte_SET_KEYBOARD_DEBOUNCE_COMMAND = _Keyboard.KeyboardMultiByte_SET_KEYBOARD_DEBOUNCE_COMMAND
KeyboardMultiByte_ADD_AUTO_DISPATCH_COMMAND = _Keyboard.KeyboardMultiByte_ADD_AUTO_DISPATCH_COMMAND
KeyboardMultiByte_REMOVE_AUTO_DISPATCH_COMMAND = _Keyboard.KeyboardMultiByte_REMOVE_AUTO_DISPATCH_COMMAND
KeyboardMultiByte_GET_RANDOM_NUMBER_COMMAND = _Keyboard.KeyboardMultiByte_GET_RANDOM_NUMBER_COMMAND
class KeyboardCommandBase(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, KeyboardCommandBase, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, KeyboardCommandBase, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def execute(self, usbConnection):
        return _Keyboard.KeyboardCommandBase_execute(self, usbConnection)
KeyboardCommandBase_swigregister = _Keyboard.KeyboardCommandBase_swigregister
KeyboardCommandBase_swigregister(KeyboardCommandBase)

ENDPOINTS_IN_MAIN = _Keyboard.ENDPOINTS_IN_MAIN
ENDPOINTS_IN_SECONDARY = _Keyboard.ENDPOINTS_IN_SECONDARY
class UsbConnection(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, UsbConnection, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, UsbConnection, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _Keyboard.new_UsbConnection(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _Keyboard.delete_UsbConnection
    __del__ = lambda self: None

    def createContext(self):
        return _Keyboard.UsbConnection_createContext(self)

    def openConnection(self):
        return _Keyboard.UsbConnection_openConnection(self)

    def sendCommand(self, command):
        return _Keyboard.UsbConnection_sendCommand(self, command)

    def getResponse(self, *args):
        return _Keyboard.UsbConnection_getResponse(self, *args)

    def closeConnection(self):
        return _Keyboard.UsbConnection_closeConnection(self)

    def isConnected(self):
        return _Keyboard.UsbConnection_isConnected(self)
UsbConnection_swigregister = _Keyboard.UsbConnection_swigregister
UsbConnection_swigregister(UsbConnection)

class IMonitor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IMonitor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IMonitor, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _Keyboard.delete_IMonitor
    __del__ = lambda self: None

    def start(self):
        return _Keyboard.IMonitor_start(self)

    def startMonitor(self):
        return _Keyboard.IMonitor_startMonitor(self)

    def stopMonitor(self):
        return _Keyboard.IMonitor_stopMonitor(self)

    def isRunning(self):
        return _Keyboard.IMonitor_isRunning(self)

    def signalEventDetected(self):
        return _Keyboard.IMonitor_signalEventDetected(self)
IMonitor_swigregister = _Keyboard.IMonitor_swigregister
IMonitor_swigregister(IMonitor)

class UdevMonitor(IMonitor):
    __swig_setmethods__ = {}
    for _s in [IMonitor]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, UdevMonitor, name, value)
    __swig_getmethods__ = {}
    for _s in [IMonitor]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, UdevMonitor, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _Keyboard.new_UdevMonitor()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def start(self):
        return _Keyboard.UdevMonitor_start(self)

    def startMonitor(self):
        return _Keyboard.UdevMonitor_startMonitor(self)

    def stopMonitor(self):
        return _Keyboard.UdevMonitor_stopMonitor(self)

    def isRunning(self):
        return _Keyboard.UdevMonitor_isRunning(self)

    def signalEventDetected(self):
        return _Keyboard.UdevMonitor_signalEventDetected(self)

    def getDetectedDevices(self):
        return _Keyboard.UdevMonitor_getDetectedDevices(self)
    __swig_destroy__ = _Keyboard.delete_UdevMonitor
    __del__ = lambda self: None
UdevMonitor_swigregister = _Keyboard.UdevMonitor_swigregister
UdevMonitor_swigregister(UdevMonitor)

class AddAutoDispatchCommand(KeyboardCommandBase):
    __swig_setmethods__ = {}
    for _s in [KeyboardCommandBase]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, AddAutoDispatchCommand, name, value)
    __swig_getmethods__ = {}
    for _s in [KeyboardCommandBase]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, AddAutoDispatchCommand, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
AddAutoDispatchCommand_swigregister = _Keyboard.AddAutoDispatchCommand_swigregister
AddAutoDispatchCommand_swigregister(AddAutoDispatchCommand)

class GetDebounceCommand(KeyboardCommandBase):
    __swig_setmethods__ = {}
    for _s in [KeyboardCommandBase]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GetDebounceCommand, name, value)
    __swig_getmethods__ = {}
    for _s in [KeyboardCommandBase]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GetDebounceCommand, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
GetDebounceCommand_swigregister = _Keyboard.GetDebounceCommand_swigregister
GetDebounceCommand_swigregister(GetDebounceCommand)

class GetFirmwareVersionCommand(KeyboardCommandBase):
    __swig_setmethods__ = {}
    for _s in [KeyboardCommandBase]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GetFirmwareVersionCommand, name, value)
    __swig_getmethods__ = {}
    for _s in [KeyboardCommandBase]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GetFirmwareVersionCommand, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
GetFirmwareVersionCommand_swigregister = _Keyboard.GetFirmwareVersionCommand_swigregister
GetFirmwareVersionCommand_swigregister(GetFirmwareVersionCommand)

class KeyboardCommandsFactory(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, KeyboardCommandsFactory, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, KeyboardCommandsFactory, name)
    __repr__ = _swig_repr
    if _newclass:
        createPingCommand = staticmethod(_Keyboard.KeyboardCommandsFactory_createPingCommand)
    else:
        createPingCommand = _Keyboard.KeyboardCommandsFactory_createPingCommand
    if _newclass:
        createGetFWVersionCommand = staticmethod(_Keyboard.KeyboardCommandsFactory_createGetFWVersionCommand)
    else:
        createGetFWVersionCommand = _Keyboard.KeyboardCommandsFactory_createGetFWVersionCommand
    if _newclass:
        createGetDebounceCommand = staticmethod(_Keyboard.KeyboardCommandsFactory_createGetDebounceCommand)
    else:
        createGetDebounceCommand = _Keyboard.KeyboardCommandsFactory_createGetDebounceCommand
    if _newclass:
        createKeypadCheckEventCommand = staticmethod(_Keyboard.KeyboardCommandsFactory_createKeypadCheckEventCommand)
    else:
        createKeypadCheckEventCommand = _Keyboard.KeyboardCommandsFactory_createKeypadCheckEventCommand
    if _newclass:
        createAddAutoDispatchCommand = staticmethod(_Keyboard.KeyboardCommandsFactory_createAddAutoDispatchCommand)
    else:
        createAddAutoDispatchCommand = _Keyboard.KeyboardCommandsFactory_createAddAutoDispatchCommand
    if _newclass:
        createSetDebounceCommand = staticmethod(_Keyboard.KeyboardCommandsFactory_createSetDebounceCommand)
    else:
        createSetDebounceCommand = _Keyboard.KeyboardCommandsFactory_createSetDebounceCommand
    if _newclass:
        createGetRandomNumberCommand = staticmethod(_Keyboard.KeyboardCommandsFactory_createGetRandomNumberCommand)
    else:
        createGetRandomNumberCommand = _Keyboard.KeyboardCommandsFactory_createGetRandomNumberCommand

    def __init__(self):
        this = _Keyboard.new_KeyboardCommandsFactory()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _Keyboard.delete_KeyboardCommandsFactory
    __del__ = lambda self: None
KeyboardCommandsFactory_swigregister = _Keyboard.KeyboardCommandsFactory_swigregister
KeyboardCommandsFactory_swigregister(KeyboardCommandsFactory)

def KeyboardCommandsFactory_createPingCommand():
    return _Keyboard.KeyboardCommandsFactory_createPingCommand()
KeyboardCommandsFactory_createPingCommand = _Keyboard.KeyboardCommandsFactory_createPingCommand

def KeyboardCommandsFactory_createGetFWVersionCommand():
    return _Keyboard.KeyboardCommandsFactory_createGetFWVersionCommand()
KeyboardCommandsFactory_createGetFWVersionCommand = _Keyboard.KeyboardCommandsFactory_createGetFWVersionCommand

def KeyboardCommandsFactory_createGetDebounceCommand():
    return _Keyboard.KeyboardCommandsFactory_createGetDebounceCommand()
KeyboardCommandsFactory_createGetDebounceCommand = _Keyboard.KeyboardCommandsFactory_createGetDebounceCommand

def KeyboardCommandsFactory_createKeypadCheckEventCommand():
    return _Keyboard.KeyboardCommandsFactory_createKeypadCheckEventCommand()
KeyboardCommandsFactory_createKeypadCheckEventCommand = _Keyboard.KeyboardCommandsFactory_createKeypadCheckEventCommand

def KeyboardCommandsFactory_createAddAutoDispatchCommand(command):
    return _Keyboard.KeyboardCommandsFactory_createAddAutoDispatchCommand(command)
KeyboardCommandsFactory_createAddAutoDispatchCommand = _Keyboard.KeyboardCommandsFactory_createAddAutoDispatchCommand

def KeyboardCommandsFactory_createSetDebounceCommand(frequency):
    return _Keyboard.KeyboardCommandsFactory_createSetDebounceCommand(frequency)
KeyboardCommandsFactory_createSetDebounceCommand = _Keyboard.KeyboardCommandsFactory_createSetDebounceCommand

def KeyboardCommandsFactory_createGetRandomNumberCommand(dataSize):
    return _Keyboard.KeyboardCommandsFactory_createGetRandomNumberCommand(dataSize)
KeyboardCommandsFactory_createGetRandomNumberCommand = _Keyboard.KeyboardCommandsFactory_createGetRandomNumberCommand

class KeypadCheckEventCommand(KeyboardCommandBase):
    __swig_setmethods__ = {}
    for _s in [KeyboardCommandBase]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, KeypadCheckEventCommand, name, value)
    __swig_getmethods__ = {}
    for _s in [KeyboardCommandBase]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, KeypadCheckEventCommand, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
KeypadCheckEventCommand_swigregister = _Keyboard.KeypadCheckEventCommand_swigregister
KeypadCheckEventCommand_swigregister(KeypadCheckEventCommand)

class PingCommand(KeyboardCommandBase):
    __swig_setmethods__ = {}
    for _s in [KeyboardCommandBase]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PingCommand, name, value)
    __swig_getmethods__ = {}
    for _s in [KeyboardCommandBase]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PingCommand, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
PingCommand_swigregister = _Keyboard.PingCommand_swigregister
PingCommand_swigregister(PingCommand)

class SetDebounceCommand(KeyboardCommandBase):
    __swig_setmethods__ = {}
    for _s in [KeyboardCommandBase]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SetDebounceCommand, name, value)
    __swig_getmethods__ = {}
    for _s in [KeyboardCommandBase]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SetDebounceCommand, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
SetDebounceCommand_swigregister = _Keyboard.SetDebounceCommand_swigregister
SetDebounceCommand_swigregister(SetDebounceCommand)

# This file is compatible with both classic and new-style classes.


