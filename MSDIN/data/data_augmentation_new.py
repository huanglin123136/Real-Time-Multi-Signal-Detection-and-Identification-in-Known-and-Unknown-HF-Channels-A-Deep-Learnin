import numpy as np
import torch
# from data_plot import draw_plot


def sample_filplr(data,data_80,label):
    # data = np.array(data)
    # label = np.array(label)
    data = data[:, ::-1]
    data_80 = data_80[:, ::-1]

    label = label.reshape(-1, 3)
    len = label.shape[0]
    for i in range(len):
        label[:, i * 3: i * 3 + 2] = 1.0 - label[:, i * 3: i * 3 + 2]
        label[:, i * 3: i * 3 + 2] = label[:, i * 3: i * 3 + 2][:, ::-1]

    return data.copy(),data_80.copy(), label


def sample_up_filplr(data,data_80,label):

    data = data[::-1,:]
    data_80 = data_80[::-1,:]

    return data.copy(),data_80.copy(), label

def sample_shift(data,data_80,label):
    # data = np.array(data)
    # label = np.array(label)
    label = label.reshape(-1, 3)
    len = label.shape[0]
    sample_len = data.shape[1]
    min_value = 1
    for i in range(len):
       min_value = min(min_value, label[i][0])
    shift_ = np.random.uniform(0, 1, 1) * max(min_value, 0)

    shift = int(shift_ * sample_len)
    new_data = data.copy()
    new_data[:, :(sample_len - shift)] = data[:, shift:]
    new_data[:, sample_len - shift:] = data[:, :shift]



    sample_len80 = data_80.shape[-1]
    shift80 = int(shift_ * sample_len80)
    new_data80 = data_80.copy()
    new_data80[:, :(sample_len80 - shift80)] = data_80[:, shift80:]
    new_data80[:, sample_len80 - shift80:] = data_80[:, :shift80]

    for i in range(len):
        label[:, i * 3: i * 3 + 2] = label[:, i * 3: i * 3 + 2] - shift_

    # import scipy.io as scio
    # scio.savemat('1.mat', {'new_data': new_data, 'new_dataRC20': new_dataRC20,'new_dataRC40': new_dataRC40,'label':label})
    return new_data,new_data80,label


def sample_jitter(data,data_80, sample):
    factor = np.random.uniform(0, 1, 1) * 0.1 + 0.95
    add_items = np.random.uniform(0, 1, 1) * 0.05 - 0.025
    data = data * factor + add_items
    data_80 = data_80 * factor + add_items

    return data,data_80, sample
