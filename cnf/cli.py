# -*- coding: utf-8 -*-

"""Console script for {{cookiecutter.project_slug}}."""
import click
from . gen import gen


@click.group()
def entry_point():
    pass


entry_point.add_command(gen)
