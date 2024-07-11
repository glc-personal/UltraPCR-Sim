import numpy as np
from typing import Dict, Set

from UPS.Core.spartition import SPartition

class SBoxWell:
	'''
	SBoxWell is the simulation well in the shape of a box which
	contains a collection of SPartitions.
	'''
	def __init__(self, width: float, height: float, depth: float):
		self.width = width
		self.height = height
		self.depth = depth
		self.partitions: Dict[int, SPartition] = {}
		self.available_ids: Set[int] = set()
		self.next_id = 0

	def add_partition(self, partition: SPartition) -> int:
		'''
		Add a partition to the well with the id set automatically
		which is returned as output.
		'''
		# Check if there are any available ids (will be if a partition had been removed)
		if self.available_ids:
			partition_id = min(self.available_ids)
			self.available_ids.remove(partition_id)
		else:
			partition_id = self.next_id
			self.next_id += 1
		# Add the partition to the well
		self.partitions[partition_id] = partition
		return partition_id		

	def remove_partition(self, partition_id: int) -> SPartition:
		'''
		Remove a partition by it's id returning the partition.
		'''
		if partition_id not in self.partitions:
			raise ValueError(f"Partition (ID = {partition_id}) does not exist!")
		# Store the partition locally before it is deleted
		sp = self.partitions[partition_id]
		# Delete the partition
		del self.partitions[partition_id]
		# Add the id for this partition to the set of available ids that can be used
		self.available_ids.add(partition_id)
		# Return the deleted partition
		return sp
		
	def get_partition(self, partition_id: int) -> SPartition:
		'''
		Get a partition by it's id returning the partition.
		'''
		if partition_id not in self.partitions:
			raise ValueError(f"Partition (ID = {partition_id}) does not exist!")
		return self.partitions[partition_id]

	def count(self) -> int:
		'''
		Get the number of partitions currently in the well.
		'''
		return len(self.partitions)
