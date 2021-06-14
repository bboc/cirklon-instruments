import argparse
import json
import os
import yaml

CKI_DIR = "instruments.cki"
YAML_DIR = "instr.src"

CKI_FILENAME_TEMPLATE = "%s.cki"
YAML_FILENAME_TEMPLATE = "%s.yaml"

# CKI predefined keys
INSTRUMENT_DATA = 'instrument_data'

# ?
TRACK_VALUES = 'track_values'
ROW_DEFS = 'row_defs'
CC_DEFS = 'CC_defs'

# slot types
MIDI_CC = 'MIDI_CC'
TRACK_CONTROL = 'track_control'


def load_yaml(source):
    with open(os.path.join(os.path.join(YAML_DIR, source)), 'r') as infile:
        return yaml.load(infile, Loader=yaml.FullLoader)


def write_json(target, data):
    with open(os.path.join(os.path.join(CKI_DIR, target)), 'w') as outfile:
        json.dump(data, outfile, indent=4)


class CirklonInstrument(object):

    def __init__(self, name):
        self.name = name
        self.raw_data = {}
        self.cki_data = {INSTRUMENT_DATA: {}}

    def make(self):
        self.raw_data = load_yaml(YAML_FILENAME_TEMPLATE % self.name)
        for instrument in self.raw_data:
            self.cki_data[INSTRUMENT_DATA][instrument] = self.process_instrument(self.raw_data[instrument])

        write_json(CKI_FILENAME_TEMPLATE % self.name, self.cki_data)

    def process_instrument(self, raw_instrument):
        """
        Convert an instrument definition in simplified YAML format
        to CKI format, build CC_defs if necessary.
        """
        instrument_data = {}

        # copy instrument parameters
        for item in raw_instrument:
            if item not in [TRACK_VALUES, ROW_DEFS]:
                instrument_data[item] = raw_instrument[item]

        track_values, midi_cc_data, cc_defs_required = self._make_track_data(raw_instrument)

        instrument_data[TRACK_VALUES] = track_values

        # make CC_defs (ic necessary)
        if cc_defs_required:
            instrument_data[CC_DEFS] = self._make_cc_defs(midi_cc_data)

        if ROW_DEFS in raw_instrument:
            row_defs = {}
            for row in raw_instrument[ROW_DEFS]:
                note = row[0]
                label = row[1]
                if len(row) > 2:
                    always_show = row[2]
                else:
                    always_show = True
                row_defs[note] = {"label": label, "always_show": always_show}

        instrument_data[ROW_DEFS] = row_defs
        return instrument_data

    def _make_track_data(self, raw_instrument):

        track_values = {}
        midi_cc_data = []  # store cc data to create CC_defs if necessary
        cc_defs_required = False
        slot = 1

        # make track_values
        for item in raw_instrument[TRACK_VALUES]:
            # "slot_1" : { "track_control" : "pgm" },
            # "slot_2" : { "MIDI_CC" : 70, "label" : "Circut" },
            if isinstance(item[0], int):
                # update slot number
                slot = item[0]
                item = item[1:]
            if len(item) > 3:
                cc_defs_required = True
            if item[0] == 'CC':
                slot_data = {
                    "MIDI_CC": item[1],
                    "label": item[2],
                }
                # store for later
                midi_cc_data.append(item[1:])
            elif item[0] == 'track':
                slot_data = {
                    TRACK_CONTROL: item[1]
                }
            else:
                raise Exception("Item is broken %s" % repr(item))

            track_values['slot_%s' % slot] = slot_data
            # increment slot!
            slot = slot + 1

        return track_values, midi_cc_data, cc_defs_required

    def _make_cc_defs(self, midi_cc_data):
        # "CC_9" : { "label" : "EQLow", "min_val" : 0, "max_val" : 127, "start_val" : 64 },
        cc_defs = {}
        for item in midi_cc_data:
            # [2, "SomeCt", 0, 127]
            # generates in CC_defs: "CC_2" : { "label" : "SomeCt", "min_val" : 0, "max_val" : 127 },
            # [3, "Switch1", 0, 4, 2]
            # generates "CC_3" : { "label" : "Switch1", "min_val" : 0, "max_val" : 4, "start_val" : 2 }
            cc_data = {
                'label': item[1]
            }
            if len(item) > 2:
                cc_data['min_val'] = item[2]
            if len(item) > 3:
                cc_data['max_val'] = item[3]
            if len(item) > 4:
                cc_data['start_val'] = item[4]

            cc_defs["CC_%s" % item[0]] = cc_data
        return cc_defs


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Create a Cirklon instrument definition file from a YAML file.')
    parser.add_argument('name', type=str,
                        help="Name of YAML file in instr.src (without extension")

    args = parser.parse_args()
    ci = CirklonInstrument(args.name)
    ci.make()
