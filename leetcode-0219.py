from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        s = set()
        for i, x in enumerate(nums):
            if x in s:
                return True
            if i >= k:
                s.remove(nums[i-k])
            s.add(x)
        return False

    def containsNearbyDuplicateTLE(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n-1):
            for j in range(k):
                if i+1+j > n-1:
                    break
                if nums[i] == nums[i+1+j]:
                    return True
        return False


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        (([1, 2, 3, 1], 3), True),  # 1
        (([1, 0, 1, 1], 1), True),  # 2
        (([1, 2, 3, 1, 2, 3], 2), False),  # 3
    ]

    solution = Solution()

    all_result = ''

    for case, (i, o) in enumerate(cases):
        print(f'#样例: {case+1}')
        print(f'输入: {repr(i)}')
        print(f'期望输出: {repr(o)}')
        try:
            result = solution.containsNearbyDuplicate(*i)
            correct = result == o
        except Exception as e:
            import traceback
            traceback.print_exc()
            correct = False
        all_result += '.' if correct else 'x'
        print(f'我的输出: {repr(result)}')
        print('结果: ' + ('正确' if correct else '错误'))
        print()

    print('测试结果:', all_result)
    yes_count = sum([1 if x == '.' else 0 for x in all_result])
    no_count = sum([1 if x == 'x' else 0 for x in all_result])
    print(
        f'共测试 {len(all_result)} 个样例，'
        f'成功 {yes_count} 个，'
        f'失败 {no_count} 个'
    )
    if 'x' in all_result:
        print('测试失败，请检查你的代码！')
    else:
        print('测试通过，所有的测试数据均返回了正确的答案！')
