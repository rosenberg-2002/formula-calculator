# Formula Calculator

A Python desktop app with 16 built-in formulas across algebra, geometry, physics, finance, and more.

| Category | Formula | Equation |
|---|---|---|
| Algebra | Quadratic Equation | `x = (-b ± √(b²-4ac)) / 2a` |
| Geometry | Circle Area | `A = πr²` |
| Geometry | Rectangle Area | `A = l × w` |
| Geometry | Triangle Area (Heron's) | `A = √(s(s-a)(s-b)(s-c))` |
| Geometry | Pythagorean Theorem | `c = √(a² + b²)` |
| Geometry | Sphere Volume | `V = (4/3)πr³` |
| Coordinate | Distance Formula | `d = √((x₂-x₁)² + (y₂-y₁)²)` |
| Physics | Kinetic Energy | `KE = ½mv²` |
| Physics | Ohm's Law | `V = I × R` |
| Physics | Electrical Power | `P = V × I` |
| Finance | Simple Interest | `I = (P × R × T) / 100` |
| Finance | Compound Interest | `A = P(1 + r/n)^(nt)` |
| Temperature | Celsius → Fahrenheit | `F = (C × 9/5) + 32` |
| Temperature | Fahrenheit → Celsius | `C = (F - 32) × 5/9` |
| Health | BMI | `BMI = weight / height²` |
| General | Percentage | `P = (Value / Total) × 100` |

## Requirements

- Python 3.6+
- tkinter (included with Python)

## Run

```bash
git clone https://github.com/rosenberg-2002/formula-calculator.git
cd formula-calculator
python main.py
```

Or download `Formula.Calculator.exe` from [Releases](https://github.com/rosenberg-2002/formula-calculator/releases) and run it directly — no Python needed.

## Usage

1. Select a formula from the left panel
2. Enter values in the input fields (Tab to move between fields)
3. Press Enter or click **Calculate**

## License

MIT
