from classes import Type, SKOS, RDFS, EDM, OWL, Node, Relation

if __name__ == '__main__':
    # print(SKOS.Concept.value)
    # print(SKOS.Concept.name)

    node: Node = Node(Type.SKOS, SKOS.Concept, 'rémi bouvier')
    print(node.type)
    print(node.name)
    print(node.class_name)
