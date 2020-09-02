import os
import sys
import math


# Add Circle class implementation below
class Circle:
    count = 0
    c_radius = 0

    def __init__(self, c_radius):
        self.c_radius = c_radius

    def area(self, *circles):
        # area of circle
        rad_list = list()
        for circle in circles:
            Circle.count += 1
            rad_list.append(3.14 * math.sqrt(circle.c_radius))
        return rad_list


circle1 = Circle(2)
circle2 = Circle(4)
circle3 =  Circle(6)
print(circle1.area(circle1,circle2,circle3))
print(Circle.count)
with open(os.environ['OUTPUT_PATH'], 'w') as fout:
    fout.write("{}\n{}".format(str(circleArea.area(1, 2, 3), Circle.count)))

#
# if __name__ == "__main__":
#     with open(os.environ['OUTPUT_PATH'], 'w') as fout:
#         res_lst = list()
#         lst = list(map(lambda x: float(x.strip()), input().split(',')))
#         for radius in lst:
#             res_lst.append(Circle(radius).area())
#         fout.write("{}\n{}".format(str(res_lst), str(Circle.no_of_circles)))