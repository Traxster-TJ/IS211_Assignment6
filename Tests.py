def test_celsius_conversions():
    assert convertCelsiusToKelvin(0) == 273.15
    assert convertCelsiusToKelvin(100) == 373.15
    assert convertCelsiusToFahrenheit(0) == 32.0
    assert convertCelsiusToFahrenheit(100) == 212.0
