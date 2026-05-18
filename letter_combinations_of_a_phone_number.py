#Brute Force
def letterCombinations(digits):
    if not digits:
        return []

    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno',
        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = ['']
    for digit in digits:
        temp = []
        for comb in result:
            for i in phone[digit]:
                temp.append(comb +i)
        result = temp
    return result
