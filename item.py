import copy


class Item:
    def __init__(self, description="", quantity=1, location="", modifiers=None, imaged=False):
        self.description = description
        self.quantity = quantity
        self.location = location
        self.modifiers = [] if modifiers is None else modifiers
        self.imaged = imaged

    def split_stack(self, seperation_amount):
        if seperation_amount >= self.quantity:
            raise ValueError(f"{seperation_amount} larger than stack quantity {self.quantity}")

        new_stack = copy.deepcopy(self)
        new_stack.quantity = seperation_amount
        self.quantity -= seperation_amount
        return new_stack
