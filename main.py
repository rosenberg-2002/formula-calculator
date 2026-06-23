"""
Formula Calculator - Desktop Application
A user-friendly GUI application for performing various mathematical calculations
High-DPI aware with dynamic scaling for all screen resolutions
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
from formulas import FORMULAS, calculate_formula


class FormulaCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Formula Calculator")
        
        # Get DPI scaling factor
        self.dpi_scale = self.calculate_dpi_scale()
        
        # Dynamic window sizing based on screen resolution
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate window size (responsive to screen size)
        window_width = min(int(1100 * self.dpi_scale), int(screen_width * 0.7))
        window_height = min(int(850 * self.dpi_scale), int(screen_height * 0.8))
        
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.resizable(True, True)
        
        # Set minimum window size
        min_width = int(800 * self.dpi_scale)
        min_height = int(600 * self.dpi_scale)
        self.root.minsize(min_width, min_height)
        
        # Set color scheme
        self.bg_color = "#f0f0f0"
        self.primary_color = "#2E86AB"
        self.secondary_color = "#A23B72"
        self.accent_color = "#F18F01"
        self.success_color = "#06A77D"
        
        self.root.configure(bg=self.bg_color)
        
        # Initialize UI
        self.setup_ui()
    
    def calculate_dpi_scale(self):
        """
        Calculate DPI scaling factor for high-resolution displays
        Returns a scale factor (1.0 for normal, 1.25 for 125%, 1.5 for 150%, etc.)
        """
        try:
            # Create a temporary root to get DPI info
            temp_root = tk.Tk()
            
            # Get the scaling value from tkinter
            scaling = temp_root.tk.call('tk', 'scaling')
            dpi = temp_root.winfo_fpixels('1i')
            
            temp_root.destroy()
            
            # Calculate scale factor (standard DPI is 96)
            # For 2.8K (typically 192+ DPI), scale factor would be around 2.0 or higher
            scale_factor = max(1.0, dpi / 96.0)
            return scale_factor
        except:
            # Fallback to 1.0 if detection fails
            return 1.0
    
    def scale(self, value):
        """
        Scale a value based on DPI
        Usage: self.scale(10) for paddings, widths, heights, etc.
        """
        return int(value * self.dpi_scale)
    
    def scale_font(self, size):
        """
        Scale font size based on DPI
        Usage: self.scale_font(12) for font sizes
        """
        return max(8, int(size * self.dpi_scale))
        
    def setup_ui(self):
        """Set up the main user interface with DPI-aware scaling"""
        # Header
        header_frame = tk.Frame(self.root, bg=self.primary_color, height=self.scale(80))
        header_frame.pack(fill=tk.X)
        
        header_label = tk.Label(
            header_frame,
            text="Formula Calculator",
            font=("Arial", self.scale_font(28), "bold"),
            bg=self.primary_color,
            fg="white"
        )
        header_label.pack(pady=self.scale(15))
        
        subtitle_label = tk.Label(
            header_frame,
            text="Calculate mathematical formulas with ease",
            font=("Arial", self.scale_font(10)),
            bg=self.primary_color,
            fg="white"
        )
        subtitle_label.pack()
        
        # Main content frame
        content_frame = tk.Frame(self.root, bg=self.bg_color)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=self.scale(20), pady=self.scale(20))
        
        # Left panel - Formula selection
        left_frame = tk.Frame(content_frame, bg=self.bg_color)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, self.scale(15)))
        
        formula_label = tk.Label(
            left_frame,
            text="Select Formula:",
            font=("Arial", self.scale_font(12), "bold"),
            bg=self.bg_color
        )
        formula_label.pack(anchor=tk.W, pady=(0, self.scale(10)))
        
        # Formula listbox with scrollbar
        scrollbar = ttk.Scrollbar(left_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.formula_listbox = tk.Listbox(
            left_frame,
            width=int(25 * (self.dpi_scale ** 0.5)),  # Adjust width for scaling
            height=int(22 * (self.dpi_scale ** 0.5)),  # Adjust height for scaling
            font=("Arial", self.scale_font(10)),
            yscrollcommand=scrollbar.set,
            bg="white",
            selectmode=tk.SINGLE
        )
        self.formula_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.formula_listbox.yview)
        
        # Populate formula list
        for formula_name in FORMULAS.keys():
            self.formula_listbox.insert(tk.END, formula_name)
        
        self.formula_listbox.bind("<<ListboxSelect>>", self.on_formula_selected)
        
        # Right panel - Formula details and input
        right_frame = tk.Frame(content_frame, bg="white", relief=tk.RAISED, bd=self.scale(2))
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Formula name display
        self.formula_title = tk.Label(
            right_frame,
            text="Select a formula",
            font=("Arial", self.scale_font(14), "bold"),
            bg=self.primary_color,
            fg="white",
            anchor=tk.W
        )
        self.formula_title.pack(fill=tk.X, padx=self.scale(15), pady=self.scale(10))
        
        # Formula description
        self.formula_description = tk.Label(
            right_frame,
            text="",
            font=("Arial", self.scale_font(9)),
            bg="white",
            fg="#333",
            wraplength=self.scale(350),
            justify=tk.LEFT,
            anchor=tk.NW
        )
        self.formula_description.pack(fill=tk.X, padx=self.scale(15), pady=(self.scale(5), self.scale(15)), anchor=tk.NW)
        
        # Input fields frame
        self.input_frame = tk.Frame(right_frame, bg="white")
        self.input_frame.pack(fill=tk.BOTH, expand=True, padx=self.scale(15), pady=self.scale(10))
        
        # Result display
        result_label = tk.Label(
            right_frame,
            text="Result:",
            font=("Arial", self.scale_font(11), "bold"),
            bg="white"
        )
        result_label.pack(anchor=tk.W, padx=self.scale(15), pady=(self.scale(10), self.scale(5)))
        
        self.result_display = tk.Label(
            right_frame,
            text="Enter values and click Calculate",
            font=("Arial", self.scale_font(12)),
            bg="#E8F5E9",
            fg=self.success_color,
            relief=tk.SUNKEN,
            bd=self.scale(2),
            height=2,
            wraplength=self.scale(350),
            justify=tk.LEFT
        )
        self.result_display.pack(fill=tk.X, padx=self.scale(15), pady=(0, self.scale(10)))
        
        # Button frame
        button_frame = tk.Frame(right_frame, bg="white")
        button_frame.pack(fill=tk.X, padx=self.scale(15), pady=self.scale(10))
        
        calculate_btn = tk.Button(
            button_frame,
            text="Calculate",
            command=self.calculate,
            bg=self.success_color,
            fg="white",
            font=("Arial", self.scale_font(11), "bold"),
            padx=self.scale(20),
            pady=self.scale(8),
            cursor="hand2"
        )
        calculate_btn.pack(side=tk.LEFT, padx=(0, self.scale(10)))
        
        clear_btn = tk.Button(
            button_frame,
            text="Clear",
            command=self.clear_inputs,
            bg=self.secondary_color,
            fg="white",
            font=("Arial", self.scale_font(11), "bold"),
            padx=self.scale(20),
            pady=self.scale(8),
            cursor="hand2"
        )
        clear_btn.pack(side=tk.LEFT, padx=(0, self.scale(10)))
        
        help_btn = tk.Button(
            button_frame,
            text="Help",
            command=self.show_help,
            bg=self.accent_color,
            fg="white",
            font=("Arial", self.scale_font(11), "bold"),
            padx=self.scale(20),
            pady=self.scale(8),
            cursor="hand2"
        )
        help_btn.pack(side=tk.LEFT)
        
        self.input_fields = {}
        self.current_formula = None  # Track selected formula even when focus changes
        
    def on_formula_selected(self, event):
        """Handle formula selection"""
        selection = self.formula_listbox.curselection()
        if not selection:
            return
        
        formula_name = self.formula_listbox.get(selection[0])
        formula_data = FORMULAS[formula_name]
        
        # Store the current formula so it's accessible even when focus changes
        self.current_formula = formula_name
        
        # Update title and description
        self.formula_title.config(text=formula_name)
        self.formula_description.config(
            text=formula_data['description'],
            wraplength=self.scale(350)
        )
        
        # Clear previous input fields
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        self.input_fields.clear()
        
        # Create input fields with Tab navigation
        entry_list = []  # Keep list for Tab navigation
        for param in formula_data['parameters']:
            param_frame = tk.Frame(self.input_frame, bg="white")
            param_frame.pack(fill=tk.X, pady=self.scale(8))
            
            label = tk.Label(
                param_frame,
                text=f"{param['name']} ({param['unit']}):",
                font=("Arial", self.scale_font(10)),
                bg="white",
                width=int(20 * (self.dpi_scale ** 0.5)),
                anchor=tk.W
            )
            label.pack(side=tk.LEFT)
            
            entry = tk.Entry(
                param_frame,
                font=("Arial", self.scale_font(10)),
                width=int(20 * (self.dpi_scale ** 0.5)),
                bg="white",
                relief=tk.SUNKEN,
                bd=1
            )
            entry.pack(side=tk.LEFT, padx=(self.scale(10), 0))
            
            self.input_fields[param['name']] = entry
            entry_list.append(entry)
        
        # Setup Tab navigation between input fields
        if entry_list:
            for idx, entry in enumerate(entry_list):
                # Create a closure to capture the current index and list
                def create_tab_handler(current_idx, entries):
                    def handle_tab(event):
                        # Move to next field, or wrap to first
                        next_idx = (current_idx + 1) % len(entries)
                        entries[next_idx].focus()
                        return "break"  # Prevent default Tab behavior
                    return handle_tab
                
                def create_shift_tab_handler(current_idx, entries):
                    def handle_shift_tab(event):
                        # Move to previous field, or wrap to last
                        prev_idx = (current_idx - 1) % len(entries)
                        entries[prev_idx].focus()
                        return "break"  # Prevent default Shift+Tab behavior
                    return handle_shift_tab
                
                # Bind Tab and Shift+Tab
                entry.bind('<Tab>', create_tab_handler(idx, entry_list))
                entry.bind('<Shift-Tab>', create_shift_tab_handler(idx, entry_list))
                
                # Bind Enter to calculate (nice UX feature)
                entry.bind('<Return>', lambda e: self.calculate())
            
            # Focus on first entry field
            entry_list[0].focus()
        
        # Clear result
        self.result_display.config(
            text="Enter values and click Calculate",
            bg="#E8F5E9",
            fg=self.success_color,
            wraplength=self.scale(350)
        )
    
    def calculate(self):
        """Perform the calculation"""
        # Use stored formula instead of relying on listbox selection
        # This prevents issues when focus changes
        if not self.current_formula:
            messagebox.showwarning("Warning", "Please select a formula first")
            return
        
        formula_name = self.current_formula
        formula_data = FORMULAS[formula_name]
        
        # Collect input values
        values = {}
        try:
            for param_name, entry in self.input_fields.items():
                value_text = entry.get().strip()
                if not value_text:
                    messagebox.showerror("Error", f"Please enter {param_name}")
                    return
                values[param_name] = float(value_text)
        except ValueError:
            messagebox.showerror("Error", "All inputs must be valid numbers")
            return
        
        # Perform calculation
        try:
            result = calculate_formula(formula_name, values)
            output_unit = formula_data.get('output_unit', '')
            result_text = f"Result: {result:.6g} {output_unit}".strip()
            
            self.result_display.config(
                text=result_text,
                bg="#E8F5E9",
                fg=self.success_color
            )
        except Exception as e:
            messagebox.showerror("Calculation Error", str(e))
            self.result_display.config(
                text=f"Error: {str(e)}",
                bg="#FFEBEE",
                fg="#C62828"
            )
    
    def clear_inputs(self):
        """Clear all input fields"""
        for entry in self.input_fields.values():
            entry.delete(0, tk.END)
        self.result_display.config(
            text="Enter values and click Calculate",
            bg="#E8F5E9",
            fg=self.success_color
        )
    
    def show_help(self):
        """Show help window with DPI-aware scaling"""
        help_window = tk.Toplevel(self.root)
        help_window.title("Help & Tutorial")
        
        # Dynamic help window size based on screen
        help_width = self.scale(600)
        help_height = self.scale(500)
        help_window.geometry(f"{help_width}x{help_height}")
        
        help_text = """
