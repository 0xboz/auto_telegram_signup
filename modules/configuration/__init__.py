#!/usr/bin/env python
import os
import json
from configparser import ConfigParser


class Configuration:
    """
    Configuration file object
    The app has an initial configuration file named config.ini
    After the first run, additional params can be saved into a new configuration file named config.json
    The app can resume from the last exit by using config.json
    """

    def __init__(self):
        self.cwd = os.getcwd()
        self.cfg_ini = os.path.join(self.cwd, 'config.ini')
        self.cfg_json = os.path.join(self.cwd, 'config.json')

    def load(self):
        # Use config.json and resume the program from the last exit
        if os.path.exists(self.cfg_json):
            with open(self.cfg_json, 'r') as f:
                return json.load(f)
        # The first-run uses config.ini instead
        else:
            cfg_parser = ConfigParser()
            cfg_parser.read(self.cfg_ini)
            return dict(cfg_parser._sections)

    def save(self, cfg_dict):
        """
        Use this function to save additional params as needed
        """
        self.cfg_json = os.path.join(self.cwd, 'config.json')
        with open(self.cfg_json, 'w') as f:
            json.dump(cfg_dict, f, indent=4)
