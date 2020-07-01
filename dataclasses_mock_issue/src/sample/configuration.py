import dataclasses
import sample.resource


@dataclasses.dataclass
class ResourceClsKwargs:
    person: sample.resource.Person
