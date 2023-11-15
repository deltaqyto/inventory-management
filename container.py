

class Container:
    def __init__(self, raw_data=None, description=None, stacks=None, location=""):
        if raw_data is not None:
            self.load_from_raw(raw_data)
        self.stacks = [] if stacks is None else stacks
        self.location = location
        #todo error if no desc provided

    def load_from_raw(self, data):
        #todo

    def __repr__(self):
        return f"Container({self.location + ', ' if self.location else ''}{self.stacks})"
