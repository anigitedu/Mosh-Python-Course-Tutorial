numbers={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}
i=input("Phone:")

for ch in i:
    if ch in numbers:
        print(numbers[ch])
    else:
        print(ch)
            

