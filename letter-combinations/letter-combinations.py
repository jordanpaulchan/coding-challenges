DICT = {
    '1': 'ab',
    '2': 'de',
    '12': 'gh'
}


def get_words(nums):
    if not nums:
        return ['']

    ans = []
    for i in range(1, len(nums) + 1):
        words = get_words(nums[i:])
        if nums[:i] in DICT:
            for char in DICT[nums[:i]]:
                for item in words:
                    ans.append(char + item)

    return ans


print(get_words('12'))
print(get_words('221'))
print(get_words('1'))
print(get_words('2212'))
