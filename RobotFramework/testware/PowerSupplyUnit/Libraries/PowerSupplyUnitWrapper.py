"""Script to use the basic commands of the PowerSupplyUnit  through
    methods of the UE2020 source code implemented for python by SWIG."""
import PowerSupplyUnit
hidPsu = PowerSupplyUnit.HidPsu()
psu = PowerSupplyUnit.Psu(hidPsu, None)

class PowerSupplyUnitWrapper(object):
        
    def __init__(self):
        
        self.__current_psu_comand = PowerSupplyUnit.PsuController.getCurrentInstance(psu)

    def powersupplyunit_initialize(self):
        """ 
        :return: Model and firmware version of the power supply unit
        """
        initialize = self.__current_psu_comand.initialize()
        print(initialize)
        return initialize

    def get_powersupplyunit_version(self):
        """ 
        :return: Model and firmware version of the power supply unit
        """
        self.__current_psu_comand.updateState()
        version_powersupplyunit = self.__current_psu_comand.getVersion()
        print(version_powersupplyunit)
        return version_powersupplyunit

    def get_powersupplyunit_acvolt(self):
        """
        :return: Volt of the powersupplyunit
        """
        self.__current_psu_comand.updateState()
        status_volts_powersupplyunit = self.__current_psu_comand.getAcDcVoltage() + 'V'
        return status_volts_powersupplyunit

    def get_powersupplyunit_InternalBatteryVoltage(self):
        """"
        :return: Volt of the internal battery
        """
        self.__current_psu_comand.updateState()
        status_volts_internalbattery = self.__current_psu_comand.getInternalBatteryVoltage() + 'V'
        return status_volts_internalbattery

    def get_powersupplyunit_InternalBatteryPercentage(self):
        """
        :return: Psu internal battery percentage
        """
        self.__current_psu_comand.updateState()
        status_InternalBatteryPercentage = self.__current_psu_comand.getInternalBatteryVoltage()
        return status_InternalBatteryPercentage

    