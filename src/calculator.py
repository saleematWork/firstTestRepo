class Calculator:
    """A simple calculator class for demonstration"""

    def add(self, a, b):
        """Add two numbers"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        return a + b

    def subtract(self, a, b):
        """Subtract b from a"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        return a * b

    def divide(self, a, b):
        """Divide a by b"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def power(self, base, exponent):
        """Calculate base raised to exponent"""
        if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
            raise ValueError("Both arguments must be numbers")
        return base ** exponent