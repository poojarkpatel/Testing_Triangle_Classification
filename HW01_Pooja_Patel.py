"""
HW01
Triangle classification
"""
import math

class Triangle:
    """
     The class takes length of three sides of triangle and return the
     type of triangle.
    """

    def __init__(self, side1, side2, side3) -> None:
        """
        init function of class
        """
        self.side1 = float(side1)
        self.side2 = float(side2)
        self.side3 = float(side3)

    def classify_triangle(self) -> str:
        if self.side1 + self.side2 < self.side3 or self.side3 + self.side1 < self.side2 or self.side3 + self.side2 < self.side1:
            raise ValueError
        else:
            if self.side1 != self.side2 and self.side2 != self.side3 and self.side3 != self.side1:
                if round((self.side1 ** 2), 2) + round((self.side2 ** 2), 2) == math.ceil((self.side3 ** 2)):
                    return "Right and Scalene Triangle"
                else:
                    return "Scalene Triangle"
            elif self.side1 == self.side2 == self.side3:
                return "Equilateral Triangle"

            elif self.side1 == self.side2 or self.side2 == self.side3 or self.side3 == self.side1:
                if (round((self.side1 ** 2), 2) + round(self.side2 ** 2, 2)) == math.ceil((self.side3 ** 2)):
                    return "Right and Isosceles Triangle"
                else:
                    return "Isosceles Triangle"

    def __str__(self):
        return f"{self.side1}, {self.side2}, {self.side3}"

if __name__ == '__main__':
    side_1 = input("Enter first side of triangle: ")
    side_2 = input("Enter second side of triangle: ")
    side_3 = input("Enter third side of triangle: ")
    triangle: Triangle = Triangle(side_1, side_2, side_3)
