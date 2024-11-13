# Define the constants for window styles and other future types (like file access flags)
WINDOW_STYLES = {
    "WS_BORDER": 0x00800000,
    "WS_CAPTION": 0x00C00000,
    "WS_CHILD": 0x40000000,
    "WS_CHILDWINDOW": 0x40000000,
    "WS_CLIPCHILDREN": 0x02000000,
    "WS_CLIPSIBLINGS": 0x04000000,
    "WS_DISABLED": 0x08000000,
    "WS_DLGFRAME": 0x00400000,
    "WS_GROUP": 0x00020000,
    "WS_HSCROLL": 0x00100000,
    "WS_ICONIC": 0x20000000,
    "WS_MAXIMIZE": 0x01000000,
    "WS_MAXIMIZEBOX": 0x00010000,
    "WS_MINIMIZE": 0x20000000,
    "WS_MINIMIZEBOX": 0x00020000,
    "WS_OVERLAPPED": 0x00000000,
    "WS_OVERLAPPEDWINDOW": 0x00CF0000,
    "WS_POPUP": 0x80000000,
    "WS_POPUPWINDOW": 0x80080000,
    "WS_SIZEBOX": 0x00040000,
    "WS_SYSMENU": 0x00080000,
    "WS_TABSTOP": 0x00010000,
    "WS_THICKFRAME": 0x00040000,
    "WS_TILED": 0x00000000,
    "WS_TILEDWINDOW": 0x00CF0000,
    "WS_VISIBLE": 0x10000000,
    "WS_VSCROLL": 0x00200000
}

# Example: File Access Flags (to support in the future)
FILE_ACCESS_FLAGS = {
    "GENERIC_READ": 0x80000000,
    "GENERIC_WRITE": 0x40000000,
    "OPEN_EXISTING": 0x00000003,
    "CREATE_NEW": 0x00000001,
    "FILE_SHARE_READ": 0x00000001,
    "FILE_SHARE_WRITE": 0x00000002,
    "FILE_FLAG_OVERLAPPED": 0x40000000
}

# More categories of constants can be added in the future in a similar way.

# Dictionary to store all types of constants (can easily be extended)
CONSTANT_CATEGORIES = {
    "Window Styles": WINDOW_STYLES,
    "File Access Flags": FILE_ACCESS_FLAGS
}

def get_styles(bitmask, styles_dict):
    """
    Given a bitmask, find out which styles are set by performing bitwise AND with known style constants.
    Returns a list of the names of applied styles.
    """
    applied_styles = []
    for style_name, style_value in styles_dict.items():
        if bitmask & style_value:
            applied_styles.append(style_name)
    return applied_styles

def process_bitmasks(bitmasks, styles_dict):
    """
    Given a list of bitmasks, process each one and display the corresponding styles for the specified category.
    """
    for bitmask in bitmasks:
        applied_styles = get_styles(bitmask, styles_dict)
        if applied_styles:
            print(f"\nBitmask {hex(bitmask)}: The following styles are applied:")
            for style in applied_styles:
                print(f"- {style}")
        else:
            print(f"\nBitmask {hex(bitmask)}: No styles are applied.")

def main():
    print("Bitmask Style Checker")
    
    # Display available categories
    print("\nAvailable categories:")
    for category in CONSTANT_CATEGORIES.keys():
        print(f"- {category}")
    
    # Get the category from the user
    category = input("\nEnter the category (e.g., 'Window Styles', 'File Access Flags'): ").strip()
    
    if category not in CONSTANT_CATEGORIES:
        print("Invalid category. Please enter a valid category from the available list.")
        return
    
    # Get the bitmask values from the user, allowing multiple bitmasks separated by commas
    user_input = input(f"Enter bitmask numbers for {category} (hex or decimal, separated by commas): ")
    
    # Process the input and convert to a list of integers
    try:
        # Split input by commas, strip whitespace, and convert each to an integer (allowing hex and decimal formats)
        bitmasks = [int(b.strip(), 0) for b in user_input.split(',')]
    except ValueError:
        print("Invalid input. Please enter valid bitmask numbers.")
        return
    
    # Process each bitmask and display the applied styles from the selected category
    process_bitmasks(bitmasks, CONSTANT_CATEGORIES[category])

if __name__ == "__main__":
    main()
