from ipykernel.kernelapp import IPKernelApp
from . import EchoK

IPKernelApp.launch_instance(kernel_class=EchoK)
