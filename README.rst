ComPath Template Package
========================

A template package for integrating new pathway databases to `ComPath <https://github.com/compath/compath>`_. 

Package Structure
-----------------

The template contains the following modules:

- manager.py: Implements the database manager, as well as useful commands for querying and populating. Here, it needs to be implemented a parser adapting the new pathway-protein association file. The parser should process the file to an iterator where each iteration contains the gene as well as the pathway level linkage.

- models.py: Defines the database model. By default, each ComPath pathway package (following the `Bio2BEL <https://github.com/bio2bel>`_. structure) should contain at least the following two models:

   1. Pathway model: containing the name of the pathway and the link with the Protein model.
   2. Protein model: containing the HGNC symbol of the gene coding for the protein.

- cli.py: Defines all commands to manage the package. By default, we have defined the 'populate' and drop' commands that correspondingly load and erase the database.

- constants.py: Contain the constants needed for the package such as name, or URLs from the pathway database RESTful APi.

All modules described above contain the minimum methods for their compatibility with `ComPath <https://github.com/compath/compath>`_. A list of 'TODOs' is included within each package stating what needs to be added. Furthermore, the 'example' module outlines a parser example. A mature example of a ComPath template would be `ComPath HGNC <https://github.com/compath/compath_hgnc>`_.
