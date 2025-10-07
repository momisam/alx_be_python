def safe_divide(numerator, denominator):
    """Performs division with error handling for invalid input and zero division."""
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Perform division safely
        result = num / den
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
