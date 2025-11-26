# IDMT Trip Time Calculator

A simple, modern tool for calculating IEC IDMT relay trip times.  
Supports the standard IEC inverse-time curves and provides a clean GUI for quick engineering use.

## Features

- IEC Normal Inverse (NI)
- IEC Very Inverse (VI)
- IEC Extremely Inverse (EI)
- IEC Long Time Inverse (LTI)
- Relay pickup, fault current, and TMS inputs
- Clean, modern GUI (ttkbootstrap)
- Light and dark mode toggle
- Smart numeric input handling
- Instant trip time calculation
- Works on Windows, macOS, and Linux

## How to Use

1. Select the IEC curve.
2. Enter:
   - Relay pickup current (A)
   - Fault current (A)
   - Time Multiplier Setting (TMS)
3. Press **Calculate**.
4. Trip time will be displayed.

## Running the App (development)

```bash
python -m idmt_tool.gui.main
