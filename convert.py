import yaml
import json
import os

CKI_DIR = "instruments.cki"
YAML_DIR = "instr.src"


def json2yaml(source, target):
    with open(os.path.join(os.path.join(CKI_DIR, source)), 'r') as infile:
        data = json.load(infile)
        print(data)
        return
    with open(os.path.join(os.path.join(YAML_DIR, target)), 'w') as outfile:
        yaml.dump(data, outfile, allow_unicode=True)


def yaml2json(source, target):
    "Simply convert YAML to JSON file, no processing"
    with open(os.path.join(os.path.join(YAML_DIR, source)), 'r') as infile:
        data = yaml.load(infile, Loader=yaml.FullLoader)

    with open(os.path.join(os.path.join(CKI_DIR, target)), 'w') as outfile:
        json.dump(data, outfile, indent=4)


def load_yaml(source):
    with open(os.path.join(os.path.join(YAML_DIR, source)), 'r') as infile:
        return yaml.load(infile, Loader=yaml.FullLoader)


def yaml2cki(name):
    ci = CirklonInstrument(name)
    ci.make()


class CirklonInstrument(object):

    def __init__(self, name):
        self.name = name
        self.raw_data = {}
        self.cki_data = {'instrument.data': {}}

    def make(self):
        """
        Convert an instrument definition in simplified YAML format
        to CKI format, build CC_defs if necessary.
        """
        self.raw_data = load_yaml("%s.yaml" % self.name)
        print(self.raw_data)
        # TODO: copy instrument parameters
        for instrument in self.raw_data:
            self.process_instrument(self.raw_data['instrument'])

        return

        target = "%s.cki" % self.name
        with open(os.path.join(os.path.join(CKI_DIR, target)), 'w') as outfile:
            json.dump(self.cki_data, outfile, indent=4)


    def process_instrument(self, instrument):
        track_values = {}
        CC_defs = None
        slot = 1


        return track_values, CC_defs


if __name__ == "__main__":
    json2yaml("Ju06.cki", 'Ju06.yaml')
    # json2yaml("Waldorf Q.cki", 'Waldorf Q.yaml')
    # yaml2json("Ju06.yaml", 'Ju06-2.cki')

    #yaml2cki('Roland Sh-01a.yaml', 'Roland sh-01a.cki')
