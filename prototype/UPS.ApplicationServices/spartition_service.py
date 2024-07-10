# UPS.ApplicationServices/spartition_service.py

import numpy as np
import random
from typing import List, Tuple

from UPC.Core.spartition import SPartition

class SPartitionService:
	'''
	SPartitionService for handling SPartitions.
	'''
	@staticmethod
	def generate_random_position(bounds: Tuple[float, float]) -> np.ndarray:
		'''
		'''
		return np.array([random.uniform(bounds[0], bounds[1]),
				random.uniform(bounds[0], bounds[1]),
				random.uniform(bounds[0], bounds[1])])
