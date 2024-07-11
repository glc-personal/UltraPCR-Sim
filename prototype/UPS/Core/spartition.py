# UPS.Core/spartition.py
import numpy as np

class SPartition:
	'''
	SPartition Class for a simulated Partition. 
	'''
	def __init__(self, 
		position: np.ndarray, radius: float, status: str, sphericity_deviation: float):
		self.position = position
		self.radius = radius
		self.status = status
		self.sphericity_deviation = sphericity_deviation

	def __eq__(self, other):
		if not isinstance(other, SPartition):
			return False
		return (
			np.array_equal(self.position, other.position) and
			self.radius == other.radius and
			self.status == other.status and
			self.sphericity_deviation == other.sphericity_deviation
		)
