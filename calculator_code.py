import tkinter as tk
import math


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("440x780")
root.resizable(False, False)


# ============================================================
# VARIABLES
# ============================================================

expr = ""
last_answer = 0
memory = 0
history = []

display = tk.StringVar()
time_result = tk.StringVar()


# ============================================================
# THEMES
# ============================================================

DARK = {
    "BG": "#202124",
    "NUMBER": "#3C4043",
    "OPERATOR": "#5F6368",
    "FUNCTION": "#F9AB00",
    "CLEAR": "#EA4335",
    "EQUAL": "#34A853",
    "MODE": "#303134",
    "TEXT": "white",
    "ENTRY_BG": "#F5F5F5",
    "ENTRY_FG": "#202124"
}

LIGHT = {
    "BG": "#F1F3F4",
    "NUMBER": "#DADCE0",
    "OPERATOR": "#BDC1C6",
    "FUNCTION": "#F9AB00",
    "CLEAR": "#EA4335",
    "EQUAL": "#34A853",
    "MODE": "#DADCE0",
    "TEXT": "#202124",
    "ENTRY_BG": "white",
    "ENTRY_FG": "#202124"
}

colors = DARK
dark_mode = True


# ============================================================
# FRAMES
# ============================================================

basic_frame = tk.Frame(root)
scientific_frame = tk.Frame(root)
finance_frame = tk.Frame(root)
time_frame = tk.Frame(root)


# ============================================================
# BASIC CALCULATOR
# ============================================================

def press(value):
    global expr

    expr += str(value)
    display.set(expr)


def clear():
    global expr

    expr = ""
    display.set("")


def backspace():
    global expr

    expr = expr[:-1]
    display.set(expr)


def equal():
    global expr, last_answer

    try:
        if not expr:
            return

        original = expr

        result = eval(
            expr,
            {"__builtins__": None},
            {}
        )

        result = round(result, 10)

        last_answer = result

        display.set(str(result))

        history.append(
            f"{original} = {result}"
        )

        expr = str(result)

        update_history()

    except ZeroDivisionError:
        display.set("Cannot divide by zero")
        expr = ""

    except:
        display.set("Invalid expression")
        expr = ""


# ============================================================
# ANS
# ============================================================

def use_answer():
    global expr

    expr += str(last_answer)
    display.set(expr)


# ============================================================
# MEMORY
# ============================================================

def memory_clear():
    global memory

    memory = 0


def memory_recall():
    global expr

    expr += str(memory)
    display.set(expr)


def memory_add():
    global memory

    try:
        memory += float(display.get())
    except:
        pass


def memory_subtract():
    global memory

    try:
        memory -= float(display.get())
    except:
        pass


# ============================================================
# MATH FUNCTIONS
# ============================================================

def square():
    global expr, last_answer

    try:
        original = expr

        result = round(float(expr) ** 2, 10)

        last_answer = result
        expr = str(result)

        display.set(str(result))

        history.append(
            f"{original}² = {result}"
        )

        update_history()

    except:
        display.set("Invalid input")


def square_root():
    global expr, last_answer

    try:
        original = expr

        value = float(expr)

        if value < 0:
            raise ValueError

        result = round(math.sqrt(value), 10)

        last_answer = result
        expr = str(result)

        display.set(str(result))

        history.append(
            f"√{original} = {result}"
        )

        update_history()

    except:
        display.set("Invalid input")


def percentage():
    global expr, last_answer

    try:
        original = expr

        result = round(float(expr) / 100, 10)

        last_answer = result
        expr = str(result)

        display.set(str(result))

        history.append(
            f"{original}% = {result}"
        )

        update_history()

    except:
        display.set("Invalid input")


def pi_value():
    global expr

    expr += str(math.pi)
    display.set(expr)


def reciprocal():
    global expr, last_answer

    try:
        original = expr

        value = float(expr)

        if value == 0:
            raise ZeroDivisionError

        result = round(1 / value, 10)

        last_answer = result
        expr = str(result)

        display.set(str(result))

        history.append(
            f"1/{original} = {result}"
        )

        update_history()

    except ZeroDivisionError:
        display.set("Cannot divide by zero")

    except:
        display.set("Invalid input")


def factorial():
    global expr, last_answer

    try:
        original = expr

        value = float(expr)

        if value < 0 or not value.is_integer():
            raise ValueError

        result = math.factorial(int(value))

        last_answer = result
        expr = str(result)

        display.set(str(result))

        history.append(
            f"{original}! = {result}"
        )

        update_history()

    except:
        display.set("Invalid factorial")


# ============================================================
# SCIENTIFIC
# ============================================================

def scientific_function(function, name):

    global expr, last_answer

    try:
        original = expr

        result = function(
            math.radians(float(expr))
        )

        result = round(result, 10)

        last_answer = result
        expr = str(result)

        display.set(str(result))

        history.append(
            f"{name}({original}) = {result}"
        )

        update_history()

    except:
        display.set("Invalid input")


def sci_sin():
    scientific_function(math.sin, "sin")


def sci_cos():
    scientific_function(math.cos, "cos")


def sci_tan():
    scientific_function(math.tan, "tan")


def sci_log():
    global expr, last_answer

    try:
        original = expr

        value = float(expr)

        if value <= 0:
            raise ValueError

        result = round(math.log10(value), 10)

        last_answer = result
        expr = str(result)

        display.set(str(result))

        history.append(
            f"log({original}) = {result}"
        )

        update_history()

    except:
        display.set("Invalid input")


def sci_ln():
    global expr, last_answer

    try:
        original = expr

        value = float(expr)

        if value <= 0:
            raise ValueError

        result = round(math.log(value), 10)

        last_answer = result
        expr = str(result)

        display.set(str(result))

        history.append(
            f"ln({original}) = {result}"
        )

        update_history()

    except:
        display.set("Invalid input")


# ============================================================
# FINANCE
# ============================================================

def calculate_si():

    try:
        p = float(principal_entry.get())
        r = float(rate_entry.get())
        t = float(finance_time_entry.get())

        if p < 0 or r < 0 or t < 0:
            raise ValueError

        si = (p * r * t) / 100
        amount = p + si

        si = round(si, 2)
        amount = round(amount, 2)

        display.set(
            f"SI = ₹{si}"
        )

        history.append(
            f"Simple Interest = ₹{si}"
        )

        update_history()

    except:
        display.set("Invalid finance input")


def calculate_ci():

    try:
        p = float(principal_entry.get())
        r = float(rate_entry.get())
        t = float(finance_time_entry.get())

        if p < 0 or r < 0 or t < 0:
            raise ValueError

        amount = p * (1 + r / 100) ** t
        ci = amount - p

        ci = round(ci, 2)
        amount = round(amount, 2)

        display.set(
            f"CI = ₹{ci}"
        )

        history.append(
            f"Compound Interest = ₹{ci}"
        )

        update_history()

    except:
        display.set("Invalid finance input")


def calculate_emi():

    try:
        principal = float(
            loan_entry.get()
        )

        annual_rate = float(
            loan_rate_entry.get()
        )

        months = int(
            loan_months_entry.get()
        )

        if principal <= 0 or annual_rate < 0 or months <= 0:
            raise ValueError

        monthly_rate = annual_rate / 12 / 100

        if monthly_rate == 0:

            emi = principal / months

        else:

            emi = (
                principal
                * monthly_rate
                * (1 + monthly_rate) ** months
                /
                ((1 + monthly_rate) ** months - 1)
            )

        emi = round(emi, 2)

        display.set(
            f"EMI = ₹{emi}"
        )

        history.append(
            f"EMI = ₹{emi}"
        )

        update_history()

    except:
        display.set("Invalid EMI input")


# ============================================================
# TIME CONVERTER
# ============================================================

def minutes_to_seconds():

    try:
        value = float(time_entry.get())

        seconds = value * 60

        result = (
            f"{value:g} minute(s) = "
            f"{seconds:g} seconds"
        )

        time_result.set(result)

        history.append(result)

        update_history()

    except:
        time_result.set("Enter valid minutes")


def hours_to_seconds():

    try:
        value = float(time_entry.get())

        seconds = value * 3600

        result = (
            f"{value:g} hour(s) = "
            f"{seconds:g} seconds"
        )

        time_result.set(result)

        history.append(result)

        update_history()

    except:
        time_result.set("Enter valid hours")


def time_to_seconds():

    try:

        value = time_entry.get().strip()

        if ":" in value:

            minutes, seconds = value.split(":")

            minutes = int(minutes)
            seconds = int(seconds)

            total = minutes * 60 + seconds

        else:

            total = float(value) * 60

        result = (
            f"{value} = "
            f"{total:g} seconds"
        )

        time_result.set(result)

        history.append(result)

        update_history()

    except:

        time_result.set(
            "Example: 2:30"
        )


def clear_time():

    time_entry.delete(
        0,
        tk.END
    )

    time_result.set("")


# ============================================================
# HISTORY
# ============================================================

def update_history():

    history_list.delete(
        0,
        tk.END
    )

    for item in reversed(history[-20:]):

        history_list.insert(
            tk.END,
            item
        )


def clear_history():

    history.clear()

    update_history()


def use_history(event=None):

    try:

        selected = history_list.curselection()

        if not selected:
            return

        value = history_list.get(
            selected[0]
        )

        display.set(value)

    except:
        pass


# ============================================================
# COPY
# ============================================================

def copy_result():

    value = display.get()

    if value:

        root.clipboard_clear()

        root.clipboard_append(value)

        root.update()

        copy_button.config(
            text="Copied!"
        )

        root.after(
            1200,
            lambda: copy_button.config(
                text="Copy"
            )
        )


# ============================================================
# MODE SWITCH
# ============================================================

def show_mode(frame):

    basic_frame.pack_forget()
    scientific_frame.pack_forget()
    finance_frame.pack_forget()
    time_frame.pack_forget()

    frame.pack(
        fill="both",
        expand=True,
        padx=18,
        pady=8
    )


def show_basic():
    show_mode(basic_frame)


def show_scientific():
    show_mode(scientific_frame)


def show_finance():
    show_mode(finance_frame)


def show_time():
    show_mode(time_frame)


# ============================================================
# THEME
# ============================================================

def change_theme():

    global dark_mode
    global colors

    dark_mode = not dark_mode

    if dark_mode:

        colors = DARK

        theme_button.config(
            text="☀ Light"
        )

    else:

        colors = LIGHT

        theme_button.config(
            text="☾ Dark"
        )

    apply_theme()


def apply_theme():

    root.configure(
        bg=colors["BG"]
    )

    for frame in [
        basic_frame,
        scientific_frame,
        finance_frame,
        time_frame,
        mode_frame,
        display_frame,
        extra_frame,
        history_frame
    ]:

        frame.configure(
            bg=colors["BG"]
        )

    display_entry.configure(
        bg=colors["ENTRY_BG"],
        fg=colors["ENTRY_FG"]
    )

    history_label.configure(
        bg=colors["BG"],
        fg=colors["TEXT"]
    )

    history_list.configure(
        bg=colors["ENTRY_BG"],
        fg=colors["ENTRY_FG"]
    )

    # Finance entries
    for entry in [
        principal_entry,
        rate_entry,
        finance_time_entry,
        loan_entry,
        loan_rate_entry,
        loan_months_entry,
        time_entry
    ]:

        entry.configure(
            bg=colors["ENTRY_BG"],
            fg=colors["ENTRY_FG"],
            insertbackground=colors["ENTRY_FG"]
        )


# ============================================================
# ABOUT
# ============================================================

def show_about():

    window = tk.Toplevel(root)

    window.title("About")
    window.geometry("390x350")

    window.configure(
        bg=colors["BG"]
    )

    tk.Label(
        window,
        text="Advanced Calculator",
        bg=colors["BG"],
        fg=colors["FUNCTION"],
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    description = (
        "A Python-based GUI calculator built "
        "using Tkinter.\n\n"
        "Features:\n"
        "• Basic calculations\n"
        "• Scientific calculations\n"
        "• Finance calculations\n"
        "• EMI calculator\n"
        "• Time converter\n"
        "• Calculation history\n"
        "• Memory functions\n"
        "• Keyboard support\n"
        "• Dark / Light mode\n"
        "• Copy result\n"
        "• Previous answer (Ans)"
    )

    tk.Label(
        window,
        text=description,
        bg=colors["BG"],
        fg=colors["TEXT"],
        font=("Arial", 10),
        justify="left"
    ).pack(padx=20)


# ============================================================
# HELP
# ============================================================

def show_help():

    window = tk.Toplevel(root)

    window.title("Help")
    window.geometry("400x420")

    window.configure(
        bg=colors["BG"]
    )

    tk.Label(
        window,
        text="How to Use",
        bg=colors["BG"],
        fg=colors["FUNCTION"],
        font=("Arial", 18, "bold")
    ).pack(pady=20)

    instructions = (
        "Keyboard:\n"
        "Enter → Calculate\n"
        "Backspace → Delete\n"
        "Escape → Clear\n\n"
        "Memory:\n"
        "MC → Memory Clear\n"
        "MR → Memory Recall\n"
        "M+ → Add to Memory\n"
        "M- → Subtract from Memory\n\n"
        "Ans → Use previous answer\n\n"
        "Scientific:\n"
        "sin, cos, tan, log, ln, √, x², xʸ\n\n"
        "Finance:\n"
        "Simple Interest, Compound Interest, EMI\n\n"
        "Time:\n"
        "2 = 2 minutes\n"
        "2:30 = 2 minutes 30 seconds"
    )

    tk.Label(
        window,
        text=instructions,
        bg=colors["BG"],
        fg=colors["TEXT"],
        font=("Arial", 10),
        justify="left"
    ).pack(
        padx=25
    )


# ============================================================
# MENU
# ============================================================

menubar = tk.Menu(root)

file_menu = tk.Menu(
    menubar,
    tearoff=0
)

file_menu.add_command(
    label="Clear",
    command=clear
)

file_menu.add_command(
    label="Clear History",
    command=clear_history
)

file_menu.add_separator()

file_menu.add_command(
    label="Exit",
    command=root.destroy
)

menubar.add_cascade(
    label="File",
    menu=file_menu
)


help_menu = tk.Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(
    label="How to Use",
    command=show_help
)

help_menu.add_command(
    label="About",
    command=show_about
)

menubar.add_cascade(
    label="Help",
    menu=help_menu
)

root.config(
    menu=menubar
)


# ============================================================
# MODE BUTTONS
# ============================================================

mode_frame = tk.Frame(
    root,
    bg=colors["BG"]
)

mode_frame.pack(
    fill="x",
    padx=18,
    pady=(10, 5)
)


def mode_button(text, command):

    return tk.Button(
        mode_frame,
        text=text,
        command=command,
        bg=colors["MODE"],
        fg=colors["TEXT"],
        font=("Arial", 9, "bold"),
        relief="flat",
        bd=0,
        height=2,
        cursor="hand2"
    )


basic_mode = mode_button(
    "BASIC",
    show_basic
)

basic_mode.pack(
    side="left",
    fill="x",
    expand=True,
    padx=2
)


scientific_mode = mode_button(
    "SCIENTIFIC",
    show_scientific
)

scientific_mode.pack(
    side="left",
    fill="x",
    expand=True,
    padx=2
)


finance_mode = mode_button(
    "FINANCE",
    show_finance
)

finance_mode.pack(
    side="left",
    fill="x",
    expand=True,
    padx=2
)


time_mode = mode_button(
    "TIME",
    show_time
)

time_mode.pack(
    side="left",
    fill="x",
    expand=True,
    padx=2
)


# ============================================================
# DISPLAY
# ============================================================

display_frame = tk.Frame(
    root,
    bg=colors["BG"]
)

display_frame.pack(
    fill="x",
    padx=18,
    pady=5
)


display_entry = tk.Entry(
    display_frame,
    textvariable=display,
    font=("Arial", 23, "bold"),
    justify="right",
    bg=colors["ENTRY_BG"],
    fg=colors["ENTRY_FG"],
    relief="flat",
    bd=0
)

display_entry.pack(
    fill="x",
    ipady=15
)


# ============================================================
# MEMORY / EXTRA
# ============================================================

extra_frame = tk.Frame(
    root,
    bg=colors["BG"]
)

extra_frame.pack(
    fill="x",
    padx=18,
    pady=3
)


def small_button(text, command):

    button = tk.Button(
        extra_frame,
        text=text,
        command=command,
        bg=colors["MODE"],
        fg=colors["TEXT"],
        font=("Arial", 8, "bold"),
        relief="flat",
        bd=0,
        cursor="hand2"
    )

    button.pack(
        side="left",
        padx=2,
        fill="x",
        expand=True
    )

    return button


small_button("MC", memory_clear)
small_button("MR", memory_recall)
small_button("M+", memory_add)
small_button("M-", memory_subtract)
small_button("Ans", use_answer)

theme_button = small_button(
    "☀ Light",
    change_theme
)

copy_button = small_button(
    "Copy",
    copy_result
)


# ============================================================
# BUTTON CREATOR
# ============================================================

def calculator_button(
    parent,
    text,
    command,
    row,
    column,
    bg=None,
    fg=None
):

    if bg is None:
        bg = colors["NUMBER"]

    if fg is None:
        fg = colors["TEXT"]

    button = tk.Button(
        parent,
        text=text,
        command=command,
        bg=bg,
        fg=fg,
        activebackground=bg,
        activeforeground=fg,
        font=("Arial", 10, "bold"),
        relief="flat",
        bd=0,
        height=2,
        cursor="hand2"
    )

    button.grid(
        row=row,
        column=column,
        padx=4,
        pady=4,
        sticky="nsew"
    )

    return button


# ============================================================
# BASIC
# ============================================================

for i in range(4):
    basic_frame.columnconfigure(
        i,
        weight=1
    )


basic_buttons = [

    ("1", lambda: press("1"), 0, 0, None),
    ("2", lambda: press("2"), 0, 1, None),
    ("3", lambda: press("3"), 0, 2, None),
    ("+", lambda: press("+"), 0, 3, colors["OPERATOR"]),

    ("4", lambda: press("4"), 1, 0, None),
    ("5", lambda: press("5"), 1, 1, None),
    ("6", lambda: press("6"), 1, 2, None),
    ("-", lambda: press("-"), 1, 3, colors["OPERATOR"]),

    ("7", lambda: press("7"), 2, 0, None),
    ("8", lambda: press("8"), 2, 1, None),
    ("9", lambda: press("9"), 2, 2, None),
    ("×", lambda: press("*"), 2, 3, colors["OPERATOR"]),

    ("0", lambda: press("0"), 3, 0, None),
    (".", lambda: press("."), 3, 1, None),
    ("=", equal, 3, 2, colors["EQUAL"]),
    ("÷", lambda: press("/"), 3, 3, colors["OPERATOR"]),

    ("AC", clear, 4, 0, colors["CLEAR"]),
    ("⌫", backspace, 4, 1, colors["FUNCTION"]),
    ("%", percentage, 4, 2, colors["FUNCTION"]),
    ("x²", square, 4, 3, colors["FUNCTION"]),

    ("π", pi_value, 5, 0, colors["FUNCTION"]),
    ("√", square_root, 5, 1, colors["FUNCTION"]),
    ("xʸ", lambda: press("**"), 5, 2, colors["FUNCTION"]),
    ("(", lambda: press("("), 5, 3, colors["FUNCTION"]),

    (")", lambda: press(")"), 6, 0, colors["FUNCTION"])
]


for text, command, row, col, bg in basic_buttons:

    calculator_button(
        basic_frame,
        text,
        command,
        row,
        col,
        bg,
        "black" if bg == colors["FUNCTION"] else None
    )


# ============================================================
# SCIENTIFIC
# ============================================================

for i in range(4):
    scientific_frame.columnconfigure(
        i,
        weight=1
    )


scientific_buttons = [

    ("sin", sci_sin, 0, 0, colors["OPERATOR"]),
    ("cos", sci_cos, 0, 1, colors["OPERATOR"]),
    ("tan", sci_tan, 0, 2, colors["OPERATOR"]),
    ("log", sci_log, 0, 3, colors["OPERATOR"]),

    ("ln", sci_ln, 1, 0, colors["OPERATOR"]),
    ("√", square_root, 1, 1, colors["FUNCTION"]),
    ("x²", square, 1, 2, colors["FUNCTION"]),
    ("xʸ", lambda: press("**"), 1, 3, colors["FUNCTION"]),

    ("π", pi_value, 2, 0, colors["FUNCTION"]),
    ("1/x", reciprocal, 2, 1, colors["FUNCTION"]),
    ("n!", factorial, 2, 2, colors["FUNCTION"]),
    ("⌫", backspace, 2, 3, colors["FUNCTION"]),

    ("7", lambda: press("7"), 3, 0, None),
    ("8", lambda: press("8"), 3, 1, None),
    ("9", lambda: press("9"), 3, 2, None),
    ("÷", lambda: press("/"), 3, 3, colors["OPERATOR"]),

    ("4", lambda: press("4"), 4, 0, None),
    ("5", lambda: press("5"), 4, 1, None),
    ("6", lambda: press("6"), 4, 2, None),
    ("×", lambda: press("*"), 4, 3, colors["OPERATOR"]),

    ("1", lambda: press("1"), 5, 0, None),
    ("2", lambda: press("2"), 5, 1, None),
    ("3", lambda: press("3"), 5, 2, None),
    ("-", lambda: press("-"), 5, 3, colors["OPERATOR"]),

    ("0", lambda: press("0"), 6, 0, None),
    (".", lambda: press("."), 6, 1, None),
    ("AC", clear, 6, 2, colors["CLEAR"]),
    ("+", lambda: press("+"), 6, 3, colors["OPERATOR"]),

    ("(", lambda: press("("), 7, 0, colors["FUNCTION"]),
    (")", lambda: press(")"), 7, 1, colors["FUNCTION"]),
    ("=", equal, 7, 2, colors["EQUAL"])
]


for text, command, row, col, bg in scientific_buttons:

    calculator_button(
        scientific_frame,
        text,
        command,
        row,
        col,
        bg,
        "black" if bg == colors["FUNCTION"] else None
    )


# ============================================================
# FINANCE
# ============================================================

finance_frame.columnconfigure(
    1,
    weight=1
)


finance_title = tk.Label(
    finance_frame,
    text="Finance Calculator",
    bg=colors["BG"],
    fg=colors["FUNCTION"],
    font=("Arial", 17, "bold")
)

finance_title.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=8
)


def finance_input(label, row):

    tk.Label(
        finance_frame,
        text=label,
        bg=colors["BG"],
        fg=colors["TEXT"],
        font=("Arial", 10, "bold")
    ).grid(
        row=row,
        column=0,
        sticky="w",
        padx=8,
        pady=5
    )

    entry = tk.Entry(
        finance_frame,
        bg=colors["ENTRY_BG"],
        fg=colors["ENTRY_FG"],
        insertbackground=colors["ENTRY_FG"],
        relief="flat",
        bd=1,
        font=("Arial", 11)
    )

    entry.grid(
        row=row,
        column=1,
        padx=8,
        pady=5,
        ipady=5,
        sticky="ew"
    )

    return entry


# SIMPLE / COMPOUND INTEREST INPUTS

principal_entry = finance_input(
    "Principal:",
    1
)

rate_entry = finance_input(
    "Rate (%):",
    2
)

finance_time_entry = finance_input(
    "Time (years):",
    3
)


tk.Button(
    finance_frame,
    text="Simple Interest",
    command=calculate_si,
    bg=colors["EQUAL"],
    fg="white",
    relief="flat",
    height=2,
    cursor="hand2"
).grid(
    row=4,
    column=0,
    columnspan=2,
    sticky="ew",
    padx=8,
    pady=4
)


tk.Button(
    finance_frame,
    text="Compound Interest",
    command=calculate_ci,
    bg=colors["FUNCTION"],
    fg="black",
    relief="flat",
    height=2,
    cursor="hand2"
).grid(
    row=5,
    column=0,
    columnspan=2,
    sticky="ew",
    padx=8,
    pady=4
)


# EMI

emi_title = tk.Label(
    finance_frame,
    text="Loan EMI",
    bg=colors["BG"],
    fg=colors["FUNCTION"],
    font=("Arial", 14, "bold")
)

emi_title.grid(
    row=6,
    column=0,
    columnspan=2,
    pady=7
)


loan_entry = finance_input(
    "Loan Amount:",
    7
)

loan_rate_entry = finance_input(
    "Annual Rate (%):",
    8
)

loan_months_entry = finance_input(
    "Months:",
    9
)


tk.Button(
    finance_frame,
    text="Calculate EMI",
    command=calculate_emi,
    bg=colors["EQUAL"],
    fg="white",
    relief="flat",
    height=2,
    cursor="hand2"
).grid(
    row=10,
    column=0,
    columnspan=2,
    sticky="ew",
    padx=8,
    pady=5
)


# ============================================================
# TIME
# ============================================================

time_title = tk.Label(
    time_frame,
    text="Time Converter",
    bg=colors["BG"],
    fg=colors["FUNCTION"],
    font=("Arial", 18, "bold")
)

time_title.pack(
    pady=15
)


time_entry = tk.Entry(
    time_frame,
    font=("Arial", 16),
    bg=colors["ENTRY_BG"],
    fg=colors["ENTRY_FG"],
    insertbackground=colors["ENTRY_FG"],
    justify="center",
    relief="flat"
)

time_entry.pack(
    fill="x",
    padx=35,
    ipady=10
)


tk.Label(
    time_frame,
    text="Examples: 2 or 2:30",
    bg=colors["BG"],
    fg="#888888"
).pack(
    pady=8
)


tk.Button(
    time_frame,
    text="Minutes → Seconds",
    command=minutes_to_seconds,
    bg=colors["EQUAL"],
    fg="white",
    relief="flat",
    height=2
).pack(
    fill="x",
    padx=35,
    pady=5
)


tk.Button(
    time_frame,
    text="Hours → Seconds",
    command=hours_to_seconds,
    bg=colors["OPERATOR"],
    fg="white",
    relief="flat",
    height=2
).pack(
    fill="x",
    padx=35,
    pady=5
)


tk.Button(
    time_frame,
    text="Convert Time",
    command=time_to_seconds,
    bg=colors["FUNCTION"],
    fg="black",
    relief="flat",
    height=2
).pack(
    fill="x",
    padx=35,
    pady=5
)


tk.Button(
    time_frame,
    text="Clear",
    command=clear_time,
    bg=colors["CLEAR"],
    fg="white",
    relief="flat",
    height=2
).pack(
    fill="x",
    padx=35,
    pady=5
)


tk.Label(
    time_frame,
    textvariable=time_result,
    bg=colors["BG"],
    fg=colors["TEXT"],
    font=("Arial", 12, "bold")
).pack(
    pady=15
)


# ============================================================
# HISTORY
# ============================================================

history_frame = tk.Frame(
    root,
    bg=colors["BG"]
)

history_frame.pack(
    fill="both",
    padx=18,
    pady=(3, 8)
)


history_label = tk.Label(
    history_frame,
    text="History",
    bg=colors["BG"],
    fg=colors["TEXT"],
    font=("Arial", 10, "bold")
)

history_label.pack(
    anchor="w"
)


history_list = tk.Listbox(
    history_frame,
    height=3,
    bg=colors["ENTRY_BG"],
    fg=colors["ENTRY_FG"],
    font=("Arial", 9),
    relief="flat"
)

history_list.pack(
    fill="both",
    pady=3
)


history_list.bind(
    "<Double-Button-1>",
    use_history
)


# ============================================================
# KEYBOARD SUPPORT
# ============================================================

def keyboard_press(event):

    if event.keysym == "Return":

        equal()

    elif event.keysym == "BackSpace":

        backspace()

    elif event.keysym == "Escape":

        clear()

    elif event.char in "0123456789+-*/().":

        press(event.char)


root.bind(
    "<Key>",
    keyboard_press
)


# ============================================================
# START
# ============================================================

show_basic()

root.mainloop()