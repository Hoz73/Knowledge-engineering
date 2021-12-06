from enum import Enum, unique


@unique
class Type(Enum):
    RDFS = 0
    RDF = 1
    OWL = 2
    FOAF = 3
    SKOS = 4
    DC = 5


##################################### knowledge engineering ####################################
@unique
class RDFS(Enum):
    subClassOf = 0
    range = 1
    domain = 2
    subPropertyOf = 3
    label = 4


@unique
class SKOS(Enum):
    # SKOS Properties
    member = 0
    collection = 1
    prefLabel = 2
    related = 3
    hiddenLabel = 4
    broader = 5
    narrower = 6
    definition = 7
    altLabel = 8
    scopeNot = 9

    # SKOS Classes
    Concept = 10


@unique
class EDM(Enum):
    # EDM Classes
    Agent = 0
    ProvidedCHO = 1

    # EDM Properties


@unique
class OWL(Enum):
    pass


########################################## semantic web #####################################
@unique
class RDF(Enum):
    type = 0
    Property = 1
    first = 2


@unique
class FOAF(Enum):
    pass


@unique
class DC(Enum):
    pass


#################################################################################################

class Relation:
    type = None
    class_name = None

    def __init__(self, type: Type, class_name):
        self.type = type
        self.class_name = class_name


class Node:
    type = None
    class_name = None
    name = None

    def __init__(self, type: Type, class_name, name):
        self.type = type
        self.class_name = class_name
        self.name = name


class Graph:
    Nodes = [Node]

    def __init__(self, Nodes: [Node]):
        self.Nodes = Nodes

# TODO how to create the relations between nodes and relationships ?