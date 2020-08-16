"""Script to use the basic commands of the Keyboard through
    methods of the UE2020 source code implemented for python by SWIG."""
import Keyboard


class KeyboardManager(object):

    def __init__(self):
        self.__keyboard_command = Keyboard.KeyboardController
        self.__current_keyboard_command = self.__keyboard_command.getCurrentInstance()
        
    def keyboard_initialize(self):
        """
        :initialize the keyboard connection
        """
        keyboard_connection = self.__keyboard_command.initialize(self.__current_keyboard_command)
        return keyboard_connection

    def get_keyboard_version(self):
        """ 
        :return: Model and firmware version of the current keyboard
        """
        version_keyboard = self.__keyboard_command.getFirmwareVersion(self.__current_keyboard_command)
        print(version_keyboard)
        return version_keyboard

    def get_keyboard_randomnumber(self, number_size):
        """"
        :return: Randon number
        """
        keyboard_randon = self.__keyboard_command.getRandomNumber(self.__current_keyboard_command, number_size)
        keyboard_randon = list(keyboard_randon)
        del keyboard_randon[0:13]
        print(keyboard_randon)
        return keyboard_randon

    def check_event(self):
        """
        :get the keyboard event
        """
        return  self.__keyboard_command.checkEvent(self.__current_keyboard_command)
        

 
