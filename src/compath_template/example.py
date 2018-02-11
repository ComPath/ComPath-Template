# -*- coding: utf-8 -*-

"""This module contains an example of a parsing method"""

pathway_file = [
    ('pathway_1_id', 'pathway_1_name'),
    ('pathway_2_id', 'pathway_2_name'),
    ('pathway_3_id', 'pathway_3_name'),
    ('pathway_4_id', 'pathway_4_name'),
]

pathway_protein_file = [
    ('gene_symbol_1', 'pathway_1_id'),
    ('gene_symbol_2', 'pathway_2_id'),
    ('gene_symbol_3', 'pathway_3_id'),
    ('gene_symbol_4', 'pathway_4_id')
]


def parse_pathways(pathway_file):
    """Parse a file consisting of lines with pathway database identifier and name"""

    # Magic parsing of the file

    return pathway_file


def parse_pathway_protein(pathway_protein_file):
    """Parse a file consisting of lines with pathway database identifier and protein name"""

    # Magic parsing of the file, look-up for identifiers mapping if it is not a HGNC symbol. You could use PyHGNC for that

    return pathway_protein_file
