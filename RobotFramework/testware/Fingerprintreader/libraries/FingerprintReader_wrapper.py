"""Script to use the basic commands of the Fingerprint Reader through
    methods of the UE2020 source code implemented for python by SWIG."""
import FingerprintReader
from PIL import Image


class FPRManager(object):

    def __init__(self):
        self.__FPR_command = FingerprintReader.FingerprintReaderController
        self.__current_FPR_comand = self.__FPR_command.getCurrentInstance()

    def get_FPR_version(self):
        """ 
        :return: Model and firmware version of the current FPR
        """
        version_FPR = self.__FPR_command.getFirmwareVersion(self.__current_FPR_comand)
        print(version_FPR)
        return version_FPR

    def connect_FPR(self):
        """
        :Connect with FingerPrintReader
        """
        connect = self.__FPR_command.connect(self.__current_FPR_comand)
        print(connect)
        return connect

    def disconnect_FPR(self):
        """
        :Disconnect with FingerPrintReader
        """
        disconnect = self.__FPR_command.disconnect(self.__current_FPR_comand)
        print(disconnect)
        return disconnect

    def get_FPR_frame(self):
        """"
        :return: Fingerprint frame
        """
        while True:
            fingerprint_frame = self.__FPR_command.getFrame(self.__current_FPR_comand)
            if fingerprint_frame.isFingerPresent and fingerprint_frame.isFinalFrame:
                finger_image = bytes(fingerprint_frame.data)
                img_size = (500, 500)
                img = Image.frombytes('L', img_size, finger_image)
                img.save("fingerprint.png")
                break
        print(fingerprint_frame.data)
        return fingerprint_frame.data

   
