def lotto_picks_util(nums, idx, remaining, seen):
    if idx >= len(nums):
        if remaining == 0:
            return [[]]
        else:
            return []
    elif remaining == 1 and idx == len(nums) - 1:
        if int(nums[idx]) > 0:
            return [[nums[idx]]]
        else:
            return []
    elif int(nums[idx]) == 0 or len(nums) - idx > 2 * remaining:
        return []

    picks = []
    for i in range(1, 3):
        if int(nums[idx:idx + i]) < 60 and nums[idx:idx + i] not in seen:
            seen.add(nums[idx:idx + i])
            for pick in lotto_picks_util(nums, idx + i, remaining - 1, seen):
                picks.append([nums[idx:idx + i]] + pick)
            seen.remove(nums[idx:idx + i])

    return picks


def print_lotto_picks(nums, ans):
    if not nums:
        print('{} ->'.format('None'))

    for num, picks in zip(nums, ans):
        result = ''
        for idx, pick in enumerate(picks):
            if idx > 0:
                result += ', '
            result += ' '.join(pick)
        print('{} -> {}'.format(num, result))

    print


def lotto_picks(nums):
    ans = []
    for num in nums:
        if not num.isdigit():
            ans.append([])
        else:
            seen = set()
            ans.append(lotto_picks_util(num, 0, 7, seen))

    return ans


if __name__ == "__main__":
    # Test empty input
    print_lotto_picks([], lotto_picks([]))

    # Test no picks for input
    print_lotto_picks(['123456789012345'], lotto_picks(['123456789012345']))

    # Test duplicate numbers in input
    print_lotto_picks(['1111111'], lotto_picks(['1111111']))

    # Test input took short for lotto_picks
    print_lotto_picks(['12345'], lotto_picks(['12345']))

    # Test invaliud input
    print_lotto_picks(['a1234567'], lotto_picks(['a1234567']))

    # Test one pick for input
    print_lotto_picks(['1234567'], lotto_picks(['1234567']))

    # Test multiple options for input
    print_lotto_picks(['15342615'], lotto_picks(['15342615']))

    # Test multiple inputs
    print_lotto_picks(
        ['1234567', '2345678'], lotto_picks(['1234567', '2345678']))

    # Test inputs given in question
    input = ['569815571556', '4938532894754', '1234567', '472844278465445']
    print_lotto_picks(input, lotto_picks(input))
