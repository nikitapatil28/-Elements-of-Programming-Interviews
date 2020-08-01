def numberToWords( num):
    if num <= 0: return "Zero"
    places = {1000000000: "Billion", 1000000: "Million", 1000: "Thousand", 100: "Hundred"}
    TenPlaces = {90: "Ninety",
                 80: "Eighty", 70: "Seventy", 60: "Sixty", 50: "Fifty", 40: "Forty", 30: "Thirty", 20: "Twenty", }
    numbers = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
               10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
               17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}

    result = ""

    def toWord(n):

        if n < 100 and n >= 20:
            res = ""
            for key in TenPlaces:
                if n // key > 0:
                    res += TenPlaces[key]
                    n = n % key
                    break
            return res + " " + numbers[n] if n > 0 else res
        elif n < 20:
            return numbers[n]

        res = ""
        while n:
            if n >= 100:
                for key in places:
                    if n // key > 0:
                        if res == "":
                            res += toWord(n // key) + " " + places[key]
                        else:
                            res += " " + toWord(n // key) + " " + places[key]
                        n %= key
                        break
            else:
                return res + " " + toWord(n)
        return res

    return toWord(num)
print(numberToWords(123))
print(numberToWords(1234567))