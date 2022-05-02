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

    def subprocess_args(self, include_stdout=True):
        # See https://github.com/pyinstaller/pyinstaller/wiki/Recipe-subprocess
        # for reference and comments.

        kwargs = {
            'stdin': subprocess.PIPE,
            'stderr': subprocess.PIPE,
            'startupinfo': None,
            'env': os.environ,
        }

        if hasattr(subprocess, 'STARTUPINFO'):
            kwargs['startupinfo'] = subprocess.STARTUPINFO()
            kwargs['startupinfo'].dwFlags |= subprocess.STARTF_USESHOWWINDOW
            kwargs['startupinfo'].wShowWindow = subprocess.SW_HIDE

        if include_stdout:
            kwargs['stdout'] = subprocess.PIPE
        else:
            kwargs['stdout'] = subprocess.DEVNULL

        return kwargs

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
    

    #TODO clean up inputs to get rid of uneeded flags
    def run(self, 
        file_location, 
        save_location,
        noise_level = 0, # defult value for algorithm 
        scale = 2, # defult value for algorithm 
        tile_size = None,
        model_path = "models-cunet",
        gpu_id = None,
        load_proc_save = None,
        tta_mode = False,
        output_format = "png"):

        if file_location == None: return 1
        if self.file_type(file_location) not in self.supported_file_types(): return 2


        command = []
        # TODO add checks to see if file paths are valid
        command += (self.binary_location, "-n", self.file_input, "-o",self.save_location)

        if noise_level > 3: return # throw error
        if noise_level > 0: command+= ("-n", noise_level)
        
        algorithms_scales = [1,2,4,8,16,32]

        if scale != 1 and scale in algorithms_scales: command+=("-s", scale)
        if scale not in algorithms_scales: return # throw error

        if tile_size != None: return #throw error if it is anything other than none

        algorithms_models = ["models-cunet", "models-upconv_7_anime_style_art_rgb", "models-upconv_7_photo"]

        if model_path != "algorithms_models" and model_path in algorithms_models: command += ("-m", model_path)
        if model_path not in algorithms_models: return # call error

        if gpu_id != None: return #throw error if it is anything other than none
        if load_proc_save != None: return #throw error if it is anything other than none
        if tta_mode != None: return #throw error if it is anything other than none

        output_formats = ["jpg", "png", "webp"]

        if output_format != "png" and output_format in output_formats: command += ("-f", format)

        try:
            process = subprocess.Popen(command, **self.subprocess_args())
        except:
            #TODO add error handling
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