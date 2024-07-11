from UPS.ApplicationServices.spartition_service import SPartitionService
import random

pbounds = (-10, 10)
rbounds = (38, 42)
sbounds = (0, 1)
dbounds = (0.1, 1)
random.seed(10)
sp = SPartitionService.generate_random_spartition(pbounds, pbounds, pbounds,
	rbounds, sbounds, dbounds)

print(sp.position)
print(sp.radius)
print(sp.status)
print(sp.sphericity_deviation)
