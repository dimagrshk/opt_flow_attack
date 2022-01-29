# Attacking Optical Flow

This project is based on the [Attacking Optical Flow](https://arxiv.org/abs/1910.10053). Authors shows that adversarial attacks can corrupt optical flow estimation and tests different architectures. In general latest approaches have more stable behavior.  
Code is based on [mmflow](https://mmflow.readthedocs.io/en/latest/) framework.


## Purpose of this work

[x] Collect models for optical flow estimation and make it runnable to test  
[x] Reproduce adversarial attack as it shown in the paper  
[] Attempt to optimize specific adversarial patch for selected models  

### Selected models
- [Flownet](https://arxiv.org/abs/1504.06852)
- [PWCnet](https://arxiv.org/abs/1709.02371)
- [RAFT](https://arxiv.org/abs/2003.12039)


### Dataset
[Sintel](http://sintel.is.tue.mpg.de/) dataset were selected for testing and reproducing.

### Experiments  
For each model were 3 runs without any patches, with white patch, with universal patch.  
- [White patch](patches/white.png)
- [Universal patch](patches/Upatch1.png)


### Metric
EPE was used to measure impact of adding patches.

## Metric Results

| Model   | Baseline | White Patch  | Adversarial  patch |
| :------:|:--------:| ------------:|:------------------:|
| FlowNet | 4.5552   | 6.3561       | 6.578              |
| PWCnet  | 2.012    | 4.308        | 4.437              |
| RAFT    | 1.471    | 3.731        | 3.844              |


## Visual Results
[Link]() to gdrive with `.mp4`

### TODO

[] Test on more datasets  
[] Attempt to optimize specific patch
