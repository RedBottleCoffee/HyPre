import numpy as np
from glob import glob
from config import *

file_path_list = glob("samples/**/*")

#== ディレクトリから音声をカテゴライズ
def categorize(file_path_list):
    noises_list = []
    targets_list = []
    for path in file_path_list:
        if 'noises' in path:
            noises_list.append(path)
        elif 'finger' in path:
            targets_list.append(path)
    return noises_list, targets_list

#== One-Hot表現生成
def one_hot(i, size):
    return list(np.diag([1]*size)[i])

#== ファイル名と正解ラベル(One-Hot)の対応づけ
def name_and_category(paths, label):
    return dict(zip(paths, [one_hot(label, conf.num_classes)] * len(paths)))



noises, targets = categorize(file_path_list)

noise_set = name_and_category(noises, 0)
target_set = name_and_category(targets, 1)


dataset = {**noise_set, **target_set}
