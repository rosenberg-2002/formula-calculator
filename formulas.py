"""
Formulas module - Contains all available formulas and calculation logic
"""

import math

# Define all available formulas
FORMULAS = {
    "Quadratic Equation": {
        "description": "Solves quadratic equations of the form ax² + bx + c = 0. Returns the first real root. Formula: x = (-b + √(b² - 4ac)) / 2a",
        "parameters": [
            {"name": "a", "unit": "coefficient"},
            {"name": "b", "unit": "coefficient"},
            {"name": "c", "unit": "coefficient"}
        ],
        "output_unit": ""
    },
    "Pythagorean Theorem": {
        "description": "Calculates the hypotenuse of a right triangle. Formula: c = √(a² + b²)",
        "parameters": [
            {"name": "a", "unit": "units"},
            {"name": "b", "unit": "units"}
        ],
        "output_unit": "units"
    },
    "Circle Area": {
        "description": "Calculates the area of a circle. Formula: A = πr²",
        "parameters": [
            {"name": "radius", "unit": "units"}
        ],
        "output_unit": "sq units"
    },
    "Rectangle Area": {
        "description": "Calculates the area of a rectangle. Formula: A = length × width",
        "parameters": [
            {"name": "length", "unit": "units"},
            {"name": "width", "unit": "units"}
        ],
        "output_unit": "sq units"
    },
    "Triangle Area (Heron's Formula)": {
        "description": "Calculates the area of a triangle given three sides. Formula: A = √(s(s-a)(s-b)(s-c)) where s = (a+b+c)/2",
        "parameters": [
            {"name": "side_a", "unit": "units"},
            {"name": "side_b", "unit": "units"},
            {"name": "side_c", "unit": "units"}
        ],
        "output_unit": "sq units"
    },
    "Distance Formula": {
        "description": "Calculates the distance between two points in 2D space. Formula: d = √((x₂-x₁)² + (y₂-y₁)²)",
        "parameters": [
            {"name": "x1", "unit": "coordinate"},
            {"name": "y1", "unit": "coordinate"},
            {"name": "x2", "unit": "coordinate"},
            {"name": "y2", "unit": "coordinate"}
        ],
        "output_unit": "units"
    },
    "Simple Interest": {
        "description": "Calculates simple interest. Formula: I = (P × R × T) / 100, where P=Principal, R=Rate (%), T=Time (years)",
        "parameters": [
            {"name": "principal", "unit": "currency"},
            {"name": "rate", "unit": "%/year"},
            {"name": "time", "unit": "years"}
        ],
        "output_unit": "currency"
    },
    "Compound Interest": {
        "description": "Calculates compound interest. Formula: A = P(1 + r/n)^(nt), where P=Principal, r=Rate, n=Compounds/year, t=Time (years)",
        "parameters": [
            {"name": "principal", "unit": "currency"},
            {"name": "rate", "unit": "%/year"},
            {"name": "time", "unit": "years"},
            {"name": "compounds_per_year", "unit": "frequency"}
        ],
        "output_unit": "currency"
    },
    "Celsius to Fahrenheit": {
        "description": "Converts temperature from Celsius to Fahrenheit. Formula: F = (C × 9/5) + 32",
        "parameters": [
            {"name": "celsius", "unit": "°C"}
        ],
        "output_unit": "°F"
    },
    "Fahrenheit to Celsius": {
        "description": "Converts temperature from Fahrenheit to Celsius. Formula: C = (F - 32) × 5/9",
        "parameters": [
            {"name": "fahrenheit", "unit": "°F"}
        ],
        "output_unit": "°C"
    },
    "Body Mass Index (BMI)": {
        "description": "Calculates BMI. Formula: BMI = weight(kg) / height(m)\u00B2. Enter height in centimeters.",
        "parameters": [
            {"name": "weight", "unit": "kg"},
            {"name": "height", "unit": "cm"}
        ],
        "output_unit": "kg/m²"
    },
    "Kinetic Energy": {
        "description": "Calculates kinetic energy. Formula: KE = ½mv², where m=mass (kg), v=velocity (m/s)",
        "parameters": [
            {"name": "mass", "unit": "kg"},
            {"name": "velocity", "unit": "m/s"}
        ],
        "output_unit": "Joules"
    },
    "Ohm's Law": {
        "description": "Calculates voltage. Formula: V = I × R, where I=Current (Amperes), R=Resistance (Ohms)",
        "parameters": [
            {"name": "current", "unit": "A"},
            {"name": "resistance", "unit": "Ω"}
        ],
        "output_unit": "V"
    },
    "Power (Electrical)": {
        "description": "Calculates electrical power. Formula: P = V × I, where V=Voltage, I=Current",
        "parameters": [
            {"name": "voltage", "unit": "V"},
            {"name": "current", "unit": "A"}
        ],
        "output_unit": "Watts"
    },
    "Percentage": {
        "description": "Calculates percentage. Formula: P = (Value / Total) × 100",
        "parameters": [
            {"name": "value", "unit": "number"},
            {"name": "total", "unit": "number"}
        ],
        "output_unit": "%"
    },
    "Sphere Volume": {
        "description": "Calculates the volume of a sphere. Formula: V = (4/3)πr³",
        "parameters": [
            {"name": "radius", "unit": "units"}
        ],
        "output_unit": "cubic units"
    }
}


