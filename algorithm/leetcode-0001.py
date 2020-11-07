from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int):
        # 枚举两个不同位置 i,k 的元素，值为 a,b
        for i, a in enumerate(nums):
            # 内部的循环，取 i 前面的部分切片再枚举，因此必然有 k < i
            for k, b in enumerate(nums[:i]):
                # 如果 a+b 等于 target 的话，直接返回位置 k, i
                if a+b == target:
                    return[k, i]


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([2, 7, 11, 15], 22), [1, 3]),
    ]

    solution = Solution()

    all_result = ''

    for case, (i, o) in enumerate(cases):
        print(f'#样例: {case+1}')
        print(f'输入: {repr(i)}')
        print(f'期望输出: {repr(o)}')
        try:
            result = solution.twoSum(*i)
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