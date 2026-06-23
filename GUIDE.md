# Formula Calculator — User Guide

## Run

**From source:**
```bash
python main.py
```

**Standalone (no Python needed):**  
Download `Formula.Calculator.exe` from [Releases](https://github.com/rosenberg-2002/formula-calculator/releases) and double-click it.

---

## How to Use

1. Pick a formula from the left panel
2. Enter values in the fields (use **Tab** to move between them)
3. Press **Enter** or click **Calculate**
4. Click **Clear** to reset and try another formula

---

## Examples

**Circle Area** — Garden with radius 5 m  
→ Select *Circle Area*, enter `5`, calculate → `78.54 sq units`

**Temperature** — Convert 25°C to Fahrenheit  
→ Select *Celsius to Fahrenheit*, enter `25`, calculate → `77 °F`

**BMI** — Weight 70 kg, height 1.75 m  
→ Select *Body Mass Index*, enter `70` and `1.75`, calculate → `22.86 kg/m²`

**Pythagorean Theorem** — Right triangle with sides 3 and 4  
→ Select *Pythagorean Theorem*, enter `3` and `4`, calculate → `5 units`

---

## Tips

- Use `.` for decimals (`3.5`, not `3,5`)
- Negative numbers are supported where valid
- Results are shown to 6 significant figures
- Press **Help** in the app for a quick in-app reference

---

## Troubleshooting

| Problem | Fix |
|---|---|
| App won't start | Run `python -m tkinter` to verify tkinter works |
| "No real roots" | Quadratic has no real solution (discriminant < 0) |
| "Invalid triangle" | Side lengths don't satisfy the triangle inequality |
| Blurry text on HiDPI | The app auto-detects DPI — try resizing the window |
