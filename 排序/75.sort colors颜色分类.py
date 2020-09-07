def sortColors(self, nums):
  red = 0
  white = 0
  blue = 0
  for num in nums:
    if num == 0:
      red += 1
    elif num == 1:
      white += 1
    else:
      blue += 1
    nums[:red] = [0] * red
    nums[red:red + white] = [1] * white
    nums[red + white:] = [2] * blue
    return nums



def sortColors(self, nums):
  left, cur, right = 0, 0, len(nums) - 1
  while cur <= right:
    if nums[cur] == 0:
      nums[cur], nums[left] = nums[left], nums[cur]
      left += 1
      cur += 1
    elif nums[cur] == 1:
      cur += 1
    else:
      nums[cur], nums[right] = nums[right], nums[cur]
      right -= 1