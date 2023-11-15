import yaml
import logging


class Item:
    def __init__(self, yaml_string=None, description=None, location=None, modifiers=None, imaged=False, logger=None):
        self.logger = logging.getLogger(__name__) if logger is None else logger
        if yaml_string:
            self.load_from_yaml(yaml_string)
        else:
            self.description = description
            self.location = location
            self.modifiers = [] if modifiers is None else modifiers
            self.imaged = imaged

    # todo error if no desc provided
    def clear(self):
        self.description = None
        self.location = None
        self.modifiers = []
        self.imaged = None

    def load_from_yaml(self, yaml_string):
        self.clear()
        data = yaml.safe_load(yaml_string)

        # Expected keys
        expected_keys = {"d", "loc", "modifier", "imaged"}

        # Check the type of parsed data
        if isinstance(data, dict):
            # Normalize keys to lowercase and process
            for key, value in data.items():
                key_lower = key.lower()
                if key_lower == "d":
                    self.description = value
                elif key_lower == "loc":
                    self.location = value
                elif key_lower == "modifier":
                    self.modifiers = value
                elif key_lower == "imaged":
                    self.imaged = value
                else:
                    # Log unexpected keys
                    self.logger.warning(f"Unexpected key '{key}' in YAML data")

        elif isinstance(data, str):
            # Process string data as description
            self.description = data
        else:
            # Raise an error for invalid data type
            raise ValueError("YAML string must be either a dictionary for item properties or a string for description")
