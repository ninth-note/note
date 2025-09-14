class History:

    def __init__(self, core):
        # core
        self.core = core

        # contents
        self.path = core.const.locations.history_path
        self.size = core.const.settings.history_size

    
    def load(self):
        data = []
        with open(self.path, "r") as file:
            data = [line.strip() for line in file]
        return data


    def get(self, index):
        data = self.load()
        return data[index]


    def get_latest(self):
        data = self.load()
        return data[0]


    def scan(self, pattern):
       pass 


    def save(self, entry):
        data = self.load()

        if entry in data:
            data.remove(entry)

        data.insert(0, entry)

        # Keep only the first 5 but later 100 lines
        # actually make this a setting in the conf
        data = data[:100]

        with open(self.path, "w") as file:
            for item in data:
                file.write(item + "\n")

        



