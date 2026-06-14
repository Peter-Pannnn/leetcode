# LeetCode 解题思路分类汇总

本文按当前文件夹分类整理常见解题套路：

- `hashmap`：哈希表、集合、计数、分组
- `2_pointers`：双指针、对撞指针、快慢指针
- `sliding_win`：滑动窗口
- `substring`：前缀和与子数组统计
- `array`：数组基础、区间、原地操作、动态规划

## 一、哈希表 hashmap

哈希表适合解决：

- 快速判断一个元素是否出现过
- 记录元素对应下标
- 统计出现次数
- 按某个 key 分组
- 去重后再查找

常用结构：

```python
mp = {}       # key -> value
st = set()   # 只判断存在性
```

### 1. 两数之和：`hashmap/1.py`

题目特点：

给定 `nums` 和 `target`，找两个数的下标，使它们的和等于 `target`。

核心思路：

遍历数组时，假设当前数是 `num`，那么另一个数应该是：

```python
need = target - num
```

如果 `need` 已经在哈希表里，说明找到了答案。否则把当前数和下标存入哈希表。

关键点：

```python
seen[num] = i
```

要放在检查之后，避免同一个元素被使用两次。

模板：

```python
seen = {}

for i, num in enumerate(nums):
    need = target - num
    if need in seen:
        return [seen[need], i]
    seen[num] = i
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(n)
```

### 2. 字母异位词分组：`hashmap/49.py`

题目特点：

把互为字母异位词的字符串分到同一组。

核心思路：

字母异位词排序后结果相同。

例如：

```text
"eat" -> "aet"
"tea" -> "aet"
"ate" -> "aet"
```

所以可以用排序后的字符串作为 key。

模板：

```python
groups = {}

for word in strs:
    key = "".join(sorted(word))
    if key not in groups:
        groups[key] = []
    groups[key].append(word)

return list(groups.values())
```

更优方向：

如果字符串只包含小写字母，可以用长度为 `26` 的计数数组作为 key：

```python
count = [0] * 26
for c in word:
    count[ord(c) - ord("a")] += 1
key = tuple(count)
```

复杂度：

```text
排序 key：O(n * k log k)
计数 key：O(n * k)
空间复杂度：O(n * k)
```

其中 `n` 是字符串数量，`k` 是字符串平均长度。

### 3. 最长连续序列：`hashmap/128.py`

题目特点：

数组未排序，找最长连续数字序列长度，要求 `O(n)`。

核心思路：

先把所有数字放进集合：

```python
num_set = set(nums)
```

只从连续序列的起点开始数。

如果：

```python
num - 1 in num_set
```

说明 `num` 不是起点，跳过。

只有当：

```python
num - 1 not in num_set
```

才从 `num` 开始不断找 `num + 1`。

模板：

```python
num_set = set(nums)
ans = 0

for num in num_set:
    if num - 1 not in num_set:
        cur = num
        while cur in num_set:
            cur += 1
        ans = max(ans, cur - num)

return ans
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(n)
```

## 二、双指针 2_pointers

双指针适合解决：

- 数组原地修改
- 有序数组中的查找
- 左右边界共同决定答案
- 固定一个元素后，在剩余区间找两个元素
- 两端向中间收缩

常见类型：

```text
同向双指针：left 和 right 都向右走
对撞双指针：left 从左走，right 从右走
排序 + 双指针：先排序，再左右夹逼
```

### 1. 移动零：`2_pointers/283.py`

题目特点：

把所有 `0` 移到末尾，同时保持非零元素相对顺序，要求原地操作。

核心思路：

使用写指针 `j`，表示下一个非零元素应该放的位置。

先把所有非零元素依次写到前面，再把后面补成 `0`。

模板：

```python
j = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[j] = nums[i]
        j += 1

for i in range(j, len(nums)):
    nums[i] = 0
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(1)
```

### 2. 盛最多水的容器：`2_pointers/11.py`

题目特点：

选择两条线，使容器面积最大。

面积公式：

```python
area = (right - left) * min(height[left], height[right])
```

核心思路：

左右指针分别从两端开始，每次计算面积，然后移动较短的那一边。

原因：

面积由短板决定。移动高的一边，宽度变小，短板没有变高，面积不可能更大。

模板：

```python
left = 0
right = len(height) - 1
ans = 0

while left < right:
    ans = max(ans, (right - left) * min(height[left], height[right]))

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

return ans
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(1)
```

### 3. 三数之和：`2_pointers/15.py`

题目特点：

找所有不重复三元组，使三数之和为 `0`。

核心思路：

先排序，然后固定一个数 `nums[i]`，在右侧区间用双指针找另外两个数。

排序后：

- `left` 右移，三数和变大
- `right` 左移，三数和变小

关键去重：

固定第一个数时去重：

```python
if i > 0 and nums[i] == nums[i - 1]:
    continue
```

找到答案后跳过重复的左右指针：

