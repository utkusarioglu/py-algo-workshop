from math import pi, ceil


class Dunder:
    x: int = 1
    y: int = 2

    def __str__(self) -> str:
        """Dunder for converting to string

        @dev
        #1 This line is whatever.
        """
        return f"x: {self.x}, y: {self.y}"  # 1

    def __int__(self) -> int:
        return self.x + self.y

    def __getitem__(self, key: str) -> str:
        return f"You have asked for {key}"

    def __delitem__(self, key: str) -> None:
        print(f"You want to delete {key}")

    def __len__(self) -> int:
        return ceil(pi)

    def __contains__(self, key: str) -> bool:
        if key in ["x", "y"]:
            return True
        return False

    def __add__(self, other) -> tuple[int, int]:
        return (self.x + other.x, self.y + other.y)

    def __iadd__(self, scalar: int):
        self.x += scalar
        self.y += scalar
        return self

    def __call__(self):
        return f"Called {self}"

    def some_method(self):
        some_very_long_named_variable_that_is_long = 4
        some_other_very_long_named_variable_that_is_long = 4
        if (
            some_very_long_named_variable_that_is_long
            + some_very_long_named_variable_that_is_long
            == 8
        ):
            print("It's long")

    def some_other_method(self):
        """
        This one has docstring
        """
        if True:
            print("True")
