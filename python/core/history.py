# write and read like stack
class History:

    def __init__(self, core):
        # core
        self.core = core

        # contents
        self.path = core.const.history_path

    
    def read(self):
        pass

    def save(self, note):
        pass

    def get_last(self):
        pass
