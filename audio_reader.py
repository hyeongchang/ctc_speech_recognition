import os
import sys
from Exceptions import PathNotFind, FileNotFind

from glob import glob
from random import shuffle
from time import time

import numpy as np

import dill
import librosa

def read_audio_from(path, sample_rate):
    # hyeongchang : n-dim vector(n,)를 (n, 1) 행렬로 reshape 해야하는 이유 알 수 있도록...
    audio, _ = librosa.load(path, sr=sample_rate)
    return audio[:, np.newaxis]

class Audio_reader(object):
    def __init__(self,
                 audio_dir,
                 sample_rate,
                 cache_dir = None):
        # read audio file list
        if not os.path.exists(audio_dir):
            raise PathNotFind("Invalid audio_dir path")
        else:
            FilePathList = sorted(glob(os.path.join(audio_dir, "**/*.wav"), recursive=True))
            FilePathList = [path.replace('\\', '/') for path in FilePathList]
            assert len(FilePathList) != 0

            AudioList = [read_audio_from(path=path, sample_rate=sample_rate) for path in FilePathList]
            # hyeongchang : commit_2


_ = Audio_reader(audio_dir="wav48", sample_rate=8000)

