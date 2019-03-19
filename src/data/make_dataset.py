# -*- coding: utf-8 -*-
import click
import logging
import os
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from alura.batch import *

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    credential_path = "data/keys/gcloud-key.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

    batch_all('data/raw')
