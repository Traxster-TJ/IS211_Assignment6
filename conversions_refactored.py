class ConversionNotPossible(Exception):
    """Exception raised when conversion between incompatible units is attempted."""
    pass


def convert(fromUnit, toUnit, value):
    """
    Convert a value from one unit to another.

    Args:
        fromUnit (str): The unit to convert from
        toUnit (str): The unit to convert to
        value (float): The value to convert

    Returns:
        float: The converted value

    Raises:
        ConversionNotPossible: If the conversion between the units is not possible
    """
    # Define unit types and their categories
    unit_categories = {
        'temperature': ['celsius', 'fahrenheit', 'kelvin'],
        'distance': ['miles', 'yards', 'meters']
    }

    # Create a flattened dictionary to look up a unit's category
    unit_to_category = {}
    for category, units in unit_categories.items():
        for unit in units:
            unit_to_category[unit] = category

    # Normalize inputs to lowercase
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()

    # Check if units exist in our supported units
    if fromUnit not in unit_to_category:
        raise ConversionNotPossible(f"Unknown unit: {fromUnit}")
    if toUnit not in unit_to_category:
        raise ConversionNotPossible(f"Unknown unit: {toUnit}")

    # Check if units are compatible (same category)
    if fromUnit == toUnit:
        return value

    from_category = unit_to_category[fromUnit]
    to_category = unit_to_category[toUnit]

    if from_category != to_category:
        raise ConversionNotPossible(f"Cannot convert from {fromUnit} to {toUnit} - incompatible unit types")

    # Handle temperature conversions
    if from_category == 'temperature':
        # Convert fromUnit to Celsius (as base unit)
        if fromUnit == 'fahrenheit':
            base_value = (value - 32) * 5 / 9
        elif fromUnit == 'kelvin':
            base_value = value - 273.15
        else:  # celsius
            base_value = value

        # Convert from Celsius to toUnit
        if toUnit == 'fahrenheit':
            return (base_value * 9 / 5) + 32
        elif toUnit == 'kelvin':
            return base_value + 273.15
        else:  # celsius
            return base_value

    # Handle distance conversions
    elif from_category == 'distance':
        # Convert fromUnit to Meters (as base unit)
        if fromUnit == 'miles':
            base_value = value * 1609.34  # 1 mile = 1609.34 meters
        elif fromUnit == 'yards':
            base_value = value * 0.9144  # 1 yard = 0.9144 meters
        else:  # meters
            base_value = value

        # Convert from Meters to toUnit
        if toUnit == 'miles':
            return base_value / 1609.34
        elif toUnit == 'yards':
            return base_value / 0.9144
        else:  # meters
            return base_value

    
    raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} not implemented")
