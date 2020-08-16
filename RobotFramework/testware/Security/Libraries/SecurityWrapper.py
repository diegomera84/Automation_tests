"""Script to use the basic commands of the MSE  through
    methods of the UE2020 source code implemented for python by SWIG."""
import Security

class SecurityWrapper(object):
        
    def __init__(self):
        
        self.__current_hash_comand = Security.SecurityController_getCurrentInstance()
        self.__mse_command = Security.MseCommandsManager.getCurrentInstance()

    def mse_initialize(self):
        """ 
        :return: MSE initialization
        """
        initialize = self.__mse_command.initialize()
        print(initialize)
        return initialize

    def get_mse_version(self):
        """ 
        :return: Model and firmware version of the MSE
        """
        version_mse = self.__mse_command.getMseFirmwareVersion()
        print(version_mse)
        return version_mse

    def get_hash(self, path_file):
        """
        :return: Hash SHA3-512 of file
        """
        self.__mse_command.close()
        code = Security.HashCode_SHA3_512
        file_hash = self.__current_hash_comand.getHashFromFile(path_file, code)
        return file_hash

    
    