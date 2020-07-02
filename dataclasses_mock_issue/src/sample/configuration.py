import dataclasses
import sample.resource
from typing import NamedTuple


@dataclasses.dataclass()
class ResourceClsKwargs():
    person: sample.resource.Person

    def asdict(self):
    	output = dict()
    	for field in dataclasses.fields(self):
    		output[field.name] = getattr(self, field.name)
    	return output

# class ResourceClsKwargs(NamedTuple):
# 	person: sample.resource.Person