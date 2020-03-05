import os
from multiprocessing import Pool

processes = ('sound.py', 'video.py')


def run_process(process):
    os.system('python {}'.format(process))


pool = Pool(processes=2)
pool.map(run_process, processes)