def calculate_formula(formula_name, values):
    """
    Calculate the result for a given formula with provided values
    
    Args:
        formula_name: Name of the formula to calculate
        values: Dictionary with parameter names as keys and values as floats
    
    Returns:
        float: The calculated result
    
    Raises:
        ValueError: If calculation is not possible
    """
    
    if formula_name == "Quadratic Equation":
        a, b, c = values["a"], values["b"], values["c"]
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            raise ValueError("No real roots (discriminant < 0)")
        return (-b + math.sqrt(discriminant)) / (2*a)
    
    elif formula_name == "Pythagorean Theorem":
        a, b = values["a"], values["b"]
        return math.sqrt(a**2 + b**2)
    
    elif formula_name == "Circle Area":
        radius = values["radius"]
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius**2
    
    elif formula_name == "Rectangle Area":
        length, width = values["length"], values["width"]
        if length < 0 or width < 0:
            raise ValueError("Length and width must be positive")
        return length * width
    
    elif formula_name == "Triangle Area (Heron's Formula)":
        a, b, c = values["side_a"], values["side_b"], values["side_c"]
        
        # Validate triangle inequality
        if a + b <= c or b + c <= a or a + c <= b:
            raise ValueError("Invalid triangle: sides do not satisfy triangle inequality")
        
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    
    elif formula_name == "Distance Formula":
        x1, y1, x2, y2 = values["x1"], values["y1"], values["x2"], values["y2"]
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    elif formula_name == "Simple Interest":
        principal, rate, time = values["principal"], values["rate"], values["time"]
        return (principal * rate * time) / 100
    
    elif formula_name == "Compound Interest":
        principal = values["principal"]
        rate = values["rate"]
        time = values["time"]
        compounds = values["compounds_per_year"]
        
        r = rate / 100
        amount = principal * (1 + r/compounds)**(compounds * time)
        return amount - principal  # Return interest, not total amount
    
    elif formula_name == "Celsius to Fahrenheit":
        celsius = values["celsius"]
        return (celsius * 9/5) + 32
    
    elif formula_name == "Fahrenheit to Celsius":
        fahrenheit = values["fahrenheit"]
        return (fahrenheit - 32) * 5/9
    
    elif formula_name == "Body Mass Index (BMI)":
        weight, height = values["weight"], values["height"]
        if height <= 0:
            raise ValueError("Height must be positive")
        height_m = height / 100
        return weight / (height_m ** 2)
    
    elif formula_name == "Kinetic Energy":
        mass, velocity = values["mass"], values["velocity"]
        return 0.5 * mass * velocity**2
    
    elif formula_name == "Ohm's Law":
        current, resistance = values["current"], values["resistance"]
        return current * resistance
    
    elif formula_name == "Power (Electrical)":
        voltage, current = values["voltage"], values["current"]
        return voltage * current
    
    elif formula_name == "Percentage":
        value, total = values["value"], values["total"]
        if total == 0:
            raise ValueError("Total cannot be zero")
        return (value / total) * 100
    
    elif formula_name == "Sphere Volume":
        radius = values["radius"]
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return (4/3) * math.pi * radius**3
    
    else:
        raise ValueError(f"Unknown formula: {formula_name}")
