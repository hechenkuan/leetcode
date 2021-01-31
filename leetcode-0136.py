from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for x in nums:
            if x in s:
                s.remove(x)
            else:
                s.add(x)
        return s.pop()


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        (([2, 2, 1],), 1, lambda x:1),  # 1
        (([4,1,2,1,2],), 4, lambda x:1),  # 1
    ]

    solution = Solution()

    all_result = ''

    for case, (i, o, f) in enumerate(cases):
        print(f'#样例: {case+1}')
        print(f'输入: {repr(i)}')
        print(f'期望输出: {repr(o)}')
        try:
            result = solution.singleNumber(*i)
            correct = result == o and f(*i)
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
