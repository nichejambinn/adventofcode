
def detect_start_of_message_marker(datastream):
    return detect_start_of_packet_marker(datastream, sequence_length=14)

def detect_start_of_packet_marker(datastream, sequence_length=4):
    for i in range(len(datastream) - sequence_length):
        if all_chars_different(datastream[i:i+sequence_length]):
            return i + sequence_length

    return False

def all_chars_different(s):
    return len(set(s)) == len(s)


if __name__=='__main__':
    with open('puzzle6', 'r') as file:
        datastream = file.readlines()[0]
        print(detect_start_of_packet_marker(datastream)) # part 1
        print(detect_start_of_message_marker(datastream)) # part 2
        