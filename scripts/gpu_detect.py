try:
    import torch
    print(f'Torch CUDA: {torch.cuda.is_available()}')
except ModuleNotFoundError as e:
    print('Torch not present in enviroment')

try:
    from tensorflow.python.client import device_lib
    print(f'Tensorflow sees: {[x.physical_device_desc or x.name for x in device_lib.list_local_devices()]}')
except ModuleNotFoundError as e:
    print('Tensorflow not present in enviroment')

try:
    import jax
    print(f'Jax: {jax.devices()}')
except ModuleNotFoundError as e:
    print('Jax not present in enviroment')


