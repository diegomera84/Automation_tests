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
        mname = '.'.join((pkg, '_Printer')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_Printer')
    _Printer = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Printer', [dirname(__file__)])
        except ImportError:
            import _Printer
            return _Printer
        try:
            _mod = imp.load_module('_Printer', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _Printer = swig_import_helper()
    del swig_import_helper
else:
    import _Printer
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
    __swig_destroy__ = _Printer.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _Printer.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _Printer.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _Printer.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _Printer.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _Printer.SwigPyIterator_equal(self, x)

    def copy(self):
        return _Printer.SwigPyIterator_copy(self)

    def next(self):
        return _Printer.SwigPyIterator_next(self)

    def __next__(self):
        return _Printer.SwigPyIterator___next__(self)

    def previous(self):
        return _Printer.SwigPyIterator_previous(self)

    def advance(self, n):
        return _Printer.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _Printer.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _Printer.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _Printer.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _Printer.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _Printer.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _Printer.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _Printer.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class vectori(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vectori, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vectori, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _Printer.vectori_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _Printer.vectori___nonzero__(self)

    def __bool__(self):
        return _Printer.vectori___bool__(self)

    def __len__(self):
        return _Printer.vectori___len__(self)

    def __getslice__(self, i, j):
        return _Printer.vectori___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _Printer.vectori___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _Printer.vectori___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _Printer.vectori___delitem__(self, *args)

    def __getitem__(self, *args):
        return _Printer.vectori___getitem__(self, *args)

    def __setitem__(self, *args):
        return _Printer.vectori___setitem__(self, *args)

    def pop(self):
        return _Printer.vectori_pop(self)

    def append(self, x):
        return _Printer.vectori_append(self, x)

    def empty(self):
        return _Printer.vectori_empty(self)

    def size(self):
        return _Printer.vectori_size(self)

    def swap(self, v):
        return _Printer.vectori_swap(self, v)

    def begin(self):
        return _Printer.vectori_begin(self)

    def end(self):
        return _Printer.vectori_end(self)

    def rbegin(self):
        return _Printer.vectori_rbegin(self)

    def rend(self):
        return _Printer.vectori_rend(self)

    def clear(self):
        return _Printer.vectori_clear(self)

    def get_allocator(self):
        return _Printer.vectori_get_allocator(self)

    def pop_back(self):
        return _Printer.vectori_pop_back(self)

    def erase(self, *args):
        return _Printer.vectori_erase(self, *args)

    def __init__(self, *args):
        this = _Printer.new_vectori(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _Printer.vectori_push_back(self, x)

    def front(self):
        return _Printer.vectori_front(self)

    def back(self):
        return _Printer.vectori_back(self)

    def assign(self, n, x):
        return _Printer.vectori_assign(self, n, x)

    def resize(self, *args):
        return _Printer.vectori_resize(self, *args)

    def insert(self, *args):
        return _Printer.vectori_insert(self, *args)

    def reserve(self, n):
        return _Printer.vectori_reserve(self, n)

    def capacity(self):
        return _Printer.vectori_capacity(self)
    __swig_destroy__ = _Printer.delete_vectori
    __del__ = lambda self: None
vectori_swigregister = _Printer.vectori_swigregister
vectori_swigregister(vectori)

class ILibUsb(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ILibUsb, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ILibUsb, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _Printer.delete_ILibUsb
    __del__ = lambda self: None

    def initialize(self, context):
        return _Printer.ILibUsb_initialize(self, context)

    def setDebug(self, context, level):
        return _Printer.ILibUsb_setDebug(self, context, level)

    def openDeviceWithVidPid(self, context, vendorId, productId):
        return _Printer.ILibUsb_openDeviceWithVidPid(self, context, vendorId, productId)

    def isKernelDriverActive(self, handle, interfaceNumber):
        return _Printer.ILibUsb_isKernelDriverActive(self, handle, interfaceNumber)

    def detachKernelDriver(self, handle, interfaceNumber):
        return _Printer.ILibUsb_detachKernelDriver(self, handle, interfaceNumber)

    def claimInterface(self, handle, interfaceNumber):
        return _Printer.ILibUsb_claimInterface(self, handle, interfaceNumber)

    def bulkTransfer(self, handle, endpoint, data, length, actualLength, timeout):
        return _Printer.ILibUsb_bulkTransfer(self, handle, endpoint, data, length, actualLength, timeout)

    def releaseInterface(self, handle, interfaceNumber):
        return _Printer.ILibUsb_releaseInterface(self, handle, interfaceNumber)

    def getErrorMessage(self, errorCode):
        return _Printer.ILibUsb_getErrorMessage(self, errorCode)

    def close(self, handle):
        return _Printer.ILibUsb_close(self, handle)

    def exit(self, context):
        return _Printer.ILibUsb_exit(self, context)
ILibUsb_swigregister = _Printer.ILibUsb_swigregister
ILibUsb_swigregister(ILibUsb)

class ICups(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ICups, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ICups, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _Printer.delete_ICups
    __del__ = lambda self: None

    def getJobs(self, jobs, name, myJobs, whichJobs):
        return _Printer.ICups_getJobs(self, jobs, name, myJobs, whichJobs)

    def getDestinations(self, destinations):
        return _Printer.ICups_getDestinations(self, destinations)

    def printFile(self, name, fileName, title, numberOfOptions, options):
        return _Printer.ICups_printFile(self, name, fileName, title, numberOfOptions, options)

    def cancelJob(self, name, jobId):
        return _Printer.ICups_cancelJob(self, name, jobId)
ICups_swigregister = _Printer.ICups_swigregister
ICups_swigregister(ICups)

class PrinterJobsManager(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PrinterJobsManager, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PrinterJobsManager, name)
    __repr__ = _swig_repr
    if _newclass:
        getCurrentInstance = staticmethod(_Printer.PrinterJobsManager_getCurrentInstance)
    else:
        getCurrentInstance = _Printer.PrinterJobsManager_getCurrentInstance
    if _newclass:
        dispose = staticmethod(_Printer.PrinterJobsManager_dispose)
    else:
        dispose = _Printer.PrinterJobsManager_dispose
    __swig_destroy__ = _Printer.delete_PrinterJobsManager
    __del__ = lambda self: None

    def __init__(self, arg2):
        this = _Printer.new_PrinterJobsManager(arg2)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def printFile(self, filePath):
        return _Printer.PrinterJobsManager_printFile(self, filePath)
PrinterJobsManager_swigregister = _Printer.PrinterJobsManager_swigregister
PrinterJobsManager_swigregister(PrinterJobsManager)

def PrinterJobsManager_getCurrentInstance(cups=None):
    return _Printer.PrinterJobsManager_getCurrentInstance(cups)
PrinterJobsManager_getCurrentInstance = _Printer.PrinterJobsManager_getCurrentInstance

def PrinterJobsManager_dispose():
    return _Printer.PrinterJobsManager_dispose()
PrinterJobsManager_dispose = _Printer.PrinterJobsManager_dispose

class CupsWrapper(ICups):
    __swig_setmethods__ = {}
    for _s in [ICups]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CupsWrapper, name, value)
    __swig_getmethods__ = {}
    for _s in [ICups]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CupsWrapper, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _Printer.delete_CupsWrapper
    __del__ = lambda self: None

    def getJobs(self, jobs, name, myJobs, whichJobs):
        return _Printer.CupsWrapper_getJobs(self, jobs, name, myJobs, whichJobs)

    def getDestinations(self, destinations):
        return _Printer.CupsWrapper_getDestinations(self, destinations)

    def printFile(self, name, fileName, title, numberOfOptions, options):
        return _Printer.CupsWrapper_printFile(self, name, fileName, title, numberOfOptions, options)

    def cancelJob(self, name, jobId):
        return _Printer.CupsWrapper_cancelJob(self, name, jobId)

    def __init__(self):
        this = _Printer.new_CupsWrapper()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
CupsWrapper_swigregister = _Printer.CupsWrapper_swigregister
CupsWrapper_swigregister(CupsWrapper)

class PrinterStatusManager(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PrinterStatusManager, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PrinterStatusManager, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        getCurrentInstance = staticmethod(_Printer.PrinterStatusManager_getCurrentInstance)
    else:
        getCurrentInstance = _Printer.PrinterStatusManager_getCurrentInstance
    if _newclass:
        dispose = staticmethod(_Printer.PrinterStatusManager_dispose)
    else:
        dispose = _Printer.PrinterStatusManager_dispose

    def startPrinterMonitor(self):
        return _Printer.PrinterStatusManager_startPrinterMonitor(self)

    def stopPrinterMonitor(self):
        return _Printer.PrinterStatusManager_stopPrinterMonitor(self)

    def isPrinterMonitorRunning(self):
        return _Printer.PrinterStatusManager_isPrinterMonitorRunning(self)

    def startCupsMonitor(self, printerName, jobId):
        return _Printer.PrinterStatusManager_startCupsMonitor(self, printerName, jobId)

    def stopCupsMonitor(self):
        return _Printer.PrinterStatusManager_stopCupsMonitor(self)

    def isCupsMonitorRunning(self):
        return _Printer.PrinterStatusManager_isCupsMonitorRunning(self)

    def didJobStatusChange(self, printerName, jobId):
        return _Printer.PrinterStatusManager_didJobStatusChange(self, printerName, jobId)

    def didHotSwapOccur(self):
        return _Printer.PrinterStatusManager_didHotSwapOccur(self)

    def updatePrinterStatus(self):
        return _Printer.PrinterStatusManager_updatePrinterStatus(self)

    def updateCupsStatus(self, printerName, jobId):
        return _Printer.PrinterStatusManager_updateCupsStatus(self, printerName, jobId)

    def getCurrentScenario(self):
        return _Printer.PrinterStatusManager_getCurrentScenario(self)

    def getTemperature(self):
        return _Printer.PrinterStatusManager_getTemperature(self)

    def signalPrinterStatus(self):
        return _Printer.PrinterStatusManager_signalPrinterStatus(self)

    def signalCupsStatus(self):
        return _Printer.PrinterStatusManager_signalCupsStatus(self)
    __swig_destroy__ = _Printer.delete_PrinterStatusManager
    __del__ = lambda self: None
PrinterStatusManager_swigregister = _Printer.PrinterStatusManager_swigregister
PrinterStatusManager_swigregister(PrinterStatusManager)

def PrinterStatusManager_getCurrentInstance(cups=None):
    return _Printer.PrinterStatusManager_getCurrentInstance(cups)
PrinterStatusManager_getCurrentInstance = _Printer.PrinterStatusManager_getCurrentInstance

def PrinterStatusManager_dispose():
    return _Printer.PrinterStatusManager_dispose()
PrinterStatusManager_dispose = _Printer.PrinterStatusManager_dispose

class AbstractCommand(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AbstractCommand, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AbstractCommand, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _Printer.delete_AbstractCommand
    __del__ = lambda self: None

    def execute(self, usbConnection):
        return _Printer.AbstractCommand_execute(self, usbConnection)

    def getResponse(self):
        return _Printer.AbstractCommand_getResponse(self)

    def __init__(self):
        this = _Printer.new_AbstractCommand()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
AbstractCommand_swigregister = _Printer.AbstractCommand_swigregister
AbstractCommand_swigregister(AbstractCommand)

class PrinterCommandsFactory(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PrinterCommandsFactory, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PrinterCommandsFactory, name)
    __repr__ = _swig_repr
    if _newclass:
        getCommandGetStatus = staticmethod(_Printer.PrinterCommandsFactory_getCommandGetStatus)
    else:
        getCommandGetStatus = _Printer.PrinterCommandsFactory_getCommandGetStatus
    if _newclass:
        getCommandGetFirmwareVersion = staticmethod(_Printer.PrinterCommandsFactory_getCommandGetFirmwareVersion)
    else:
        getCommandGetFirmwareVersion = _Printer.PrinterCommandsFactory_getCommandGetFirmwareVersion

    def __init__(self):
        this = _Printer.new_PrinterCommandsFactory()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _Printer.delete_PrinterCommandsFactory
    __del__ = lambda self: None
PrinterCommandsFactory_swigregister = _Printer.PrinterCommandsFactory_swigregister
PrinterCommandsFactory_swigregister(PrinterCommandsFactory)

def PrinterCommandsFactory_getCommandGetStatus():
    return _Printer.PrinterCommandsFactory_getCommandGetStatus()
PrinterCommandsFactory_getCommandGetStatus = _Printer.PrinterCommandsFactory_getCommandGetStatus

def PrinterCommandsFactory_getCommandGetFirmwareVersion():
    return _Printer.PrinterCommandsFactory_getCommandGetFirmwareVersion()
PrinterCommandsFactory_getCommandGetFirmwareVersion = _Printer.PrinterCommandsFactory_getCommandGetFirmwareVersion

class PrinterCommandsManager(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PrinterCommandsManager, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PrinterCommandsManager, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    if _newclass:
        getCurrentInstance = staticmethod(_Printer.PrinterCommandsManager_getCurrentInstance)
    else:
        getCurrentInstance = _Printer.PrinterCommandsManager_getCurrentInstance
    if _newclass:
        dispose = staticmethod(_Printer.PrinterCommandsManager_dispose)
    else:
        dispose = _Printer.PrinterCommandsManager_dispose

    def openConnection(self):
        return _Printer.PrinterCommandsManager_openConnection(self)

    def closeConnection(self):
        return _Printer.PrinterCommandsManager_closeConnection(self)

    def isConnectionOpen(self):
        return _Printer.PrinterCommandsManager_isConnectionOpen(self)

    def getPrinterStatus(self):
        return _Printer.PrinterCommandsManager_getPrinterStatus(self)

    def getFirmwareVersion(self):
        return _Printer.PrinterCommandsManager_getFirmwareVersion(self)
    __swig_destroy__ = _Printer.delete_PrinterCommandsManager
    __del__ = lambda self: None
PrinterCommandsManager_swigregister = _Printer.PrinterCommandsManager_swigregister
PrinterCommandsManager_swigregister(PrinterCommandsManager)

def PrinterCommandsManager_getCurrentInstance(libUsb=None):
    return _Printer.PrinterCommandsManager_getCurrentInstance(libUsb)
PrinterCommandsManager_getCurrentInstance = _Printer.PrinterCommandsManager_getCurrentInstance

def PrinterCommandsManager_dispose():
    return _Printer.PrinterCommandsManager_dispose()
PrinterCommandsManager_dispose = _Printer.PrinterCommandsManager_dispose

ENDPOINTS_IN_MAIN = _Printer.ENDPOINTS_IN_MAIN
ENDPOINTS_IN_SECONDARY = _Printer.ENDPOINTS_IN_SECONDARY
class UsbConnection(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, UsbConnection, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, UsbConnection, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _Printer.new_UsbConnection(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _Printer.delete_UsbConnection
    __del__ = lambda self: None

    def createContext(self):
        return _Printer.UsbConnection_createContext(self)

    def openConnection(self):
        return _Printer.UsbConnection_openConnection(self)

    def sendCommand(self, command):
        return _Printer.UsbConnection_sendCommand(self, command)

    def getResponse(self, *args):
        return _Printer.UsbConnection_getResponse(self, *args)

    def closeConnection(self):
        return _Printer.UsbConnection_closeConnection(self)

    def isConnected(self):
        return _Printer.UsbConnection_isConnected(self)
UsbConnection_swigregister = _Printer.UsbConnection_swigregister
UsbConnection_swigregister(UsbConnection)

# This file is compatible with both classic and new-style classes.


