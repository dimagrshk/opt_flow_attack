MODELS = {
    "pwc": (
        'configs/pwcnet/pwcnet_ft_4x1_300k_sintel_final_384x768.py', 
        'checkpoints/pwcnet_ft_4x1_300k_sintel_final_384x768.pth'
    ),
    "flownetc": (
        'configs/flownet/flownetc_8x1_sfine_sintel_384x448.py',
        'checkpoints/flownetc_8x1_sfine_sintel_384x448.pth'
    ),
    "raft": (
        "configs/raft/raft_8x2_100k_mixed_368x768.py",
        "checkpoints/raft_8x2_100k_mixed_368x768.pth"
    )
}