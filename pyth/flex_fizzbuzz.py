from typing import List


class Zzer:
    def __init__(self) -> None:
        self.fizz_buzz_hash = {3: 'Fizz', 5: 'Buzz'}

    def fizzBuzz(self, n: int) -> List[str]:
        fb_arr: list[str] = []

        for i in range(1, n + 1):
            fb = ''

            for interval_key, zzer in self.fizz_buzz_hash.items():
                if (i % interval_key) == 0:
                    fb += zzer

            fb_arr.append(fb or str(i))

        return fb_arr

        pass
    
