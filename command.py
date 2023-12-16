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


# cli entry point
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


# Find fossils
@cli.command(context_settings={'help_option_names': ['-h', '--help']})
@click.option('--outdir', '-o', default='fossiler_find', show_default=True, help='output directory')
@click.option('--clades', '-c', default=None, show_default=True, help='clade names')
@click.option('--rocks', '-r', default=None, type = int, show_default=True, help='rock IDs')
@click.option('--tree', '-t', default=None, show_default=True, help='tree file in newick')
@click.option('--getsp', '-gs', is_flag=True, help='get species in starting tree')
@click.option('--number', '-n', default=19, show_default=True, help='number of species in the starting tree')
@click.option('--getaxonomy', '-gt', default=None, show_default=True, help='get taxonomy of a given species name')
@click.option('--mcmctreeformat', '-mf', is_flag=True, help='get mcmctree format output')
@click.option('--wholetree', '-wt', is_flag=True, help='use the whole angiosperm tree infomation')
@click.option('--setconserved', '-sc', is_flag=True, help='adopt the same maximum constraint as (Morris et al., 2018)')
@click.option('--onlyone', '-oo', is_flag=True, help='get only one species per order')
def find(**kwargs):
    """
    Find available fossils
    """
    _find(**kwargs)

def _find(tree,outdir,clades,rocks,getaxonomy,mcmctreeformat,wholetree,setconserved,getsp,number,onlyone):
    from fossiler.fossils import rawfossils,cooccurancerecords,gettreewithfossil,standalonetaxonomy,getproperstartingtree
    if clades != None: rawfossils(clades)
    if rocks !=None: cooccurancerecords(rocks)
    if tree != None:
        treef = gettreewithfossil(tree,formatt=mcmctreeformat,wholetree=wholetree,Yang=setconserved)
        if getsp: getproperstartingtree(treef,number,outdir,onlyone=onlyone)
    if getaxonomy!= None: standalonetaxonomy(getaxonomy)


if __name__ == '__main__':
    start = timer()
    cli()
    end = timer()
    logging.info("Total run time: {}s".format(int(end-start)))
