import glob
import os

import numpy as np

from metric import end_point_error_map
from flo_utils import readFlow


gt_dir = "/home/hd/Projects/Rsrch/ucu/flownet2-pytorch/MPI-Sintel/training/flow/alley_1/"
pred_dir = "/home/hd/Projects/Rsrch/ucu/flownet2-pytorch/MPI-Sintel/training/final/alley_1_att/flow/"


def run_metric_dir(gt_dir, pred_dir):
    gt_files = glob.glob(os.path.join(gt_dir, '*.flo'))
    gt_files = np.sort(gt_files)

    pred_files = glob.glob(os.path.join(pred_dir, '*.flo'))
    pred_files = np.sort(pred_files)

    average_metric = []

    for gt_file, pred_file in zip(gt_files, pred_files):
        print(gt_file, pred_file)
        gt = readFlow(gt_file)
        pred = readFlow(pred_file)
        value = end_point_error_map(pred, gt)
        average_metric.append(value)
    average_metric = np.array(average_metric)
    print(average_metric.mean())

run_metric_dir(gt_dir, pred_dir)
