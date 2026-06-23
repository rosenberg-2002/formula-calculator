"""
Formula Calculator - Desktop Application
UI redesigned after a desktop messaging app (two-panel, chat-bubble style).
"""

import tkinter as tk
from tkinter import ttk, messagebox
from formulas import FORMULAS, calculate_formula

# ── Palette ─────────────────────────────────────────────────────────────────
WHITE        = "#FFFFFF"
BG_APP       = "#E4E6EB"
BG_CHAT      = "#F0F2F5"
BORDER       = "#E3E6EA"
SEL_BG       = "#EEF2FF"
HOV_BG       = "#F7F8FA"
TX_PRIMARY   = "#111827"
TX_SECONDARY = "#6B7280"
TX_LIGHT     = "#9CA3AF"
TX_WHITE     = "#FFFFFF"
BLUE         = "#5B7AF5"
BLUE_DARK    = "#4A67E3"
ORANGE       = "#FF6B35"

CATEGORIES = {
    "Algebra":     ("#8B5CF6", "#EDE9FE"),
    "Geometry":    ("#3B82F6", "#DBEAFE"),
    "Physics":     ("#EF4444", "#FEE2E2"),
    "Finance":     ("#10B981", "#D1FAE5"),
    "Temperature": ("#F97316", "#FFEDD5"),
    "Health":      ("#EC4899", "#FCE7F3"),
    "General":     ("#6B7280", "#F3F4F6"),
    "Coordinate":  ("#06B6D4", "#CFFAFE"),
}

FORMULA_CATEGORY = {
    "Quadratic Equation":              "Algebra",
    "Pythagorean Theorem":             "Geometry",
    "Circle Area":                     "Geometry",
    "Rectangle Area":                  "Geometry",
    "Triangle Area (Heron's Formula)": "Geometry",
    "Distance Formula":                "Coordinate",
    "Simple Interest":                 "Finance",
    "Compound Interest":               "Finance",
    "Celsius to Fahrenheit":           "Temperature",
    "Fahrenheit to Celsius":           "Temperature",
    "Body Mass Index (BMI)":           "Health",
    "Kinetic Energy":                  "Physics",
    "Ohm's Law":                       "Physics",
    "Power (Electrical)":              "Physics",
    "Percentage":                      "General",
    "Sphere Volume":                   "Geometry",
}

FORMULA_EQ = {
    "Quadratic Equation":              "x = (\u2212b \u00b1 \u221a(b\u00b2\u22124ac)) / 2a",
    "Pythagorean Theorem":             "c = \u221a(a\u00b2 + b\u00b2)",
    "Circle Area":                     "A = \u03c0r\u00b2",
    "Rectangle Area":                  "A = l \u00d7 w",
    "Triangle Area (Heron's Formula)": "A = \u221a(s(s\u2212a)(s\u2212b)(s\u2212c))",
    "Distance Formula":                "d = \u221a((x\u2082\u2212x\u2081)\u00b2 + (y\u2082\u2212y\u2081)\u00b2)",
    "Simple Interest":                 "I = (P \u00d7 R \u00d7 T) / 100",
    "Compound Interest":               "A = P(1 + r/n)^(nt)",
    "Celsius to Fahrenheit":           "F = (C \u00d7 9/5) + 32",
    "Fahrenheit to Celsius":           "C = (F \u2212 32) \u00d7 5/9",
    "Body Mass Index (BMI)":           "BMI = weight / height\u00b2",
    "Kinetic Energy":                  "KE = \u00bdmv\u00b2",
    "Ohm's Law":                       "V = I \u00d7 R",
    "Power (Electrical)":              "P = V \u00d7 I",
    "Percentage":                      "P = (Value / Total) \u00d7 100",
    "Sphere Volume":                   "V = (4/3)\u03c0r\u00b3",
}


class FormulaCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Formula Calculator")
        self.root.configure(bg=BG_APP)

        self.dpi = self._dpi_scale()

        sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
        w = min(self.s(1020), int(sw * 0.75))
        h = min(self.s(700),  int(sh * 0.85))
        root.geometry(f"{w}x{h}+{(sw - w) // 2}+{(sh - h) // 2}")
        root.minsize(self.s(720), self.s(480))
        root.resizable(True, True)

        self.current_formula   = None
        self.input_fields      = {}
        self._items            = {}
        self._selected         = None
        self._search_var       = tk.StringVar()
        self._search_var.trace_add("write", self._on_search)
        self._body_canvas      = None
        self._result_container = None

        self._build()

    def _dpi_scale(self):
        try:
            t = tk.Tk()
            dpi = t.winfo_fpixels("1i")
            t.destroy()
            return max(1.0, dpi / 96.0)
        except Exception:
            return 1.0

    def s(self, v):  return int(v * self.dpi)
    def sf(self, v): return max(8, int(v * self.dpi))

    def _build(self):
        wrap = tk.Frame(self.root, bg=BG_APP)
        wrap.pack(fill=tk.BOTH, expand=True, padx=self.s(10), pady=self.s(10))
        win = tk.Frame(wrap, bg=WHITE)
        win.pack(fill=tk.BOTH, expand=True)
        self._build_titlebar(win)
        body = tk.Frame(win, bg=WHITE)
        body.pack(fill=tk.BOTH, expand=True)
        sidebar = tk.Frame(body, bg=WHITE, width=self.s(275))
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        sidebar.pack_propagate(False)
        self._build_sidebar(sidebar)
        tk.Frame(body, bg=BORDER, width=1).pack(side=tk.LEFT, fill=tk.Y)
        content = tk.Frame(body, bg=BG_CHAT)
        content.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self._build_content(content)

    def _build_titlebar(self, parent):
        bar = tk.Frame(parent, bg=WHITE, height=self.s(40))
        bar.pack(fill=tk.X)
        bar.pack_propagate(False)
        c = tk.Canvas(bar, width=self.s(20), height=self.s(20), bg=WHITE, highlightthickness=0)
        c.pack(side=tk.LEFT, padx=(self.s(14), self.s(6)), pady=self.s(10))
        c.create_oval(1, 1, self.s(19), self.s(19), fill=ORANGE, outline="")
        tk.Label(bar, text="Formula Calculator", font=("Segoe UI", self.sf(9), "bold"),
                 bg=WHITE, fg=TX_PRIMARY).pack(side=tk.LEFT)
        for sym, cmd in [("\u2014", None), ("\u25a1", None), ("\u2715", self.root.destroy)]:
            b = tk.Label(bar, text=sym, font=("Segoe UI", self.sf(10)),
                         bg=WHITE, fg=TX_SECONDARY, padx=self.s(12), pady=self.s(8), cursor="hand2")
            b.pack(side=tk.RIGHT)
            b.bind("<Button-1>", lambda e, fn=cmd: fn and fn())
            b.bind("<Enter>", lambda e, w=b: w.config(bg="#F0F0F0"))
            b.bind("<Leave>", lambda e, w=b: w.config(bg=WHITE))
        tk.Frame(parent, bg=BORDER, height=1).pack(fill=tk.X)

    def _build_sidebar(self, parent):
        hdr = tk.Frame(parent, bg=WHITE)
        hdr.pack(fill=tk.X, padx=self.s(14), pady=(self.s(12), self.s(6)))
        tk.Label(hdr, text="Formulas", font=("Segoe UI", self.sf(12), "bold"),
                 bg=WHITE, fg=TX_PRIMARY).pack(side=tk.LEFT)
        tk.Label(hdr, text=f" {len(FORMULAS)} ", font=("Segoe UI", self.sf(8), "bold"),
                 bg=BLUE, fg=TX_WHITE).pack(side=tk.LEFT, padx=self.s(8))
        sb = tk.Frame(parent, bg="#F0F2F5", highlightthickness=1, highlightbackground=BORDER)
        sb.pack(fill=tk.X, padx=self.s(12), pady=(0, self.s(8)))
        tk.Label(sb, text="\u2315", font=("Segoe UI", self.sf(10)),
                 bg="#F0F2F5", fg=TX_LIGHT).pack(side=tk.LEFT, padx=(self.s(8), 0))
        self._search_entry = tk.Entry(sb, textvariable=self._search_var,
                                      font=("Segoe UI", self.sf(9)), bg="#F0F2F5",
                                      fg=TX_SECONDARY, relief=tk.FLAT, bd=0,
                                      insertbackground=TX_PRIMARY)
        self._search_entry.pack(fill=tk.X, expand=True, padx=self.s(4), pady=self.s(7))
        self._search_entry.insert(0, "Search formulas...")
        self._search_entry.bind("<FocusIn>",  self._search_focus_in)
        self._search_entry.bind("<FocusOut>", self._search_focus_out)
        lf = tk.Frame(parent, bg=WHITE)
        lf.pack(fill=tk.BOTH, expand=True)
        self._list_canvas = tk.Canvas(lf, bg=WHITE, highlightthickness=0)
        vsb = ttk.Scrollbar(lf, orient="vertical", command=self._list_canvas.yview)
        self._list_inner = tk.Frame(self._list_canvas, bg=WHITE)
        self._list_inner.bind("<Configure>", lambda e: self._list_canvas.configure(
            scrollregion=self._list_canvas.bbox("all")))
        self._list_canvas.create_window((0, 0), window=self._list_inner, anchor="nw")
        self._list_canvas.configure(yscrollcommand=vsb.set)
        self._list_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self._list_canvas.bind("<MouseWheel>",
            lambda e: self._list_canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
        self._populate_list()

    def _search_focus_in(self, _):
        if self._search_entry.get() == "Search formulas...":
            self._search_entry.delete(0, tk.END)
            self._search_entry.config(fg=TX_PRIMARY)

    def _search_focus_out(self, _):
        if not self._search_entry.get():
            self._search_entry.insert(0, "Search formulas...")
            self._search_entry.config(fg=TX_SECONDARY)

    def _on_search(self, *_):
        if not hasattr(self, "_list_inner"):
            return
        q = self._search_var.get()
        self._populate_list("" if q in ("", "Search formulas...") else q)

    def _populate_list(self, q=""):
        for w in self._list_inner.winfo_children():
            w.destroy()
        self._items.clear()
        for name in FORMULAS:
            if q and q.lower() not in name.lower():
                continue
            cat = FORMULA_CATEGORY.get(name, "General")
            cat_main, cat_lt = CATEGORIES.get(cat, ("#6B7280", "#F3F4F6"))
            eq = FORMULA_EQ.get(name, "")
            row = tk.Frame(self._list_inner, bg=WHITE, cursor="hand2")
            row.pack(fill=tk.X)
            bar = tk.Frame(row, bg=WHITE, width=self.s(3))
            bar.pack(side=tk.LEFT, fill=tk.Y)
            inner = tk.Frame(row, bg=WHITE)
            inner.pack(side=tk.LEFT, fill=tk.X, expand=True,
                       padx=(self.s(4), self.s(8)), pady=self.s(7))
            av = tk.Label(inner, text=cat[0], font=("Segoe UI", self.sf(11), "bold"),
                          bg=cat_lt, fg=cat_main, width=2, anchor=tk.CENTER)
            av.pack(side=tk.LEFT, padx=(self.s(2), self.s(10)))
            tf = tk.Frame(inner, bg=WHITE)
            tf.pack(side=tk.LEFT, fill=tk.X, expand=True)
            nl = tk.Label(tf, text=name, font=("Segoe UI", self.sf(9), "bold"),
                          bg=WHITE, fg=TX_PRIMARY, anchor=tk.W)
            nl.pack(anchor=tk.W)
            el = tk.Label(tf, text=eq, font=("Segoe UI", self.sf(8)),
                          bg=WHITE, fg=TX_SECONDARY, anchor=tk.W)
            el.pack(anchor=tk.W)
            bdg = tk.Label(inner, text=f"  {cat}  ", font=("Segoe UI", self.sf(7)),
                           bg=cat_lt, fg=cat_main)
            bdg.pack(side=tk.RIGHT, padx=self.s(4))
            tk.Frame(self._list_inner, bg=BORDER, height=1).pack(fill=tk.X, padx=self.s(12))
            recolor = [row, inner, tf, nl, el]
            self._items[name] = {"row": row, "bar": bar, "inner": inner,
                                  "tf": tf, "nl": nl, "el": el, "cat_main": cat_main}
            for w in recolor + [av, bdg]:
                w.bind("<Button-1>", lambda e, n=name: self._select(n))
            for w in recolor:
                w.bind("<Enter>",  lambda e, n=name: self._hover(n, True))
                w.bind("<Leave>",  lambda e, n=name: self._hover(n, False))
        self._list_canvas.configure(scrollregion=self._list_canvas.bbox("all"))

    def _hover(self, name, on):
        if name == self._selected:
            return
        info = self._items.get(name)
        if not info:
            return
        bg = HOV_BG if on else WHITE
        for key in ("row", "inner", "tf", "nl", "el"):
            try: info[key].config(bg=bg)
            except Exception: pass

    def _select(self, name):
        if self._selected and self._selected in self._items:
            old = self._items[self._selected]
            for key in ("row", "inner", "tf", "nl", "el"):
                try: old[key].config(bg=WHITE)
                except Exception: pass
            try: old["bar"].config(bg=WHITE)
            except Exception: pass
        self._selected = name
        info = self._items[name]
        for key in ("row", "inner", "tf", "nl", "el"):
            try: info[key].config(bg=SEL_BG)
            except Exception: pass
        try: info["bar"].config(bg=info["cat_main"])
        except Exception: pass
        self.current_formula = name
        self._update_content(name)

    def _build_content(self, parent):
        self._empty = tk.Frame(parent, bg=BG_CHAT)
        self._empty.place(relx=0, rely=0, relwidth=1, relheight=1)
        tk.Label(self._empty, text="\U0001f9ee", font=("Segoe UI Emoji", self.sf(44)),
                 bg=BG_CHAT, fg=TX_LIGHT).place(relx=0.5, rely=0.38, anchor=tk.CENTER)
        tk.Label(self._empty, text="Select a formula to get started",
                 font=("Segoe UI", self.sf(11)), bg=BG_CHAT, fg=TX_SECONDARY).place(
                     relx=0.5, rely=0.47, anchor=tk.CENTER)
        tk.Label(self._empty, text="Choose from 16 formulas in the left panel",
                 font=("Segoe UI", self.sf(9)), bg=BG_CHAT, fg=TX_LIGHT).place(
                     relx=0.5, rely=0.52, anchor=tk.CENTER)
        self._active = tk.Frame(parent, bg=BG_CHAT)

    def _update_content(self, name):
        self._empty.place_forget()
        self._active.place(relx=0, rely=0, relwidth=1, relheight=1)
        for w in self._active.winfo_children():
            w.destroy()
        self.input_fields = {}
        fd = FORMULAS[name]
        cat = FORMULA_CATEGORY.get(name, "General")
        cat_main, cat_lt = CATEGORIES.get(cat, ("#6B7280", "#F3F4F6"))
        eq = FORMULA_EQ.get(name, "")

        hdr = tk.Frame(self._active, bg=WHITE, height=self.s(58))
        hdr.pack(fill=tk.X)
        hdr.pack_propagate(False)
        tk.Frame(hdr, bg=cat_main, width=self.s(4)).pack(side=tk.LEFT, fill=tk.Y)
        av = tk.Label(hdr, text=name[0], font=("Segoe UI", self.sf(14), "bold"),
                      bg=cat_main, fg=TX_WHITE, width=2, anchor=tk.CENTER)
        av.pack(side=tk.LEFT, padx=self.s(12), pady=self.s(9))
        nf = tk.Frame(hdr, bg=WHITE)
        nf.pack(side=tk.LEFT, fill=tk.Y, pady=self.s(9))
        tk.Label(nf, text=name, font=("Segoe UI", self.sf(10), "bold"),
                 bg=WHITE, fg=TX_PRIMARY, anchor=tk.W).pack(anchor=tk.W)
        tk.Label(nf, text=eq, font=("Segoe UI", self.sf(8)),
                 bg=WHITE, fg=TX_SECONDARY, anchor=tk.W).pack(anchor=tk.W)
        tk.Label(hdr, text=f"  {cat}  ", font=("Segoe UI", self.sf(8)),
                 bg=cat_lt, fg=cat_main).pack(side=tk.RIGHT, padx=self.s(14), pady=self.s(18))
        tk.Frame(self._active, bg=BORDER, height=1).pack(fill=tk.X)

        body = tk.Frame(self._active, bg=BG_CHAT)
        body.pack(fill=tk.BOTH, expand=True)
        body_canvas = tk.Canvas(body, bg=BG_CHAT, highlightthickness=0)
        vsb = ttk.Scrollbar(body, orient="vertical", command=body_canvas.yview)
        inner = tk.Frame(body_canvas, bg=BG_CHAT)
        inner.bind("<Configure>", lambda e: body_canvas.configure(
            scrollregion=body_canvas.bbox("all")))
        body_canvas.create_window((0, 0), window=inner, anchor="nw")
        body_canvas.configure(yscrollcommand=vsb.set)
        body_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)

        def _scroll(e):
            body_canvas.yview_scroll(int(-1*(e.delta/120)), "units")
        body_canvas.bind("<MouseWheel>", _scroll)
        inner.bind("<MouseWheel>", _scroll)
        self._body_canvas = body_canvas

        self._add_recv_bubble(inner, fd["description"], "Formula")
        entry_list = []
        for param in fd["parameters"]:
            e = self._add_input_bubble(inner, param["name"], param["unit"])
            self.input_fields[param["name"]] = e
            entry_list.append(e)

        for i, e in enumerate(entry_list):
            def _tab(ev, idx=i, lst=entry_list):
                lst[(idx+1) % len(lst)].focus(); return "break"
            def _stab(ev, idx=i, lst=entry_list):
                lst[(idx-1) % len(lst)].focus(); return "break"
            e.bind("<Tab>",       _tab)
            e.bind("<Shift-Tab>", _stab)
            e.bind("<Return>",    lambda ev: self._calculate())
        if entry_list:
            entry_list[0].focus()

        self._result_container = tk.Frame(inner, bg=BG_CHAT)
        self._result_container.pack(fill=tk.X, padx=self.s(16), pady=(self.s(4), self.s(16)))

        tk.Frame(self._active, bg=BORDER, height=1).pack(fill=tk.X)
        bot = tk.Frame(self._active, bg=WHITE, height=self.s(62))
        bot.pack(fill=tk.X)
        bot.pack_propagate(False)
        hint = tk.Frame(bot, bg="#F0F2F5", highlightthickness=1, highlightbackground=BORDER)
        hint.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=self.s(14), pady=self.s(13))
        tk.Label(hint, text=f"Enter values for \u201c{name}\u201d then press Calculate",
                 font=("Segoe UI", self.sf(8)), bg="#F0F2F5", fg=TX_LIGHT,
                 padx=self.s(8), pady=self.s(6)).pack(side=tk.LEFT)
        tk.Button(bot, text="Clear", font=("Segoe UI", self.sf(9)),
                  bg=WHITE, fg=TX_SECONDARY, relief=tk.FLAT, bd=0, cursor="hand2",
                  padx=self.s(10), pady=self.s(7), command=self._clear,
                  activebackground=SEL_BG, activeforeground=BLUE).pack(
                      side=tk.RIGHT, padx=(0, self.s(4)), pady=self.s(13))
        tk.Button(bot, text="Calculate  \u2192", font=("Segoe UI", self.sf(9), "bold"),
                  bg=BLUE, fg=TX_WHITE, relief=tk.FLAT, bd=0, cursor="hand2",
                  padx=self.s(14), pady=self.s(8), command=self._calculate,
                  activebackground=BLUE_DARK, activeforeground=TX_WHITE).pack(
                      side=tk.RIGHT, padx=self.s(8), pady=self.s(13))

    def _add_recv_bubble(self, parent, text, label=""):
        row = tk.Frame(parent, bg=BG_CHAT)
        row.pack(fill=tk.X, padx=self.s(16), pady=(self.s(12), self.s(4)), anchor=tk.W)
        if label:
            tk.Label(row, text=label, font=("Segoe UI", self.sf(7)),
                     bg=BG_CHAT, fg=TX_LIGHT).pack(anchor=tk.W)
        bub = tk.Frame(row, bg=WHITE, highlightthickness=1, highlightbackground=BORDER)
        bub.pack(anchor=tk.W, ipadx=self.s(10), ipady=self.s(6))
        tk.Label(bub, text=text, font=("Segoe UI", self.sf(9)), bg=WHITE, fg=TX_PRIMARY,
                 wraplength=self.s(440), justify=tk.LEFT).pack()

    def _add_input_bubble(self, parent, param_name, unit):
        row = tk.Frame(parent, bg=BG_CHAT)
        row.pack(fill=tk.X, padx=self.s(16), pady=self.s(5), anchor=tk.W)
        row.bind("<MouseWheel>", lambda e: self._body_canvas.yview_scroll(
            int(-1*(e.delta/120)), "units"))
        tk.Label(row, text=f"{param_name}  ({unit})", font=("Segoe UI", self.sf(7)),
                 bg=BG_CHAT, fg=TX_LIGHT).pack(anchor=tk.W)
        bub = tk.Frame(row, bg=WHITE, highlightthickness=1, highlightbackground=BORDER)
        bub.pack(anchor=tk.W, ipadx=self.s(6), ipady=self.s(2))
        e = tk.Entry(bub, font=("Segoe UI", self.sf(10)), bg=WHITE, fg=TX_PRIMARY,
                     relief=tk.FLAT, bd=0, width=int(26 * max(1.0, self.dpi**0.5)),
                     insertbackground=TX_PRIMARY)
        e.pack(padx=self.s(10), pady=self.s(6))
        e.bind("<FocusIn>",  lambda ev, b=bub: b.config(highlightbackground=BLUE, highlightthickness=2))
        e.bind("<FocusOut>", lambda ev, b=bub: b.config(highlightbackground=BORDER, highlightthickness=1))
        e.bind("<MouseWheel>", lambda ev: self._body_canvas.yview_scroll(
            int(-1*(ev.delta/120)), "units"))
        return e

    def _calculate(self):
        if not self.current_formula:
            return
        name = self.current_formula
        values = {}
        try:
            for pname, entry in self.input_fields.items():
                v = entry.get().strip()
                if not v:
                    messagebox.showerror("Missing input",
                                         f"Please enter a value for \u2018{pname}\u2019")
                    return
                values[pname] = float(v)
        except ValueError:
            messagebox.showerror("Invalid input", "All values must be valid numbers")
            return
        try:
            result = calculate_formula(name, values)
        except Exception as ex:
            messagebox.showerror("Calculation Error", str(ex))
            return
        unit = FORMULAS[name].get("output_unit", "")
        display = f"{result:.6g}"
        if unit:
            display += f"  {unit}"
        for w in self._result_container.winfo_children():
            w.destroy()
        tk.Label(self._result_container, text="Result", font=("Segoe UI", self.sf(7)),
                 bg=BG_CHAT, fg=TX_LIGHT).pack(anchor=tk.E)
        bub = tk.Frame(self._result_container, bg=BLUE)
        bub.pack(anchor=tk.E, ipadx=self.s(16), ipady=self.s(10))
        tk.Label(bub, text=display, font=("Segoe UI", self.sf(14), "bold"),
                 bg=BLUE, fg=TX_WHITE).pack(padx=self.s(4))
        self._body_canvas.update_idletasks()
        self._body_canvas.yview_moveto(1.0)

    def _clear(self):
        for e in self.input_fields.values():
            e.delete(0, tk.END)
        if self._result_container:
            for w in self._result_container.winfo_children():
                w.destroy()
        if self.input_fields:
            next(iter(self.input_fields.values())).focus()


def main():
    root = tk.Tk()
    FormulaCalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
