def decode_message(s):
    decoded_message = ""
    
    for i in range(0, len(s), 2):
        lowercase_pos = ord(s[i]) - ord('a') + 1
        uppercase_pos = ord(s[i + 1]) - ord('A') + 1
        decoded_char = chr((lowercase_pos + uppercase_pos - 1) % 26 + ord('a'))
        decoded_message += decoded_char
    
    return decoded_message

encoded_string = "[string]"
hidden_message = decode_message(encoded_string)
print("Decoded Message:", hidden_message)
