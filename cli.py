#!/usr/bin/python3
import click
import logging
import sys
import os
import warnings
from timeit import default_timer as timer
import pkg_resources
from rich.logging import RichHandler
__version__ = pkg_resources.require("fossiler")[0].version


# CLI entry point
@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.option('--verbosity', '-v', type=click.Choice(['info', 'debug']),
    default='info', help="Verbosity level, default = info.")
def cli(verbosity):
    """
    fossiler - Copyright (C) 2023-2024 Hengchi Chen\n
    Contact: heche@psb.vib-ugent.be
    """
    logging.basicConfig(
        format='%(message)s',
        handlers=[RichHandler()],
        datefmt='%H:%M:%S',
        level=verbosity.upper())
    logging.info("This is fossiler v{}".format(__version__))
    pass


# Diamond and gene families
@cli.command(context_settings={'help_option_names': ['-h', '--help']})
@click.argument('sequences', nargs=-1, type=click.Path(exists=True))
@click.option('--outdir', '-o', default='fossiler_find', show_default=True, help='output directory')
@click.option('--clades', '-c', default=None, show_default=True, help='clade names')
@click.option('--rocks', '-r', default=None, type = int, show_default=True, help='Rock IDs')
def find(**kwargs):
    """
    Find available fossils
    """
    _find(**kwargs)

def _find(sequences,outdir,clades,rocks):
    from fossiler.fossils import rawfossils,cooccurancerecords
    rawfossils(clades)
    cooccurancerecords(rocks)


if __name__ == '__main__':
    start = timer()
    cli()
    end = timer()
    logging.info("Total run time: {}s".format(int(end-start)))
