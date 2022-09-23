import os
from abc import ABC, abstractmethod
from typing import List

from threading import Thread, Lock, Semaphore

from transformers import AutoModelForPreTraining, AutoTokenizer

# TODO: implement text sim. module for filtering out frequently duplicated domains


class BaseSim(ABC):
    def __init__(self):
        pass
    
    
    @abstractmethod
    def calcualte_sim(self,):
        pass

class JaccardSim:
    pass


class MinHash:
    pass


class LSH:
    pass


class BertEmbeddingKMeans:
    pass