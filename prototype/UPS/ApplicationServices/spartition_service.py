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
	def generate_random_spartition(xbounds: Tuple[float, float],
		ybounds: Tuple[float, float], zbounds: Tuple[float, float],
		rbounds: Tuple[float, float], sbounds: Tuple[int, int],
		dbounds: Tuple[float, float]) -> SPartition:
		'''
		Generate a random SPartition
		'''
		# Generate random parameters based on the provided bounds
		position = np.array([random.uniform(xbounds[0], xbounds[1]),
				random.uniform(ybounds[0], ybounds[1]),
				random.uniform(zbounds[0], zbounds[1])])
		radius = random.uniform(rbounds[0], rbounds[1])
		status = random.randint(sbounds[0], sbounds[1])
		sphericity_deviation = random.uniform(dbounds[0], dbounds[1])

		# Initialize the SPartition instance and return it
		sp = SPartition(position, radius, status, sphericity_deviation)
		return sp
