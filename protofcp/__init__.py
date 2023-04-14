from .FCPSocket import *
from .consts import *
import warnings
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings(action = "ignore", category = CryptographyDeprecationWarning)

AUTHOR = "Andrea Vaccaro"