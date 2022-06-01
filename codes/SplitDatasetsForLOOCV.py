"""
This script is used to generate the sub-datasets for LOOCV.
It would create a folder and put the sub-datasets in it, and the number of
sub-datasets would be the same as the number of nodes in the original dataset.

Please note that due to the huge size of gross for all sub-datasets, these subsets
would not be uploaded to GitHub.

To generate these sub-datasets, you just need to put this script into the same
path of the original dataset, change the next two parts (see comments below),
and run it.
"""

import pandas as pd
import os

# 1. `path` should be following format:
#    xxx/.../aaa_bbb.csv, where `_` is used to split the name of the dataset.
path = "EUAir_Transportation_multiplex.csv"

# 2. In addition, the below two indexes are locations of nodes which would
#    be leave out in each iteration.
#    For example, if the dataset has following format as
#       layer, from, to, weight,
#         0,    1,    2,    3,
#    then the indexes of nodes should be 1 and 2.
from_node = 1
to_node = 2

################################################################################

folder = "LOOCV_subdatasets_" + path.split("_")[0]
os.mkdir(folder)

dataset = pd.read_csv(path, header=None)

all_nodes = list(set(list(dataset[from_node]) + list(dataset[to_node])))

for leave_node in all_nodes:
    sub_dataset = dataset[
        (dataset[from_node] != leave_node) & (dataset[to_node] != leave_node)
    ]
    new_path = folder + "/%s_%s.csv" % (path.split("_")[0], str(leave_node))
    sub_dataset.to_csv(new_path, index=None, header=None)
