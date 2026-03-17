class Distance:

    CONVERSION = {
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value, unit):
        if unit not in self.CONVERSION:
            raise ValueError(f"Неизвестная единица измерения: {unit}")
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):
        return self.value * self.CONVERSION[self.unit]

    @staticmethod
    def from_meters(meters, unit):
        return Distance(meters / Distance.CONVERSION[unit], unit)

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented

        total_meters = self.to_meters() + other.to_meters()

        # возвращаем результат в единицах первого операнда
        return Distance.from_meters(total_meters, self.unit)


d1 = Distance(10, "m")
d2 = Distance(2, "km")
d3 = Distance(50, "cm")

print(d1)
print(d2)
print(d3)

result1 = d1 + d2
print(result1)

result2 = d2 + d1
print(result2)

result3 = d1 + d3
print(result3)