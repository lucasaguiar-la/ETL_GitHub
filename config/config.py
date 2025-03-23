import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FILTER_KEY = 'Python'
LOG_DIR_PATH = os.path.join(BASE_DIR, 'logs')
DATA_DIR_PATH = os.path.join(BASE_DIR, 'data', 'raw')
LOADER_OUTPUT_PATH = os.path.join(BASE_DIR, 'data', 'final')