import numpy as np

from UPS.Core.spartition import SPartition

def test_spartition_creation():
	'''
	'''
	position = np.array([1.0, 2.0, 3.0])
	radius = 1.5
	status = 'positive'
	sphericity_deviation = 0.1

	spartition = SPartition(position, radius, status, sphericity_deviation)

	assert np.array_equal(spartition.position, position)
	assert spartition.radius == radius
	assert spartition.status == status
	assert spartition.sphericity_deviation == sphericity_deviation
