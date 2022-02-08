def numxtract(number: int) -> str:
    appearances: dict[str, int] = {}
    
    for num in str(abs(number)):
        appearances[num] = str(number).count(num)
    
    for key in sorted(appearances):
        print(f'{key} is found {appearances[key]} times')

    highest = max(appearances.values())
    return f"max is/are {', '.join(sorted(key for key in appearances if appearances[key] == highest))}"

# print(numxtract(-3331100))
print(numxtract(45667799))
