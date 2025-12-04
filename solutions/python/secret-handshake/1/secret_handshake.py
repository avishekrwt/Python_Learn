def commands(binary_str):
    actions = ['wink','double blink','close your eyes','jump']
    binary_str = binary_str[::-1]
    decoded_msg = []
    for i in range(4):
        if binary_str[i] == '1' :
            decoded_msg.append(actions[i])
    if binary_str[4] == '1':
        decoded_msg.reverse()

    return decoded_msg