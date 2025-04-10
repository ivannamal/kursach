def read_and_filter_printable_chars(file_path):
    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        # Skip the first 228 bytes
        file.seek(228)

        # Read the rest of the file content
        file_content = file.read()

        # Initialize an empty list to hold printable characters
        printable_chars = []

        # Loop through each byte in the file content (excluding the last byte to avoid out-of-range error)
        for i in range(len(file_content) - 1):
            byte = file_content[i]
            next_byte = file_content[i + 1]

            # If the byte is printable (ASCII 32-126), add it to the list
            if 32 <= byte <= 126:
                printable_chars.append(chr(byte))

                # Check if the next byte is not printable (ASCII less than 32 or greater than 126)
                if not (32 <= next_byte <= 126):
                    printable_chars.append('\n')  # Add newline after the printable character

        # Check the last byte separately (bc i didn't include it in the loop above)
        last_byte = file_content[-1]
        if 32 <= last_byte <= 126:
            printable_chars.append(chr(last_byte))

        # Join the list of printable characters into a string and return
        return ''.join(printable_chars)


# Example usage
file_path = 'chapters_spanish.landb'  # Replace with the path to your file
result = read_and_filter_printable_chars(file_path)
print(result)
