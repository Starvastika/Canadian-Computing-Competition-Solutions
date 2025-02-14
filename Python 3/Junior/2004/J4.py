def encode_message(keyword, message):
    filtered_message = ''.join([char for char in message if char.isalpha()])
    width = len(keyword)
    rows = [filtered_message[i:i + width] for i in range(0, len(filtered_message), width)]
    shifts = [ord(char) - ord('A') for char in keyword]
    encoded_message = ''
    for row in rows:
        for i, char in enumerate(row):
            shift = shifts[i]
            encoded_char = chr(((ord(char) - ord('A') + shift) % 26 + ord('A')))
            encoded_message += encoded_char
    return encoded_message
keyword = input().strip()
message = input().strip()
encoded_message = encode_message(keyword, message)
print(encoded_message)