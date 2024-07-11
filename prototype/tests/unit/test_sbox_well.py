from UPS.Core.sbox_well import SBoxWell
from UPS.Core.spartition import SPartition

def test_sbox_well():
	'''
	'''
	sp1 = SPartition([0,0,0], 0.1, 0, 1)
	sp2 = SPartition([0,0,0], 0.2, 0, 1)
	sp3 = SPartition([0,0,0], 0.3, 0, 1)
	well = SBoxWell(10, 10, 10)
	well.add_partition(sp1)
	well.add_partition(sp2)
	well.add_partition(sp3)
	assert well.count() == 3
	sp2_removed = well.remove_partition(1)
	assert well.count() == 2
	assert sp2 == sp2_removed
