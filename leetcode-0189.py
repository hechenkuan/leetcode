from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n 
        if k == 0:
            return 
        for i in range(n//2):
            nums[i],nums[n-1-i]=nums[n-1-i],nums[i]
        for i in range(k//2):
            nums[i],nums[k-1-i]=nums[k-1-i],nums[i]
        for i in range((n-k)//2):
            nums[i+k],nums[n-1-i]=nums[n-1-i],nums[i+k]

            


    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for j in range(k):
            a = nums[-1]
            for i in range(n-1, 0, -1):
                nums[i] = nums[i-1]
            nums[0] = a


if __name__ == "__main__":
    """测试代码
    """

    cases = [
        (([1, 2, 3, 4, 5, 6, 7], 3), None, lambda x,
        k:x == [5, 6, 7, 1, 2, 3, 4]),  # 1
        (([1, 2, 3, 4, 5, 6, 7,13,23,2,42,43324,432,32,6,7,855,32,4,43,6,473], 2), None, lambda x,
        k:x == [6,473,1, 2, 3, 4, 5, 6, 7,13,23,2,42,43324,432,32,6,7,855,32,4,43,]),  # 1
    ]

    solution = Solution()

    all_result = ''

    for case, (i, o, f) in enumerate(cases):
        print(f'#样例: {case+1}')
        print(f'输入: {repr(i)}')
        print(f'期望输出: {repr(o)}')
        try:
            result = solution.rotate(*i)
            correct = result == o and f(*i)
        except Exception as e:
            import traceback
            traceback.print_exc()
            correct = False
        all_result += '.' if correct else 'x'
        print(f'我的输出: {repr(i[0])}')
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
