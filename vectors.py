from typing import TypeVar, List

vector = List[float]

def vec_sum(x:vector, y:vector) -> vector:
    if(len(x) == len(y)):
        return [v1+v2 for v1,v2 in zip(x,y)]
    else:
        print('tamanhos dos vetores inválidos')
        return None

def vec_scale(x:vector, scale:float) -> vector:
    return [value*scale for value in x]

v1 = [1,2,3]
v2 = [1,1,1]

print(vec_sum(v1,vec_scale(v2,-1)))