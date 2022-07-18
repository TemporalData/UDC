# Imports
from tensorboard.plugins import projector
import pandas as pd
import numpy as np
from torch.utils.tensorboard import SummaryWriter

# Load vectors and labels
vectors = pd.read_csv('data/input/model_simcse_data_dental_vectors.tsv', sep='\t', header=None)
labels = pd.read_csv('data/input/test_labels.tsv', sep='\t')

# 
writer = SummaryWriter()
writer.add_embedding(np.array(vectors),np.array(labels).tolist())
writer.close()

