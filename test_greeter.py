import unittest
from greeter import Greeter


class TestGreeter(unittest.TestCase):
    def test_greet(self):
        greeter = Greeter("Alice")
        assert greeter.greet() == "Hello, Alice!"

    def test_greet_empty_name(self):
        greeter = Greeter("")
        assert greeter.greet() == "Hello, !"

    def test_greet_none_name(self):
        greeter = Greeter(None)
        assert greeter.greet() == "Hello, None!"

if __name__ == "__main__":
    unittest.main()
