def chooseBestSum (maxSum, nTowns, ls):
    # Testa casos onde a soma é inviável
    if len(ls) <= nTowns:
        return None
    for x in ls:
        if x >= maxSum:
            return None
    # Cria um array com posições = quantidade de cidades contendo indexes para realizar os testes em ls        
    _index = []
    for x in range(nTowns):
        _index.append(x)
    # Armazena todas as combinações válidas em um array
    idealSum = 0

    cur = len(_index) - 1
    lim = len(ls) - 1
    chan = cur

    while True:
        sumTest = 0
        for x in _index:
            sumTest += ls[x]
        if sumTest == maxSum:   # Encerra a função caso haja uma soma perfeita
            return test
        if sumTest < maxSum and sumTest > idealSum:
            idealSum = sumTest
        
        # Manipulação das possibilidades
        lim = (len(ls) - 1) - (len(_index) - 1 - chan)
        if _index[chan] < lim:
            _index[chan] += 1
        else:
            if cur < chan:
                chan -= 1
                _index[chan] += 1
            elif cur > 0:
                cur -= 1
                chan = len(_index) - 1
                _index[cur] += 1
                for x in range(cur+1,len(_index)):
                    prev = x - 1
                    _index[x] = _index[prev] + 1 
            else:
                return idealSum

    

distances = [50,52,54,60,57,40]
print(chooseBestSum(200, 4, distances))