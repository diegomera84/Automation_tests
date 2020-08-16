"""Script to use the basic commands of the printer K300G through
    methods of the UE2020 source code implemented for python by SWIG."""
import Printer


class PrinterManager(object):

    def __init__(self):
        self.__printer_command = Printer.PrinterCommandsManager
        self.__current_printer_comand = self.__printer_command.getCurrentInstance()
        self.__printer_job = Printer.PrinterJobsManager
        self.__current_printer_job = self.__printer_job.getCurrentInstance()

    def get_printer_version(self):
        """ 
        :return: Model and firmware version of the current printer
        """
        version_printer = bytearray(self.__printer_command.getFirmwareVersion(self.__current_printer_comand))
        print(version_printer)
        version_printer = str(version_printer.strip(), 'utf-8')
        return version_printer

    def get_printer_volt(self):
        """
        :return: Volt of the print
        """
        status_volts_printer = self.__printer_command.getPrinterStatus(self.__current_printer_comand)
        status_volts_printer = str(status_volts_printer[1]) + 'V'
        return str(status_volts_printer)

    def get_printer_temperature(self):
        """"
        :return: Temperture of the print
        """
        status_temperature_printer = self.__printer_command.getPrinterStatus(self.__current_printer_comand)
        return status_temperature_printer[2]

    def get_printer_status(self):
        """
        :return: Printer status codes
        """
        status_printer = self.__printer_command.getPrinterStatus(self.__current_printer_comand)
        return status_printer[0]

    def print_file(self, path_file):
        """
        Send the file contents to print
        :param: path of the file that is required to print
                example: /home/user/Images/picture.jpg
        """
        return  self.__printer_job.printFile(self.__current_printer_job, path_file)
        

 



