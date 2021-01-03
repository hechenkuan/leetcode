from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        m = 0
        for i in range(n):
            # 如果nums[i]是新出现的数字
            if nums[i] != 0 :
                nums[m],nums[i] = nums[i],nums[m]
                m += 1


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        (([0, 1, 0, 3, 12],), None, lambda x:x == [1, 3, 12, 0, 0]),  # 1
    ]

    solution = Solution()

    all_result = ''

    for case, (i, o, f) in enumerate(cases):
        print(f'#样例: {case+1}')
        print(f'输入: {repr(i)}')
        print(f'期望输出: {repr(o)}')
        try:
            result = solution.moveZeroes(*i)
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
