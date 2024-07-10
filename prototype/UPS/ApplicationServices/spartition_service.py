# UPS.ApplicationServices/spartition_service.py

import numpy as np
import random
from typing import List, Tuple

from UPS.Core.spartition import SPartition

class SPartitionService:
	'''
	SPartitionService for handling SPartitions.
	'''
	@staticmethod
	def generate_random_position(xbounds: Tuple[float, float],
		ybounds: Tuple[float, float], zbounds: Tuple[float, float]) -> np.ndarray:
		'''
		'''
		return np.array([random.uniform(xbounds[0], xbounds[1]),
				random.uniform(ybounds[0], ybounds[1]),
				random.uniform(zbounds[0], zbounds[1])])
