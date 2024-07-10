# tests/unit/test_spartition_service.py

import numpy as np

from UPS.ApplicationServices.spartition_service import SPartitionService
from UPS.Core.spartition import SPartition

def test_generate_random_position():
	'''
	'''
	bounds = (-10, 10)
	position = SPartitionService.generate_random_position(bounds, bounds, bounds)

	assert len(position) == 3
	assert bounds[0] <= position[0] <= bounds[1]
	assert bounds[0] <= position[1] <= bounds[1]
	assert bounds[0] <= position[2] <= bounds[1]
