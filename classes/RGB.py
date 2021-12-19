from abc import ABC, abstractmethod


class ComputerColor(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __mul__(self, other) -> "ComputerColor":
        pass

    @abstractmethod
    def __rmul__(self, other) -> "ComputerColor":
        pass


class RGBColor(ComputerColor):
    END = "\033[0"
    START = "\033[1;38;2"
    MOD = "m"

    def __init__(self, red: int, green: int, blue: int):
        self.red = max(min(red, 255), 0)
        self.green = max(min(green, 255), 0)
        self.blue = max(min(blue, 255), 0)

    def __str__(self):
        return f"{self.START};{self.red};{self.green};{self.blue}{self.MOD}●{self.END}{self.MOD}"

    __repr__ = __str__

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (
                self.blue == other.blue and
                self.green == other.green and
                self.red == other.red
        )

    def __add__(self, other):
        if not isinstance(other, RGBColor):
            raise ValueError(f"Сложение цвета с {type(other)} недопустимо")
        return RGBColor(
            self.red + other.red,
            self.green + other.green,
            self.blue + other.blue,
        )

    def __hash__(self):
        return hash((self.red, self.green, self.blue))

    @staticmethod
    def _contrast(c, level):
        if c < 0 or c > 1:
            raise ValueError("Число вне отрезка [0, 1]")
        cl = -256 * (1 - c)
        F = (259 * (cl + 255)) / (255 * (259 - cl))
        return int(F * (level - 128) + 128)

    def __mul__(self, c):
        return RGBColor(
            self._contrast(c, self.red),
            self._contrast(c, self.green),
            self._contrast(c, self.blue),
        )

    __rmul__ = __mul__


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]
    for row in a_matrix:
        print("".join(str(ptr) for ptr in row))


if __name__ == "__main__":
    red = RGBColor(0, 255, 25)
    print_a(red * 0.88)






