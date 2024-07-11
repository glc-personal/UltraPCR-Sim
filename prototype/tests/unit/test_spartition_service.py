# tests/unit/test_spartition_service.py

import numpy as np

from UPS.ApplicationServices.spartition_service import SPartitionService
from UPS.Core.spartition import SPartition

def test_equality():
	'''
	'''
	sp = SPartition([0.1, 0.31, 4.1], 38.5, 1, 0.1)
	expected = SPartition([0.1, 0.31, 4.1], 38.5, 1, 0.1)
	unexpected = SPartition([0,0,0], 1, 0, 1)
	assert sp == expected
	assert sp != unexpected

def test_generate_random_spartition():
	'''
	'''
	# Set the possible bounds for all parameters
	pbounds = (-10, 10)
	rbounds = (38, 42)
	sbounds = (0, 1)
	dbounds = (0.1, 1)
	sp = SPartitionService.generate_random_spartition(pbounds, pbounds, pbounds,
		rbounds, sbounds, dbounds)
	assert len(sp.position) == 3
	assert pbounds[0] <= sp.position[0] <= pbounds[1]
	assert pbounds[0] <= sp.position[1] <= pbounds[1]
	assert pbounds[0] <= sp.position[2] <= pbounds[1]
	assert rbounds[0] <= sp.radius <= rbounds[1]
	assert sbounds[0] <= sp.status <= sbounds[1]
	assert dbounds[0] <= sp.sphericity_deviation < dbounds[1]
