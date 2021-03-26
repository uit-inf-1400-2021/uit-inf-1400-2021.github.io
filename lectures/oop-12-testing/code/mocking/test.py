import unittest
import unittest.mock as m
import src

# Child class of TestCase - enables automatic test discovery
class TestOuter(unittest.TestCase):
    # Simple test of the OuterClass initialization
    def test_name(self):
        o = src.OuterClass()
        self.assertEqual(o.name, "Testing")

    # Test where we mock the InnerClass
    @m.patch("src.InnerClass")
    def test_mock(self, inner):
        # Get the instance for modifying the mock methods
        instance = inner.return_value
        # Ensure the return value is "Mocked" for the get_name method
        instance.get_name.return_value = "Mocked"

        # Initialization of OuterClass
        o = src.OuterClass()
        # The name has changed
        self.assertEqual(o.name, "Mocked")
        # get_name was called exactly once on the mocked object
        instance.get_name.assert_called_once()

if __name__ == "__main__":
    unittest.main()
