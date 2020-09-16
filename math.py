def get_stat(container):
    """Runs Some Stuff"""
    stat = []
    points = []
    def mul(x, y):
        return x*y
    def add(x, y):
        return x+y
    def sub(x,y):
        return x-y
    def div(x, y):
        return x/y
    equation = lambda x, y: mul(5, x) + mul(4, y)

    for coord in container:
        print(f"f{coord} is Equal to")
        ans = equation(coord[0], coord[1])
        print(ans)
        stat.append(ans)
        points.append(coord)
        print()

    print(f"The Largest Number is {max(stat)} belonging to {points[stat.index(max(stat))]}")
    print(f"The Smallest Number is {min(stat)} belonging to {points[stat.index(min(stat))]}")

point_set = [
    (-6, 6),
    (-6, 3),
    (-3, 0),
    (1, 0),
    (2, 1),
    (2, 4),
]
get_stat(point_set)