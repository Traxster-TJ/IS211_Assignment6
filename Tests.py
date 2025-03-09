import unittest
from conversions import (
    convertCelsiusToKelvin, convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius, convertFahrenheitToKelvin,
    convertKelvinToCelsius, convertKelvinToFahrenheit
)


class TestCelsiusConversions(unittest.TestCase):
    def test_celsius_to_kelvin(self):
        # Test cases for Celsius to Kelvin conversion
        test_cases = [
            (0.0, 273.15), #water freezes
            (100.0, 373.15), #Water boils
            (-273.15, 0.0),
            (300.0, 573.15),# part 1 example
            (37.0, 310.15) # Avg body temperature
        ]

        for celsius, expected_kelvin in test_cases:
            print(f"Testing: {celsius}°C should convert to {expected_kelvin}K")
            result = convertCelsiusToKelvin(celsius)
            self.assertAlmostEqual(result, expected_kelvin, places=2)

    def test_celsius_to_fahrenheit(self):
        # Testing for Celsius to Fahrenheit
        test_cases = [
            (0.0, 32.0),  # Water freezes
            (100.0, 212.0),  # water boils
            (-40.0, -40.0),
            (300.0, 572.0),  #part 1 example
            (37.0, 98.6)  # avg Body temperature
        ]

        for celsius, expected_fahrenheit in test_cases:
            print(f"Testing: {celsius}°C should convert to {expected_fahrenheit}°F")
            result = convertCelsiusToFahrenheit(celsius)
            self.assertAlmostEqual(result, expected_fahrenheit, places=2)


class TestFahrenheitConversions(unittest.TestCase):
    def test_fahrenheit_to_celsius(self):
        # Testing for Fahrenheit to Celsius
        test_cases = [
            (32.0, 0.0),
            (212.0, 100.0),
            (-40.0, -40.0),
            (98.6, 37.0),
            (572.0, 300.0)
        ]

        for fahrenheit, expected_celsius in test_cases:
            print(f"Testing: {fahrenheit}°F should convert to {expected_celsius}°C")
            result = convertFahrenheitToCelsius(fahrenheit)
            self.assertAlmostEqual(result, expected_celsius, places=2)

    def test_fahrenheit_to_kelvin(self):
        # Testing for Fahrenheit to Kelvin
        test_cases = [
            (32.0, 273.15),
            (212.0, 373.15),
            (98.6, 310.15),
            (572.0, 573.15),
            (0.0, 255.37)
        ]

        for fahrenheit, expected_kelvin in test_cases:
            print(f"Testing: {fahrenheit}°F should convert to {expected_kelvin}K")
            result = convertFahrenheitToKelvin(fahrenheit)
            self.assertAlmostEqual(result, expected_kelvin, places=2)


class TestKelvinConversions(unittest.TestCase):
    def test_kelvin_to_celsius(self):
        # Testing for Kelvin to Celsius
        test_cases = [
            (273.15, 0.0),
            (373.15, 100.0),
            (0.0, -273.15),
            (310.15, 37.0),
            (573.15, 300.0)
        ]

        for kelvin, expected_celsius in test_cases:
            print(f"Testing: {kelvin}K should convert to {expected_celsius}°C")
            result = convertKelvinToCelsius(kelvin)
            self.assertAlmostEqual(result, expected_celsius, places=2)

    def test_kelvin_to_fahrenheit(self):
        # Testing for Kelvin to Fahrenheit
        test_cases = [
            (273.15, 32.0),
            (373.15, 212.0),
            (0.0, -459.67),
            (310.15, 98.6),
            (573.15, 572.0)
        ]

        for kelvin, expected_fahrenheit in test_cases:
            print(f"Testing: {kelvin}K should convert to {expected_fahrenheit}°F")
            result = convertKelvinToFahrenheit(kelvin)
            self.assertAlmostEqual(result, expected_fahrenheit, places=2)


if __name__ == '__main__':
    unittest.main()
