from importlib.resources import path
import os
import glob

import numpy as np
import cv2 as cv
from torch import imag


patch_shape = None


def overlay_pathes(images, patch, position=[100, 500]):
    x, y = position
    patch_size = patch_shape[0]
    images[:, x:x + patch_size, y: y + patch_size, :] = patch
    return images


def prepare_patch(path_to_patch):
    assert os.path.isfile(path_to_patch), f"{path_to_patch}, doesn't exists"
    patch: np.ndarray = cv.imread(path_to_patch)
    print("orig shape:", patch.shape)
    patch = cv.resize(patch, (153, 153))
    print("resized shape:", patch.shape)
    global patch_shape
    patch_shape = patch.shape[:2]
    return patch


def save_attacked_images(folder, images, images_list):
    os.makedirs(folder, exist_ok=True)
    image_names = [i.split("/")[-1] for i in images_list]
    for i_name, image in zip(image_names, images):
        cv.imwrite(f"{folder}/{i_name}", image)
    


def main():
    patch_path = "patches/Upatch1.png"
    # patch_path = "patches/white.png"



    patch = prepare_patch(patch_path)
    images_dir = "images/"
    images_dir = "/home/hd/Projects/Rsrch/ucu/flownet2-pytorch/MPI-Sintel/training/final/alley_1"
    images_files = glob.glob(os.path.join(images_dir, '*.png')) + \
                   glob.glob(os.path.join(images_dir, '*.jpg'))
    print(images_files)
    images = np.array([cv.imread(i) for i in images_files])
    print("images shape: ", images.shape)
    attacked_images = overlay_pathes(images, patch)

    attacked_dir = f"{images_dir}_att"
    save_attacked_images(attacked_dir, attacked_images, images_files)



if __name__ == "__main__":
    main()
