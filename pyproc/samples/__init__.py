import numpy as np
from glob import glob
from config import *

file_path_list = glob("samples/**/*")

#== ディレクトリから音声をカテゴライズ
def categorize(file_path_list):
    labels = conf.labels
    catg_dict = dict([(label.lower(), []) for label in labels])
    for path in file_path_list:
        if '__' in path: continue
        catg_dict[path.split('/')[-2]].append(path)
    return catg_dict

#== One-Hot表現生成
def one_hot(i, size):
    return list(np.diag([1]*size)[i])

#== ファイル名と正解ラベル(One-Hot)の対応づけ
def name_and_category(paths, label):
    return dict(zip(paths, [one_hot(label, conf.num_classes)] * len(paths)))



categories = categorize(file_path_list)
backet = {}

for k, v in categories.items():
    print(k)
    print(v)
    spec = name_and_category(v, conf.labels.index(k))
    backet = {**backet, **spec}


dataset = backet
