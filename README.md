# Formula Calculator - Desktop Application

A user-friendly Python desktop application for performing various mathematical calculations. Choose from 15+ built-in formulas, input your values, and get instant results with a modern, intuitive interface.

## Features

✨ **Key Features:**
- 🧮 **15+ Built-in Formulas** - Covers algebra, geometry, physics, finance, and more
- 🎨 **Modern UI/UX Design** - Clean, intuitive interface with color-coded elements
- ⚡ **Real-time Calculations** - Get instant results
- 📋 **Easy Parameter Entry** - Clear input fields with unit labels
- 🛡️ **Input Validation** - Prevents invalid calculations and shows helpful error messages
- 📖 **Built-in Help System** - Learn how to use each formula

## Available Formulas

### Algebra & Equations
1. **Quadratic Equation** - Solves ax² + bx + c = 0
   - Input: Coefficients a, b, c
   - Output: x value (first real root)

### Geometry
2. **Circle Area** - Calculate area of a circle
   - Input: Radius
   - Output: Area (square units)

3. **Rectangle Area** - Calculate area of a rectangle
   - Input: Length, Width
   - Output: Area (square units)

4. **Triangle Area (Heron's Formula)** - Calculate area of any triangle
   - Input: Three side lengths
   - Output: Area (square units)

5. **Pythagorean Theorem** - Find hypotenuse of right triangle
   - Input: Two sides (a, b)
   - Output: Hypotenuse (c)

6. **Sphere Volume** - Calculate volume of a sphere
   - Input: Radius
   - Output: Volume (cubic units)

### Distance & Coordinates
7. **Distance Formula** - Calculate distance between two points
   - Input: x₁, y₁, x₂, y₂ coordinates
   - Output: Distance

### Physics
8. **Kinetic Energy** - Calculate kinetic energy
   - Input: Mass (kg), Velocity (m/s)
   - Output: Energy (Joules)
   - Formula: KE = ½mv²

9. **Ohm's Law** - Calculate voltage
   - Input: Current (Amperes), Resistance (Ohms)
   - Output: Voltage (Volts)
   - Formula: V = I × R

10. **Power (Electrical)** - Calculate electrical power
    - Input: Voltage (V), Current (A)
    - Output: Power (Watts)
    - Formula: P = V × I

### Finance
11. **Simple Interest** - Calculate simple interest earned
    - Input: Principal, Rate (% per year), Time (years)
    - Output: Interest earned
    - Formula: I = (P × R × T) / 100

12. **Compound Interest** - Calculate compound interest
    - Input: Principal, Rate (% per year), Time (years), Compounds per year
    - Output: Interest earned
    - Formula: A = P(1 + r/n)^(nt)

### Temperature
13. **Celsius to Fahrenheit** - Convert temperature
    - Input: Temperature in Celsius
    - Output: Temperature in Fahrenheit
    - Formula: F = (C × 9/5) + 32

14. **Fahrenheit to Celsius** - Convert temperature
    - Input: Temperature in Fahrenheit
    - Output: Temperature in Celsius
    - Formula: C = (F - 32) × 5/9

### Health & Medicine
15. **Body Mass Index (BMI)** - Calculate health metric
    - Input: Weight (kg), Height (m)
    - Output: BMI (kg/m²)
    - Formula: BMI = weight / height²

### General Math
16. **Percentage** - Calculate percentage
    - Input: Value, Total
    - Output: Percentage (%)
    - Formula: P = (Value / Total) × 100

## Installation & Setup

### Requirements
- Python 3.6 or higher
- tkinter (usually included with Python)

### Installation Steps

1. **Clone or download this project** to your computer
   ```bash
   cd python_app
   ```

2. **Install dependencies** (if needed)
   ```bash
   pip install -r requirements.txt
   ```
   
   Note: This project only requires tkinter, which comes with Python. If you have any issues, ensure you have the latest Python version installed.

3. **Run the application**
   ```bash
   python main.py
   ```

## How to Use

### Step-by-Step Guide

1. **Launch the Application**
   - Run `python main.py` in your terminal
   - The Formula Calculator window will open

2. **Select a Formula**
   - Browse the list of formulas on the left side
   - Click on any formula to select it
   - The formula description will appear on the right side

3. **Enter Values**
   - Read the formula description to understand what each parameter means
   - Enter numerical values in the input fields
   - Each field shows the expected unit (e.g., meters, kg, percentage)

4. **Calculate**
   - Click the "Calculate" button to perform the calculation
   - The result will appear in the result display area
   - The result shows the value with the appropriate unit

5. **Clear & Try Again**
   - Click "Clear" to reset all input fields
   - Select another formula and repeat

### Important Tips

✅ **Input Guidelines:**
- Use **decimal points** for decimal numbers (e.g., 3.5, not 3,5)
- **Negative numbers** are supported where applicable
- All inputs must be **valid numbers**
- Fields cannot be left empty

❌ **Common Errors:**
- "Please enter [field name]" - You forgot to fill in a required field
- "All inputs must be valid numbers" - Check that all entries are numbers
- "No real roots (discriminant < 0)" - Quadratic equation has no real solutions
- "Invalid triangle" - Triangle sides don't satisfy triangle inequality theorem

✨ **Features:**
- Results display up to **6 significant figures** for precision
- Hover over fields to see helpful tooltips
- Results maintain appropriate **decimal precision**
- **Color-coded interface** for easy navigation

## Application Interface Overview

### Main Layout

```
┌─────────────────────────────────────────────────────────┐
│        FORMULA CALCULATOR (Header)                      │
├──────────────────┬──────────────────────────────────────┤
│                  │                                      │
│ Select Formula:  │ Formula Details                     │
│                  │ • Description                       │
│ [Formula List]   │ • Input Fields                      │
│ • Quadratic Eq   │ • Result Display                    │
│ • Pythagorean    │ • Calculate/Clear/Help Buttons      │
│ • Circle Area    │                                      │
│ • etc...         │                                      │
│                  │                                      │
└──────────────────┴──────────────────────────────────────┘
```

### Color Scheme
- **Primary Blue** (#2E86AB) - Header and main accents
- **Secondary Purple** (#A23B72) - Secondary buttons
- **Orange** (#F18F01) - Help button
- **Green** (#06A77D) - Calculate button
- **Light Gray** (#f0f0f0) - Background

## File Structure

```
python_app/
├── main.py              # Main application GUI
├── formulas.py          # Formula definitions and calculations
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Project Structure Details

### main.py
- Implements the `FormulaCalculatorApp` class
- Manages the GUI using tkinter
- Handles user interactions and input validation
- Displays results and error messages

### formulas.py
- Defines all 16 available formulas
- Each formula includes description, parameters, and units
- `calculate_formula()` function performs calculations
- Input validation and error handling

## Troubleshooting

### Application won't start
- **Solution:** Ensure Python 3.6+ is installed: `python --version`
- **Solution:** Check tkinter is installed: `python -m tkinter` (should open a test window)

### Formulas not calculating
- **Solution:** Verify all input fields are filled with valid numbers
- **Solution:** Check the formula description for correct parameter format
- **Solution:** Look at error messages for specific issues

### Display issues
- **Solution:** Resize the window or check your screen resolution (recommended 1920x1080+)
- **Solution:** On macOS, ensure you're using Python 3.8+ for proper tkinter display

## Future Enhancements

Potential features for future versions:
- 📊 Calculation history and export to CSV
- 📱 Web version using Flask/Django
- 🔧 Custom formula editor (users can create own formulas)
- 🎯 Advanced scientific calculations
- 📈 Graph plotting for results visualization
- 🌍 Multilingual interface
- 💾 Save favorite formulas
- 🔄 Unit conversion helpers

## Credits & License

Created as an educational Python desktop application project.

Built with:
- Python 3.x
- tkinter (GUI framework)
- math (calculations)

## Support & Feedback

For issues, suggestions, or questions:
1. Check the built-in Help (click "Help" button)
2. Review this README document
3. Verify your input values are correct
4. Check that you're using the latest version

---

**Enjoy calculating! 🧮**

Happy computing with the Formula Calculator!
