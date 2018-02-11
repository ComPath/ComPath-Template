ComPath Template Package
========================

A template package for integrating new pathway databases to ComPath. 

Package Structure
-----------------

The template contains the following modules:

- manager.py: Implements the database manager, as well as useful commands for querying and populating. Here, it needs to be implemented a parser adapting the new pathway-protein association file. The parser should process the file to an iterator where each iteration contains the gene as well as the pathway level linkage.

- models.py: Defines the database model. By default, each Bio2BEL pathway package should contain two models:
  1. Pathway model: containing the name of the pathway and the link with the Protein model.
  2. Protein model: containing the HGNC symbol of the gene coding for the protein.

- cli.py: Defines all commands to manage the package. By default, we have defined the 'populate' and drop' commands that correspondingly load and erase the database.

- constants.py: Contain the constants needed for the package such as name, or URLs from the pathway database RESTful APi.
