def calculate_area(dimension_1, dimension_2, shape=0):
    if shape == "triangle":
        area = 1 / 2 * (dimension_1 * dimension_2)
        print("Area of triangle is: ", area)
    elif shape == "rectangle":
        area = dimension_1 * dimension_2
        print("Area of rectangle is: ", area)
    else:
        print("***Error: Input shape is neither triangle or rectangle.")
        area = None
    return area


print(calculate_area(10, 5, "rectangle"))