FORMULA CALCULATOR - USER GUIDE

How to Use:
1. Select a formula from the list on the left
2. Read the formula description to understand what it calculates
3. Enter the required values in the input fields
4. Click "Calculate" to see the result

Available Formulas:
• Quadratic Equation: Solves ax² + bx + c = 0 for x
• Pythagorean Theorem: Calculates c = √(a² + b²)
• Circle Area: Calculates the area of a circle (πr²)
• Rectangle Area: Calculates the area of a rectangle (l × w)
• Triangle Area: Calculates the area using Heron's formula
• Distance Formula: Calculates distance between two points
• Simple Interest: Calculates I = (P × R × T) / 100
• Compound Interest: Calculates A = P(1 + r/n)^(nt)
• Celsius to Fahrenheit: Temperature conversion
• Body Mass Index (BMI): Health metric calculation
• Kinetic Energy: Calculates KE = ½mv²
• Ohm's Law: Calculates V = I × R

Tips:
• Use decimal points for decimal numbers (e.g., 3.5 not 3,5)
• Negative numbers are supported
• Results are displayed with up to 6 significant figures
• Click "Clear" to reset input fields and start over

For more information, refer to the README.md file.
        """
        
        text_widget = scrolledtext.ScrolledText(
            help_window,
            font=("Courier", self.scale_font(10)),
            wrap=tk.WORD,
            bg="white"
        )
        text_widget.pack(fill=tk.BOTH, expand=True, padx=self.scale(10), pady=self.scale(10))
        text_widget.insert(tk.END, help_text)
        text_widget.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    app = FormulaCalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