```python
while left < right and nums[left] == nums[left + 1]:
    left += 1
while left < right and nums[right] == nums[right - 1]:
    right -= 1
```

模板：

```python
nums.sort()
res = []

for i in range(len(nums) - 2):
    if nums[i] > 0:
        break

    if i > 0 and nums[i] == nums[i - 1]:
        continue

    left = i + 1
    right = len(nums) - 1

    while left < right:
        total = nums[i] + nums[left] + nums[right]

        if total == 0:
            res.append([nums[i], nums[left], nums[right]])

            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            left += 1
            right -= 1
        elif total < 0:
            left += 1
        else:
            right -= 1

return res
```

复杂度：

```text
时间复杂度：O(n^2)
空间复杂度：O(1)
```

不计算返回结果和排序额外空间。

### 4. 接雨水：`2_pointers/42.py`

题目特点：

每个位置能接的水由左边最高柱子和右边最高柱子共同决定。

公式：

```text
当前位置接水量 = min(左侧最高, 右侧最高) - 当前高度
```

核心思路：

用双指针从两端向中间走，同时维护：

```python
left_max
right_max
```

每次移动高度较小的一侧，因为较小侧的接水上限已经可以确定。

模板：

```python
left = 0
right = len(height) - 1
left_max = 0
right_max = 0
ans = 0

while left < right:
    if height[left] < height[right]:
        if height[left] >= left_max:
            left_max = height[left]
        else:
            ans += left_max - height[left]
        left += 1
    else:
        if height[right] >= right_max:
            right_max = height[right]
        else:
            ans += right_max - height[right]
        right -= 1

return ans
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(1)
```

## 三、滑动窗口 sliding_win

滑动窗口适合解决：

- 连续子串
- 连续子数组
- 固定长度窗口
- 满足某种条件的最长/最短区间
- 字符计数匹配

常见类型：

```text
固定窗口：窗口长度固定，例如 len(p)
可变窗口：窗口长度变化，例如最长无重复子串
```

### 1. 无重复字符的最长子串：`sliding_win/3.py`

题目特点：

找不含重复字符的最长子串长度。

核心思路：

使用哈希表记录每个字符最后一次出现的位置：

```python
last_index[char] = right
```

当当前字符以前出现过，并且位置还在当前窗口内：

```python
last_index[char] >= left
```

就把左边界移动到重复字符的下一个位置：

```python
left = last_index[char] + 1
```

模板：

```python
last_index = {}
left = 0
ans = 0

for right, char in enumerate(s):
    if char in last_index and last_index[char] >= left:
        left = last_index[char] + 1

    last_index[char] = right
    ans = max(ans, right - left + 1)

return ans
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(min(n, 字符集大小))
```

注意：

如果用字符串切片保存窗口，再使用：

```python
char in sub_str
sub_str.index(char)
sub_str = s[left:right + 1]
```

这些操作都可能是 `O(k)`，整体最坏会接近 `O(n^2)`。

### 2. 找到字符串中所有字母异位词：`sliding_win/438.py`

题目特点：

在 `s` 中找所有长度等于 `len(p)` 且与 `p` 字母计数相同的子串。

核心思路：

窗口长度固定为 `len(p)`，维护两个长度为 `26` 的计数数组：

```python
p_count
win
```

每次右边加入一个字符，如果窗口超过长度，就左边移出一个字符。

当窗口长度等于 `len(p)` 且两个计数数组相等时，记录左端点。

模板：

```python
p_count = [0] * 26
win = [0] * 26
res = []

for c in p:
    p_count[ord(c) - ord("a")] += 1

left = 0

for right in range(len(s)):
    win[ord(s[right]) - ord("a")] += 1

    if right - left + 1 > len(p):
        win[ord(s[left]) - ord("a")] -= 1
        left += 1

    if right - left + 1 == len(p) and win == p_count:
        res.append(left)

return res
```

复杂度：

```text
时间复杂度：O(n * 26)，通常看作 O(n)
空间复杂度：O(26)，也就是 O(1)
```

## 四、子数组与前缀和 substring

这类题重点不是普通字符串，而是“连续子数组/子串”的统计。

常见套路：

```text
子数组和 = 当前前缀和 - 之前某个前缀和
```

只要题目里出现：

- 连续子数组
- 和为 k
- 统计个数
- 数组可能有负数

就要优先想到前缀和 + 哈希表。

### 1. 和为 K 的子数组：`substring/560.py`

题目特点：

统计和为 `k` 的连续子数组个数。

核心公式：

```text
prefix[j] - prefix[i - 1] = k
```

变形：

```text
prefix[i - 1] = prefix[j] - k
```

遍历到当前位置时，当前前缀和是 `cur_sum`，需要找以前出现过多少次：

```python
need = cur_sum - k
```

所以哈希表存：

```text
key：前缀和
value：这个前缀和出现次数
```

初始化：

```python
prefix_count = {0: 1}
```

