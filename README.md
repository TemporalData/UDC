# Unsupervised Document Clustering - Master Thesis

## Abstract

The aim of this paper is to discover a method of finding semantically similar clusters
from a text dataset in an unsupervised manner. An existing semantic text similarity
benchmark will be used to substantiate the use of embeddings for this task. The
embeddings will represent the entire text input using state of the art sentence trans-
formers. These transformers will be combined with contrastive learning to further
enhance the embeddings using state of the art research. By using transfer learning
during this process this work can utilize the pre-trained models of previous research
and retain their performance. These techniques will be applied to dental patient
data. Resulting in visualizations that allow for exploration of the proposed clusters.

## Structure of Project

    .
    ├── Clustering                  # Code used for clustering
    ├── Embeddings	                # Code for generating the embeddings
	│   ├── SimCSE	                   # The official SimCSE repository
	│   ├── simcse_generation	   # Scripts used to train the simcse model
	│   └── word2vec	           # Scripts used to train the word2vec model
	├── Preprocessing	        # Extracting relevant data from the raw files
	│   └── visualization	            # Charts used in the report
	├── Visualization	        # Contains code for visualizing the embeddings
	│   ├── models/dental_simcse        # Stores the embeddings from the dental simcse model
    │   └── tensorboard_dir		    # Stores the required files for the tensorboard visualization
    └── README.md		        # Description file
	
## Download and Usage

All the code uses [poetry](https://python-poetry.org/docs/) for the virtual environments.
The one exception is the simcse generation, for that virtual environment use pip.

Set the python version to 3.9.13 using poetry.

Go to the directory of choice, 

Run `poetry install`

Then run `poetry shell` and open a jupyter notebook or run the *.py* scripts.

## Dependencies

Refer to the respective *pyproject.toml* files in each directory

## Bugs

Find a bug in the project? [Open a new issue on GitHub](https://github.com/TemporalData/UDC/issues)




