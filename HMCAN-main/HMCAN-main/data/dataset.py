import torch
from torch.utils.data import Dataset
import numpy as np


class Dataset(Dataset):
    def __init__(self, data_label_list_path, data_vgg_list_path, data_bert_list_path, index_id=None):

        data_labels = np.array(torch.load(data_label_list_path)).astype("int")
        data_vgg = torch.load(data_vgg_list_path)
        x_features = torch.load(data_bert_list_path)


        if index_id != None:
            data_labels = data_labels[index_id]
            data_vgg = data_vgg[index_id]
            x_features = x_features[index_id]

        self.data_labels = data_labels
        self.data_vgg = data_vgg
        self.x_features = x_features

'''
data_label_list_path：用于加载数据标签的文件路径。
data_vgg_list_path：用于加载VGG特征数据的文件路径。
data_bert_list_path：用于加载Bert特征数据的文件路径。
index_id：可选参数，如果提供了这个参数，它会用来选择特定的数据子集，即仅选择指定索引的数据。
'''

    def __len__(self):
        return len(self.data_labels)

    def __getitem__(self, index):
        return index, \
               self.data_labels[index], \
               self.data_vgg[index], \
               self.x_features[index]
