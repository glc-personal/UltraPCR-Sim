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

