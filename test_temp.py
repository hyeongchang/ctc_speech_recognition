import os
import librosa
import numpy as np


a, _ = librosa.load("wav48/p225/p225_001.wav", sr=8000)
print(a[:, np.newaxis])
# hyeongchang : commit_2