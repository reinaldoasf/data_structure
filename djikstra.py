processed = []
def find_lower_cost_node(costs):
    lower_cost = float("inf")
    lower_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lower_cost and node not in processed:
            lower_cost_node = node
            lower_cost = cost
    return lower_cost_node
def create_grafo():
    grafo = {}
    grafo['inicio'] = {}
    grafo['a'] = {}
    grafo['b'] = {}
    grafo['c'] = {}
    grafo['d'] = {}
    grafo['fim'] = {}
    grafo['inicio']['a'] = 5
    grafo['inicio']['b'] = 2
    grafo['a']['c'] = 4
    grafo['a']['d'] = 2
    grafo['b']['a'] = 8
    grafo['b']['d'] = 7
    grafo['c']['d'] = 5
    grafo['c']['fim'] = 3
    grafo['d']['fim'] = 1
    return grafo
def print_path(pais):
    node = pais['fim']
    path = "fim <- " + node
    while node != 'inicio':
        node = pais[node]
        path+=" <- "+node
    print(path)

if __name__ == '__main__':
    grafo = create_grafo()
    infinito = float('inf')
    node = find_lower_cost_node(grafo['inicio'])
    pais = dict()
    pais['a'] = 'inicio'
    pais['b'] = 'inicio'
    pais['c'] = None
    pais['d'] = None
    pais['fim'] = None
    custos = dict()
    custos['a'] = grafo['inicio']['a']
    custos['b'] = grafo['inicio']['b']
    custos['c'] = float('inf')
    custos['d'] = float('inf')
    custos['fim'] = float('inf')

    while node is not None:
        custo = custos[node]
        vizinhos = grafo[node]
        for vizinho in vizinhos.keys():
            novo_custo = custo + vizinhos[vizinho]
            if custos[vizinho] > novo_custo:
                custos[vizinho] = novo_custo
                pais[vizinho] = node
        processed.append(node)
        node = find_lower_cost_node(custos)

    print(custos)
    print_path((pais))