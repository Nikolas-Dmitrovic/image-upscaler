"""
Wrapper for upscaling algorithms


"""

import os
import subprocess


''' Function return code meanings
1 - no file location found
2 - improper file type


'''



class upscaler():
    def __init__(self, Binary_location = None) -> None:
        self.file_input = None
        self.input_type = None
        self.binary_location = Binary_location
        self.upscale_algorithm = None
        self.save_location = None


    def file_type(self, file):
        pass
        """
        file_type = ...
        
        self.input_type = file_type
        return file_type
        """

    def supported_file_types(self):
        # TODO find all common file types between algoritms
        supported_file_types = {
            'JPNG',
            'PNG'
            }
        return supported_file_types

    # TODO add **args and parse for flags
    # or just have each flag as a kwarg
    def run(self, file_location, save_location):
        # sudo-esk code used a placeholder to show how the command should be structured
        if file_location == None: return 1
        if self.file_type(file_location) not in self.supported_file_types(): return 2

        command = []
        command += (self.binary_location, self.file_input, self.save_location)

        try:
            # TODO create function to send rest of the suprocess args to the open command
            # look at https://github.com/pyinstaller/pyinstaller/wiki/Recipe-subprocess
            proc = subprocess.Popen(command)
        except:
            pass
    def save_file(self):
        pass

    def free_recources(self):
        #deletes downloaded image
        #and upscaled image from local sys
        pass


class wifu2x(upscaler):
    def __init__(self, Binary_location=None) -> None:
        super().__init__(Binary_location)
    
    def run(self):
        pass

class esgran(upscaler):
    def __init__(self, Binary_location=None) -> None:
        super().__init__(Binary_location)

    def run(self):
        pass

class cugan(upscaler):
    def __init__(self, Binary_location=None) -> None:
        super().__init__(Binary_location)

    def run(self):
        pass

class anime4k(upscaler):
    def __init__(self, Binary_location=None) -> None:
        super().__init__(Binary_location)

    def run(self):
        pass