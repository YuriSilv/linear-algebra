from typing import TypeVar, List
import math

vector = List[float]

def vec_sum(x:vector, y:vector) -> vector:
    if(len(x) == len(y)):
        return [v1+v2 for v1,v2 in zip(x,y)]
    else:
        print('tamanhos dos vetores inválidos')
        return None

def vec_scale(x:vector, scale:float) -> vector:
    return [value*scale for value in x]

def vec_norm(x: vector) -> float:
    return math.sqrt(sum([value**2 for value in x]))

def vec_unit(x: vector) -> vector:
    return vec_scale(x, (1/vec_norm(x)))

def ang_vec2(ang:float, mag:float) -> vector:
    x = round(math.cos(ang)*mag, 3)
    y = round(math.sin(ang)*mag, 3)
    return [x,y]

def linear_combination(v:List[vector], c:list) -> vector:
    n_vecs = [vec_scale(vetor,c_value) for vetor, c_value in zip(v,c)]
    result = [0]*len(v[0])
    for v in n_vecs:
        result = vec_sum(result, v)

    return result

def dot_vec(x:vector, y:vector) -> float:
    return [x[1]*x[3] - x[2]*y[1], x[2]*y[0] - x[0]*y[2], x[0]*y[1] - x[1]*y[0]]

v1 = [1,2,3]
v2 = [1,1,1]

print(linear_combination([[1,2],[0,3]], [2,-2/3]))