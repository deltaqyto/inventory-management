import yaml

from container import Container


class Manifest:
    def __init__(self, manifest_file_path=None):
        self.storages = []
        
        if manifest_file_path is not None:
            self.load_manifest(manifest_file_path)

    def generate_manifest(self, save_path=None):
        pass

    def load_manifest(self, file_path):
        """Load manifest with provided file path"""
        self.load_manifest_s(open(file_path).read())

    def load_manifest_s(self, manifest_string):
        """Load manifest with provided yaml string"""
        data = yaml.safe_load(manifest_string)
        self.storages = []
        for category, contents in data.items():
            if category.lower() in ["template"]:
                continue
            contents = [c for c in contents if c is not None]

            print(f"C: {category}")
            
            if category.lower() in ["storage"]:
                self.storages = [Container(raw_data=c) for c in contents]
                print(self.storages)
                continue
            #todo spawn item, bind to storage
            print(contents)


def test():
    b3manifest = Manifest("items.yaml")


if __name__ == "__main__":
    test()
