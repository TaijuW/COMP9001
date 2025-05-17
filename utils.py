def convert_position(pos):
    # Validate input format
    if len(pos) != 2:
        raise ValueError('Expected example: a1, b2, e3')
    
    try:
        # Convert letter to row number (a=0, b=1, etc.)
        row = ord(pos[0].lower()) - ord('a')
        # Convert number to column number (1=0, 2=1, etc.)
        col = int(pos[1]) - 1
    except ValueError:
        raise ValueError('Invalid place: Select from a1 to h8')
    
    return row, col