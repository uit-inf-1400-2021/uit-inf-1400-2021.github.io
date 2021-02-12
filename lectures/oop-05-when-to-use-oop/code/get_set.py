class Color:
    def __init__(self, color, name):
        self.color = color
        self._name = name

    def _set_name(self, name):
        if type(name) == str:
            self._name = name
        else:
            print("Bad type!")

    def _get_name(self):
        return self._name

    name = property(_get_name, _set_name)


print(__name__)

if __name__ == "__main__":
    c = Color((255,0,0), "Red")
    c.name = "Really Red"
    c.name = None
    print(c.name)
