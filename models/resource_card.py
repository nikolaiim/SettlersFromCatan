import sys
sys.path.append("/Users/nikolai.molvik/Projects/Settlers/Settlers")


from dataclasses import dataclass
import models.resource_types

@dataclass
class Resource_card:
    resource_type:  models.resource_types.Resource_type

