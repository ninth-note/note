# base
from configparser import ConfigParser as Parser
from os.path import join

# utils
from utils import PROGRAM_DIR


class Config:

    def __init__(self):
        self.filepath = join(PROGRAM_DIR, "config.ini")
        self._parser = Parser()
        self._parser.read(self.filepath)
   

    def get_section_param(self, section_key, param_key):
        section = self._get_section(section_key)
        try:
            param = section[param_key]
        except KeyError as e:
            msg = f"Config parameter '{param_key}' is missing"
            raise MissingConfigParam(msg) from e
        return param

    def _get_section(self, key):
        try:
            section = self._parser[key]
        except KeyError as e:
            msg = f"Config section '{key}' is missing"
            raise MissingConfigSection(msg) from e
        return section



class ConfigError(Exception):
    """Custom exception for config errors"""
    pass



class MissingConfigSection(ConfigError):
    """Custom exception for missing config section"""
    pass



class MissingConfigParam(ConfigError):
    """Custom exception for missing config param"""
    pass

