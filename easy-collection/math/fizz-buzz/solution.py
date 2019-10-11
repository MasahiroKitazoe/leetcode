class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []
        for num in range(1, n+1):
            if num % 15 == 0:
                ret.append("FizzBuzz")
            elif num % 3 == 0:
                ret.append("Fizz")
            elif num % 5 == 0:
                ret.append("Buzz")
            else:
                ret.append(str(num))
        return ret

