# base
from os import environ
from os.path import join

# config exceptions
from core.config import ConfigError


class Settings:

    def __init__(self, conf):
        self.conf = conf

 
    @property
    def history_size(self):
        default_size = 10
        try: 
            return self.conf.get_section_param("history", "size")
        except ConfigError as e:
            print(e)
            return default_size

