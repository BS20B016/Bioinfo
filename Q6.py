def DNA_String_Search(sequence, strings_to_search):
    result = {}
    for string in strings_to_search:
        count = 0
        start_positions = []
        start = 0
        while start < len(sequence):
            pos = sequence.find(string, start)
            if pos == -1:
                break
            count += 1
            start_positions.append(pos)
            start = pos + 1
        result[string] = (count, start_positions)
    return result

sequence = "GACATTGTGAACAGTAAAAAAGTCCATGCAATGCGCAAGGAGCAGAAGAGGAAGCAGGGCAAGCAGCGCTCCATGGGCTCTCCCATGGACTACTCTCCTCTGCCCATCGACAAGCATGAGCCTGAATTTGGTCCATGCAGAAGAAAACTGGATGGG"
seq =input("Enter the String: ")
strings_to_search = [seq]

result = DNA_String_Search(sequence, strings_to_search)
for string, (count, start_positions) in result.items():
    print(f"String: {string}")
    print(f"Total matches: {count}")
    print(f"Start positions: {start_positions}")
    print()