表示数组开始之前，前缀和 `0` 出现过一次。这样可以统计从下标 `0` 开始的子数组。

模板：

```python
prefix_count = {0: 1}
cur_sum = 0
ans = 0

for num in nums:
    cur_sum += num

    need = cur_sum - k
    ans += prefix_count.get(need, 0)

    prefix_count[cur_sum] = prefix_count.get(cur_sum, 0) + 1

return ans
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(n)
```

为什么不用滑动窗口：

因为数组里可能有负数。窗口扩大不一定使和变大，窗口缩小也不一定使和变小，所以滑动窗口不稳定。

## 五、数组 array

数组题常见套路：

- 一次遍历维护状态
- 排序后处理
- 原地交换或反转
- 区间合并
- 动态规划

### 1. 最大子数组和：`array/53.py`

题目特点：

找和最大的连续子数组。

核心思路：

动态规划，也叫 Kadane 算法。

遍历到 `num` 时，只考虑两个选择：

```text
1. 接在之前的连续子数组后面
2. 从当前 num 重新开始
```

状态转移：

```python
cur_sum = max(num, cur_sum + num)
```

全局答案：

```python
max_sum = max(max_sum, cur_sum)
```

模板：

```python
cur_sum = nums[0]
max_sum = nums[0]

for num in nums[1:]:
    cur_sum = max(num, cur_sum + num)
    max_sum = max(max_sum, cur_sum)

return max_sum
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(1)
```

注意：

初始化要用 `nums[0]`，不要用 `0`，否则全负数数组会出错。

### 2. 合并区间：`array/56.py`

题目特点：

给定多个区间，合并所有重叠区间。

核心思路：

先按左端点排序：

```python
intervals.sort(key=lambda x: x[0])
```

然后从左到右处理，只需要比较当前区间和结果中的最后一个区间。

如果当前区间起点大于已合并区间终点，说明不重叠：

```python
interval[0] > res[-1][1]
```

否则说明重叠，更新右端点：

```python
res[-1][1] = max(res[-1][1], interval[1])
```

模板：

```python
intervals.sort(key=lambda x: x[0])
res = []

for interval in intervals:
    if not res or interval[0] > res[-1][1]:
        res.append(interval)
    else:
        res[-1][1] = max(res[-1][1], interval[1])

return res
```

复杂度：

```text
时间复杂度：O(n log n)
空间复杂度：O(n)
```

主要时间花在排序。

### 3. 轮转数组：`array/189.py`

题目特点：

将数组向右轮转 `k` 位，要求原地操作。

核心思路：

三次反转。

把数组分成两段：

```text
A B
```

其中 `B` 是最后 `k` 个元素。向右轮转 `k` 位的目标是：

```text
B A
```

三次反转过程：

```text
A B
整体反转 -> B反 A反
反转前 k 个 -> B A反
反转剩余部分 -> B A
```

模板：

```python
def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

n = len(nums)
k %= n

reverse(nums, 0, n - 1)
reverse(nums, 0, k - 1)
reverse(nums, k, n - 1)
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(1)
```

注意：

```python
nums[0:x].reverse()
```

不适合用于原地反转原数组的一段，因为切片会创建新列表，`reverse()` 只会反转这个临时列表。

## 六、刷题时如何判断用哪类方法

| 题目关键词 | 优先考虑 |
|---|---|
| 查找某个数是否出现过 | `set` |
| 记录元素下标 | `dict` |
| 统计次数 | `dict` / `Counter` |
| 按特征分组 | `dict` / `defaultdict(list)` |
| 未排序但要求 `O(n)` 查找 | 哈希表 |
| 连续子数组和为 `k`，可能有负数 | 前缀和 + 哈希表 |
| 连续子串，最长/最短 | 滑动窗口 |
| 固定长度子串匹配 | 固定窗口 + 计数 |
| 原地移动元素 | 同向双指针 |
| 两端共同决定答案 | 对撞双指针 |
| 三数/两数有序查找 | 排序 + 双指针 |
| 区间合并 | 按左端点排序 |
| 最大连续和 | 动态规划 |
| 数组轮转 | 三次反转 |

## 七、复杂度速查

| 方法 | 常见时间复杂度 | 常见空间复杂度 |
|---|---|---|
| 哈希表一次遍历 | `O(n)` | `O(n)` |
| 集合去重查找 | `O(n)` | `O(n)` |
| 双指针一次扫描 | `O(n)` | `O(1)` |
| 排序 + 双指针 | `O(n log n)` 或 `O(n^2)` | 通常 `O(1)` 或排序额外空间 |
| 滑动窗口 | `O(n)` | `O(字符集大小)` 或 `O(n)` |
| 前缀和 + 哈希表 | `O(n)` | `O(n)` |
| 区间排序合并 | `O(n log n)` | `O(n)` |
| Kadane 动态规划 | `O(n)` | `O(1)` |

