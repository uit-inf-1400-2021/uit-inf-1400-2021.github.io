class InnerClass:
    def __init__(self):
        self.name = "Testing"

    def get_name(self):
        return self.name

class OuterClass:
    def __init__(self):
        self.inner = InnerClass()
        self.name = self.inner.get_name()
