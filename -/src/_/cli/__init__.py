# SPDX-FileCopyrightText: 2023-present Mohammad Zain Abbas <mohammadzainabbas@gmail.com>
#
# SPDX-License-Identifier: MIT
import click

from _.__about__ import __version__


@click.group(context_settings={"help_option_names": ["-h", "--help"]}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name=".")
def _():
    click.echo("Hello world!")
