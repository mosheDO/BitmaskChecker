# Bitmask Style Checker

This Python script helps users determine which constants are applied from a given bitmask. It supports multiple categories of constants (e.g., Window Styles, File Access Flags) and allows easy extensibility for future additions. The user can input a bitmask, select a category, and the script will display which constants are set based on the bitmask.

## Features
- Supports multiple constant categories like **Window Styles** and **File Access Flags**.
- Allows users to input **multiple bitmask values** (in hexadecimal or decimal format).
- Automatically processes each bitmask and displays the corresponding constants.
- **Easily extensible** to support new constant categories in the future (e.g., Process Flags, Thread Creation Flags).
- Provides **clear output** indicating which constants are applied for each bitmask.

## Usage

```

python window_style_checker.py


Enter the category (e.g., 'Window Styles', 'File Access Flags'): Window Styles
Enter bitmask numbers for Window Styles (hex or decimal, separated by commas): 0x00CF0000, 1342177280

Bitmask 0xcf0000: The following styles are applied:
- WS_OVERLAPPEDWINDOW
- WS_CAPTION
- WS_SYSMENU
- WS_THICKFRAME
- WS_MINIMIZEBOX
- WS_MAXIMIZEBOX

Bitmask 0x50000000: The following styles are applied:
- WS_CHILD
- WS_DISABLED
- WS_SYSMENU
- WS_THICKFRAME
- WS_TABSTOP
- WS_SIZEBOX
```
