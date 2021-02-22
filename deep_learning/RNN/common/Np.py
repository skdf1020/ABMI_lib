from common.Config import GPU


if GPU:
    import cupy as np
    import cupyx.scatter_add as add_at
    np.cuda.set_allocator(np.cuda.MemoryPool().malloc)
#    np.add.at = cupyx.scatter_add
    add_at = add_at

    print('\033[92m' + '-' * 60 + '\033[0m')
    print(' ' * 23 + '\033[92mGPU Mode (cupy)\033[0m')
    print('\033[92m' + '-' * 60 + '\033[0m\n')
else:
    import numpy as np