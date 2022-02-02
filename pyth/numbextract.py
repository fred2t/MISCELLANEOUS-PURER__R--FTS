from typing import Any, Dict

D: Dict[int, Any] = {}

def f(num: int) -> str:
    for c in str(abs(num)):
        D[int(c)] = str(num).count(c)
    
    for key in sorted(D):
        print(f'{key} is found {D[key]} times')

    highest = max(D.values())
    return f"max is {[key for key in D if D[key] == highest]}"

print(f(1100))
