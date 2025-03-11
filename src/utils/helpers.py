from pathlib import Path

import logging
import os

def setup_logging(log_file=None, level=logging.INFO):
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    if log_file:
        log_dir = os.mpath.dirname(log_file)
        if log_dir:
            Path(log_dir).mkdir(parents=True, exist_ok=True)

        logging.basicConfig(
            level=level,
            format=log_format,
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
    else:
        logging.getLogger('matplotlib').setlevel(logging.WARNING)
        logging.getLogger('pandas').setLevel(logging.WARNING)

        logging.info('Sistema de logging configurado com sucesso.')
