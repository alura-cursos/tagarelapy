from alura.transcriptor import *
from os import listdir
from os.path import isfile, join
import logging

def batch_single_upload(filename):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('raw data: {}'.format(filename))
    t = Transcriptor(filename, basefolder="")
    t.video_to_audio()
    t.upload_audio()

def batch_multiple_translate(filename):
    logger = logging.getLogger(__name__)
    output = "data/processed/{}.md".format(filename)
    if os.path.isfile(output):
        logger.info("Skipping {}".format(output))
        return
    logger.info('parallel: {}'.format(filename))
    t = Transcriptor(filename, basefolder="")
    result = t.transcribe()
    result.save_json()
    result.save_markdown()

def parallel_process(array, function, n_jobs=16, use_kwargs=False, front_num=3):
    from tqdm import tqdm
    from concurrent.futures import ProcessPoolExecutor, as_completed
    """
        A parallel version of the map function with a progress bar. 

        Args:
            array (array-like): An array to iterate over.
            function (function): A python function to apply to the elements of array
            n_jobs (int, default=16): The number of cores to use
            use_kwargs (boolean, default=False): Whether to consider the elements of array as dictionaries of 
                keyword arguments to function 
            front_num (int, default=3): The number of iterations to run serially before kicking off the parallel job. 
                Useful for catching bugs
        Returns:
            [function(array[0]), function(array[1]), ...]
    """
    from tqdm import tqdm
    from concurrent.futures import ProcessPoolExecutor, as_completed
    #We run the first few iterations serially to catch bugs
    if front_num > 0:
        front = [function(**a) if use_kwargs else function(a) for a in array[:front_num]]
    #If we set n_jobs to 1, just run a list comprehension. This is useful for benchmarking and debugging.
    if n_jobs==1:
        return front + [function(**a) if use_kwargs else function(a) for a in tqdm(array[front_num:])]
    #Assemble the workers
    with ProcessPoolExecutor(max_workers=n_jobs) as pool:
        #Pass the elements of array into function
        if use_kwargs:
            futures = [pool.submit(function, **a) for a in array[front_num:]]
        else:
            futures = [pool.submit(function, a) for a in array[front_num:]]
        kwargs = {
            'total': len(futures),
            'unit': 'it',
            'unit_scale': True,
            'leave': True
        }
        #Print out the progress as tasks complete
        for f in tqdm(as_completed(futures), **kwargs):
            pass
    out = []
    #Get the results from the futures. 
    for i, future in tqdm(enumerate(futures)):
        try:
            out.append(future.result())
        except Exception as e:
            out.append(e)
    return front + out

def batch_all(folder):
    logger = logging.getLogger(__name__)
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    mp4s = [f[:-4] for f in onlyfiles if f.endswith('.mp4')]
    logger.info("Running for {} files".format(len(mp4s)))

    # for mp4 in mp4s:
    #     batch_single_upload(mp4)

    parallel_process(mp4s, batch_multiple_translate, n_jobs=4)
