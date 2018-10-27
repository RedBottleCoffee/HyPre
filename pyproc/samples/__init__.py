import numpy as np
from glob import glob
from config import *

file_path_list = glob("samples/**/*")

def categorize(file_path_list):
    noises_list = []
    targets_list = []
    for path in file_path_list:
        if 'noises' in path:
            noises_list.append(path)
        elif 'targets' in path:
            targets_list.append(path)
    return noises_list, targets_list

def one_hot(i, size):
    return list(np.diag([1]*size)[i])

def name_and_category(paths, label):
    return dict(zip(paths, [one_hot(label, conf.num_classes)] * len(paths)))



noises, targets = categorize(file_path_list)

noise_set = name_and_category(noises, 0)
target_set = name_and_category(targets, 1)


dataset = {**noise_set, **target_set}
