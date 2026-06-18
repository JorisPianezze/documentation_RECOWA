.. _installation:

Installation
*********************************************************

You have the flexibility to download and compile models in any directory you prefer.
However, I recommend dedicating a specific directory for your case study, particularly if you plan to test new versions of models, compilers, or libraries.

.. note::

   The :ref:`download` and :ref:`compilation` steps must be performed on the machines where you will run the simulations.

To get the models template directory, do :

.. code-block:: bash

   git clone https://github.com/JorisPianezze/models_recowa.git

Rename the directory into your own project : 

.. code-block:: bash

   mv models_recowa models_YOURPROJECT

Configure your environment
=========================================================

This coupling system has been tested on several machines. First you need to verify your maching with

.. code-block:: bash

   cd models_YOURPROJECT
   ./create_environment.sh

If your machine has already been tested you need to have a script :file:`environment.sh` inside models_YOURPROJECT directory.

.. note::

   * This environment has already been tested in your machine.
   * Different scripts will call :file:`environment.sh` file. You also have to use this script when you will compile and run models.

.. _download_libraries:

Download the libraries
====================================

First, you need to download and install NetCDF library. To download tar.gz files, do :

.. code-block:: bash

   cd models_YOURPROJECT/libraries
   ./download.sh

You need to have 4 new tar.gz files in the libraries directory.

.. _download_models:

Download the models
====================================

To download the models already testd in your machine, you can execute this file :

.. code-block:: bash

   cd models_YOURPROJECT
   ./download_models.sh

.. _check_installation:

Check tree
=================================

At the end of this section, you need to have following script and directories :

.. tab-set::

   .. tab-item:: Laptop Ubuntu 20.04

      .. include:: check_tree_laptop_joris.rst
