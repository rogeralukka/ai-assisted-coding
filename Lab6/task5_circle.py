import math
from typing import Union


class Circle:
    """Represents a geometric circle defined by its radius."""

    def __init__(self, radius: Union[int, float]):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be an integer or float.")
        if radius <= 0:
            raise ValueError("Radius must be a positive number greater than zero.")

        self.radius = float(radius)

    def area(self) -> float:
        """Calculates the area: Area = π * r^2."""
        return math.pi * (self.radius ** 2)

    def circumference(self) -> float:
        """Calculates the circumference: C = 2 * π * r."""
        return 2 * math.pi * self.radius

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"


if __name__ == "__main__":
    test_radii = [1.0, 5.0, 7.5]

    print(f"{'Radius':>8} | {'Circumference':>15} | {'Area':>15}")
    print("-" * 44)

    for r in test_radii:
        c = Circle(r)
        print(f"{c.radius:8.2f} | {c.circumference():15.4f} | {c.area():15.4f}")
