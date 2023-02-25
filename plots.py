import matplotlib.pyplot as plt
import vectors

def plot2d_sum_graph(x: vectors.vector, y: vectors.vector):
    vec_sum = vectors.vec_sum(x, y)
    plt.plot([0, x[0]], [0, x[1]], color='red')
    plt.plot([x[0], y[0]+x[0]], [x[1], y[1]+x[1]], color='blue')
    plt.plot([0, vec_sum[0]], [0, vec_sum[1]], '--')
    plt.savefig('sum_graph.png')