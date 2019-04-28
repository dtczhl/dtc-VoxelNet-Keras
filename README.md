

6-core i9 @ 2.90GHz   
GeForce GTX 1070 (8GB)

Dp, Hp, Wp, T


###  Chrono Time

| H | W | Time seconds (CPU) | Time seconds (GPU) |
| --- | --- | --- | --- |
| 23 | 23 | 0.31 | 0.75 |
| 31 | 31 | 0.47 | 0.77 |
| 40 | 40 | 0.64 | 0.80 |
| 55 | 55 | 1.04 | 0.87 |
| 71 | 71 | 1.65 | 1.00 |
| 95 | 95 | 2.89 | 1.20 |
| 127 | 127 | 5.30 | 1.64 |
| 175| 175 | Crash | Crash |

### CPU Time

| H | W | Time seconds (CPU) | Time seconds (GPU) |
| --- | --- | --- | --- |
| 23 | 23 | 1.74 | 0.74 |
| 31 | 31 | 3.06 | 0.77 |
| 40 | 40 | 4.99 | 0.81 |
| 55 | 55 | 9.29 | 0.87 |
| 71 | 71 | 15.69 | 1.02 |
| 95 | 95 | 28.39 | 1.23 |
| 127 | 127 | 53.06 | 1.66 |
| 175| 175 | Crash | Crash |

---

# VoxelNet-Keras
VoxelNet implementation in Keras

*NOTE*: This is still a work in progress. The full training pipeline is not yet done, but the model is practically fully implemented (see `model.png`) aside from some missing activations near the top Conv2D/Conv2DTranspose layers. Also, the sampling and grouping can be done as a preprocessing step outside the network, hence the difference in input shape vs what was described in the paper.
