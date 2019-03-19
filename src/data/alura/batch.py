from alura.transcriptor import *
from os import listdir
from os.path import isfile, join
import logging

def batch_single(filename):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data: {}'.format(filename))
    t = Transcriptor(filename, basefolder="")
    t.video_to_audio()
    t.upload_audio()
    result = t.transcribe()
    result.save_json()
    response.save_markdown()

def batch_all(folder):
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    mp4s = [f for f in onlyfiles if f.endswith('.mp4')]
    print(mp4s)
    for mp4 in mp4s[:1]:
        batch_single(mp4[:-4])
