values = []
def setup():
    size(800, 500)
    for i in range(0, width):
        values.append(random(height))
    # values.sort()
    for j in range(0, len(values)):
        for k in range(0, len(values)-i-1):
            a = values[k]
            b = values[k+1]
            if a > b:
                swap(values, j, j+1)
def draw():
    background(0)
    for I in range(len(values)):
        stroke(255)
        line(I, height, I, height - values[I])
def swap(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp
