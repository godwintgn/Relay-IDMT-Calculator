import re
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# from iec_trip.api import compute_trip_time
from idmt_tool.iec_trip.api import compute_trip_time

class IDMTTool(ttk.Window):

    def __init__(self):
        super().__init__(title="IEC Trip Time Calculator", themename="flatly")

        self.current_theme = "flatly"

        # Window config
        self.geometry("500x620")
        self.minsize(480, 580)
        self.resizable(True, True)

        # ==========================
        # TOP BAR
        # ==========================
        top = ttk.Frame(self, padding=(10, 10))
        top.pack(fill=X)

        title = ttk.Label(
            top,
            text="IEC Trip Time Calculator",
            font=("Segoe UI", 17, "bold")
        )
        title.pack(side=LEFT)

        self.theme_btn = ttk.Button(
            top,
            text="🌙",
            width=3,
            bootstyle=SECONDARY,
            command=self.toggle_theme,
        )
        self.theme_btn.pack(side=RIGHT)

        # ==========================
        # INPUT CARD
        # ==========================
        card = ttk.Labelframe(
            self,
            text="Inputs",
            padding=20,
            bootstyle="secondary",
        )
        card.pack(fill=X, padx=20, pady=10)

        ttk.Label(card, text="Trip curve", font=("Segoe UI", 11)).pack(anchor=W)

        curves = [
            "IEC Normal Inverse",
            "IEC Very Inverse",
            "IEC Extremely Inverse",
            "IEC Long Time Inverse",
        ]

        self.curve_var = ttk.StringVar(value=curves[0])
        self.curve_box = ttk.Combobox(
            card,
            textvariable=self.curve_var,
            values=curves,
            width=30,
            state="readonly",
        )
        self.curve_box.pack(fill=X, pady=(0, 12))

        # entries
        self.entry_pickup, self.frame_pickup = self._make_entry(
            card, "Relay pickup current (A)"
        )
        self.entry_fault, self.frame_fault = self._make_entry(
            card, "Fault current (A)"
        )
        self.entry_tms, self.frame_tms = self._make_entry(
            card, "Time Multiplier Setting (TMS)"
        )

        self.error_label = ttk.Label(card, text="", bootstyle="danger")
        self.error_label.pack(anchor=W)

        ttk.Button(
            card,
            text="Calculate",
            bootstyle=PRIMARY,
            command=self.calculate,
        ).pack(fill=X, pady=(12, 5))

        # ==========================
        # RESULT CARD
        # ==========================
        result = ttk.Labelframe(
            self,
            text="Results",
            padding=20,
            bootstyle="default",
        )
        result.pack(fill=X, padx=20, pady=10)

        self.result_label = ttk.Label(
            result,
            text="Trip time: ---",
            font=("Segoe UI", 13, "bold"),
        )
        self.result_label.pack(anchor=W)

        # ENTER = calculate
        self.bind("<Return>", lambda e: self.calculate())

    # ==========================
    # ENTRY BUILDER
    # ==========================
    def _make_entry(self, parent, label_text):
        ttk.Label(parent, text=label_text).pack(anchor=W)

        frame = ttk.Frame(parent)
        frame.pack(fill=X, pady=(0, 12))

        entry = ttk.Entry(frame, bootstyle="secondary")
        entry.pack(fill=X)

        # clear red on typing
        entry.bind("<KeyRelease>", lambda e, ent=entry: ent.configure(bootstyle="secondary"))

        return entry, frame

    # ==========================
    # NUMERIC PARSING
    # ==========================
    def parse_float(self, value: str):
        if not value.strip():
            return None

        cleaned = re.sub(r"[^0-9.\-]", "", value)
        try:
            return float(cleaned)
        except ValueError:
            return None

    # ==========================
    # ERROR DISPLAY
    # ==========================
    def _show_error(self, msg, entry=None, frame=None):
        self.error_label.config(text=msg)
        self.result_label.config(text="Trip time: ---")

        if entry:
            entry.configure(bootstyle="danger")

            # restore after flash
            def clear_style():
                entry.configure(bootstyle="secondary")

            entry.after(300, clear_style)
            entry.focus()

    # ==========================
    # SMART NUMBER FORMAT
    # ==========================
    def smart_format(self, n: float) -> str:
        if n is None:
            return "---"

        if abs(n) < 1e-3 or abs(n) >= 1e6:
            return f"{n:.4e}".replace("+", "")
        s = f"{n:.6f}".rstrip("0").rstrip(".")
        return s

    # ==========================
    # MAIN CALCULATION
    # ==========================
    def calculate(self):
        # reset all entries to normal style
        for entry in (self.entry_pickup, self.entry_fault, self.entry_tms):
            entry.configure(bootstyle="secondary")

        self.error_label.config(text="")
        self.result_label.config(text="Trip time: ---")

        pickup = self.parse_float(self.entry_pickup.get())
        fault = self.parse_float(self.entry_fault.get())
        tms = self.parse_float(self.entry_tms.get())

        if pickup is None or pickup <= 0:
            return self._show_error("Pickup must be a positive number.",
                                    self.entry_pickup)

        if fault is None or fault <= 0:
            return self._show_error("Fault current must be positive.",
                                    self.entry_fault)

        if tms is None or tms <= 0:
            return self._show_error("TMS must be positive.",
                                    self.entry_tms)

        curve = self.curve_var.get()
        t = compute_trip_time(curve, pickup, fault, tms)

        if t == float("inf"):
            self.result_label.config(text="Trip time: No trip (∞)")
        else:
            time_str = self.smart_format(t)
            self.result_label.config(text=f"Trip time: {time_str} s")

    # ==========================
    # THEME TOGGLE
    # ==========================
    def toggle_theme(self):
        if self.current_theme == "flatly":
            self.current_theme = "darkly"
            self.style.theme_use("darkly")
            self.theme_btn.config(text="☀️")
        else:
            self.current_theme = "flatly"
            self.style.theme_use("flatly")
            self.theme_btn.config(text="🌙")


def main():
    app = IDMTTool()
    app.mainloop()

if __name__ == "__main__":
    main()

