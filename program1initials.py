def display_initials(name):
    # Split the name into parts
    parts = name.split()
    # Extract and capitalize initials
    initials = [part[0].upper() + '.' for part in parts]
    # Join and display the initials
    print(' '.join(initials))
    