# Formula Calculator

A Python web app with 16 built-in formulas. Runs a local server and opens in your browser automatically — no external packages needed.

## Formulas

| Category | Formula | Equation |
|---|---|---|
| Algebra | Quadratic Equation | `x = (-b ± √(b²-4ac)) / 2a` |
| Geometry | Circle Area | `A = πr²` |
| Geometry | Rectangle Area | `A = l × w` |
| Geometry | Triangle Area (Heron's) | `A = √(s(s-a)(s-b)(s-c))` |
| Geometry | Pythagorean Theorem | `c = √(a² + b²)` |
| Geometry | Sphere Volume | `V = (4/3)πr³` |
| Geometry | Distance Formula | `d = √((x₂-x₁)² + (y₂-y₁)²)` |
| Physics | Kinetic Energy | `KE = ½mv²` |
| Physics | Ohm's Law | `V = I × R` |
| Physics | Electrical Power | `P = V × I` |
| Finance | Simple Interest | `I = (P × R × T) / 100` |
| Finance | Compound Interest | `A = P(1 + r/n)^(nt)` |
| Temperature | Celsius → Fahrenheit | `F = (C × 9/5) + 32` |
| Temperature | Fahrenheit → Celsius | `C = (F - 32) × 5/9` |
| Health | BMI | `BMI = weight / height²` |
| Math | Percentage | `P = (Value / Total) × 100` |

## Requirements

- Python 3.8+
- No external packages — uses Python's built-in `http.server`

## Run

```bash
git clone https://github.com/rosenberg-2002/formula-calculator.git
cd formula-calculator
python main.py
```

Your browser opens automatically at `http://127.0.0.1:5050`.

## Features

- Clean two-panel web UI — sidebar with search, main content area
- **Step-by-step solutions** — every calculation shows the full working, animated
- Cycling live demo on the home screen
- Searchable formula list grouped by category
- Press **Enter** to calculate from anywhere

## Usage

1. Pick a formula from the sidebar
2. Fill in the input fields
3. Press **Enter** or click **Calculate**
4. See the step-by-step solution animate in

## License

MIT
