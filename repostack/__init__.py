# -*- coding: utf-8 -*-

import os
import importlib

import click


__version__ = '0.0.6'
VERSION = tuple(map(int, __version__.split('.')))

plugin_folder = os.path.dirname(__file__)


class CLI(click.MultiCommand):

    def list_commands(self, ctx):
        return sorted(self.cmds.keys())

    def get_command(self, ctx, name):
        return self.cmds[name]

    @property
    def cmds(self):
        if not hasattr(self, '_cmds'):
            filenames = [fn[:-3] for fn in os.listdir(plugin_folder) if fn.endswith('.py') and fn != '__init__.py']
            self._cmds = {}
            for fn in filenames:
                module = importlib.import_module('.' + fn, __name__)
                for cmd in getattr(module, 'cmds', []):
                    self._cmds[cmd.name] = cmd
        return self._cmds


@click.command(cls=CLI)
@click.version_option()
def cli():
    pass
