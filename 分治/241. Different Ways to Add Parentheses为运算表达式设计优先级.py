"""
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

示例 1:

输入: "2-1-1"
输出: [0, 2]
解释:
((2-1)-1) = 0
(2-(1-1)) = 2
示例 2:

输入: "2*3-4*5"
输出: [-34, -14, -10, -10, 10]
解释:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10


个大问题，我们可以根据运算符分成相应的六个小问题;第一个小问题是2，直接从字符串转成int返回，第二个小 问题是           ，又可以转化成四个小问题。这就是分而治之，分治思想。
我们常用来解决分治的方法是递归，递归需要注意递归推进和递归返回(或者叫做边界条件)。递归推进就是从大问 题转化为小问题，从“情况n”变化到情况“n+1"的过程，这里我们直接将运算符两侧的字符串分别作为一个子问题，压 入下一个递归即可。边界条件是当我们没有运算符的时候返回对应的整数，或者返回对应子问题的结果。需要注意， 当子问题返回了结果之后，需要根据对应的运算符，得到父问题的结果，再进行返回。
比如，       的结果得到了之后，我们要算 和       两个子问题返回结果相减后的结果再返回
"""

class Solution:
    def diffWaysToCompute(self, input: 'str') -> 'List[int]':
        return_list = []
        for i in range(len(input)):
            c = input[i]
            if c in ['+', '-', '*']:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        if c == '+':
                            return_list.append(l + r)
                        elif c == '-':
                            return_list.append(l - r)
                        elif c == '*':
                            return_list.append(l * r)
        if not return_list:
                            return_list.append(int(input))
        return return_list






class Solution:
  def diffWaysToCompute(self, input):
    signal = {
        '+': lambda x,y:x+y,
        '-': lambda x,y:x-y,
        '*': lambda x,y:x*y,
        #'/': lambda x,y:x/y,
    }
    def helper(input):
      res = []
      n = len(input)
      for i in range(n):
        if input[i] in signal:
          lefts = helper(input[:i])
          rights = helper(input[i+1:])
          for left in lefts:
            for right in rights:
              res.append(signal[input[i]](left, right))
      if not res:
        res.append(int(input))
      return res
    return helper(input)