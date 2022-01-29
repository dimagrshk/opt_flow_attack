import glob
from os import makedirs
from os.path import join


from mmflow.apis import inference_model, init_model
import flowiz as fz
import cv2 as cv
import numpy as np
from PIL import Image
from tqdm import tqdm

from model_config import MODELS
from flo_utils import writeFlow

config_file, checkpoint_file = MODELS["flownetc"]

print("settings:", config_file, checkpoint_file)

data_dir = "/home/hd/Projects/Rsrch/ucu/flownet2-pytorch/MPI-Sintel/training/final/alley_1_att"
flo_out_dir = join(data_dir, "flow")

device = 'cuda:0'
model = init_model(config_file, checkpoint_file, device=device)



def run_model_dir(model, data_dir, flo_out_dir, vizualize=True):
    makedirs(flo_out_dir, exist_ok=True)
    images = glob.glob(join(data_dir, '*.png')) + \
                    glob.glob(join(data_dir, '*.jpg'))

    images = np.sort(images)

    print(images)

    for imfile1, imfile2 in tqdm(zip(images[:-1], images[1:])):
        fl = inference_model(model, imfile1, imfile2)
        flo_name = join(flo_out_dir, imfile1.split("/")[-1].split(".")[0])
        writeFlow(f"{flo_name}.flo", fl)
        if vizualize:
            uv = fz.convert_from_flow(fl, mode='RGB')
            Image.fromarray(uv).save(f"{flo_name}.png")


run_model_dir(model, data_dir, flo_out_dir, True)
