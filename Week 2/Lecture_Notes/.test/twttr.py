def main():
    ls = vovel_list()
    str = input("Input: ")
    output_str = ""

    for c in str:
        if c in ls:
            continue
        output_str += c

    print("Output:",output_str)

def vovel_list():
    word = ['a','e','i','o','u']
    upper = []

    for char in word:
            upper += char.upper()

    return word

main()
