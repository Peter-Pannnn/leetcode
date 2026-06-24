# LeetCode 解题思路分类汇总

本文按当前文件夹分类整理常见解题套路：

- `hashmap`：哈希表、集合、计数、分组
- `2_pointers`：双指针、对撞指针、快慢指针
- `sliding_win`：滑动窗口
- `substring`：前缀和与子数组统计
- `array`：数组基础、区间、原地操作、动态规划
- `matrix`：矩阵模拟、原地标记、旋转与遍历
- `link`：链表指针、反转、快慢指针
- `bitree`：二叉树递归、层序遍历、二叉搜索树
- `graph`：图搜索、网格 DFS/BFS、连通块
- `backtrack`：回溯搜索、排列、子集
- `bisearch`：二分查找、边界二分、旋转数组
- `stack`：栈模拟、辅助栈、括号嵌套
- `heap`：堆、Top K、小顶堆
- `greedy`：贪心、最远覆盖、局部最优
- `dynamic`：一维动态规划、状态转移
- `2d_dynamic`：二维动态规划、路径类问题

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

## 六、矩阵 matrix

矩阵题常见套路：

- 用行列下标模拟移动过程
- 维护上下左右边界
- 使用第一行、第一列作为标记数组
- 原地交换元素，避免额外矩阵
- 明确 `m = len(matrix)`，`n = len(matrix[0])`

### 1. 矩阵置零：`matrix/73.py`

题目特点：

如果某个位置是 `0`，就把它所在的整行和整列都置为 `0`，要求原地操作。

三种思路：

```text
O(mn) 空间：复制原矩阵，再根据原矩阵的 0 修改 matrix
O(m+n) 空间：用 rows 和 cols 记录哪些行列需要置零
O(1) 空间：用第一行和第一列作为标记数组
```

最优思路：

用 `matrix[i][0]` 标记第 `i` 行是否需要置零，用 `matrix[0][j]` 标记第 `j` 列是否需要置零。

第一行和第一列本身也可能有 `0`，所以要额外记录：

```python
first_row_zero = False
first_col_zero = False
```

模板：

```python
m = len(matrix)
n = len(matrix[0])

first_row_zero = any(matrix[0][j] == 0 for j in range(n))
first_col_zero = any(matrix[i][0] == 0 for i in range(m))

for i in range(1, m):
    for j in range(1, n):
        if matrix[i][j] == 0:
            matrix[i][0] = 0
            matrix[0][j] = 0

for i in range(1, m):
    for j in range(1, n):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
            matrix[i][j] = 0

if first_row_zero:
    for j in range(n):
        matrix[0][j] = 0

if first_col_zero:
    for i in range(m):
        matrix[i][0] = 0
```

复杂度：

```text
时间复杂度：O(mn)
空间复杂度：O(1)
```

### 2. 螺旋矩阵：`matrix/54.py`

题目特点：

按照顺时针螺旋顺序返回矩阵所有元素。

核心思路：

维护四个边界：

```python
top = 0
bottom = len(matrix) - 1
left = 0
right = len(matrix[0]) - 1
```

每一圈按四个方向走：

```text
1. 从左到右走 top 行
2. 从上到下走 right 列
3. 从右到左走 bottom 行
4. 从下到上走 left 列
```

走完一条边，就收缩对应边界。

模板：

```python
res = []
top = 0
bottom = len(matrix) - 1
left = 0
right = len(matrix[0]) - 1

while top <= bottom and left <= right:
    for j in range(left, right + 1):
        res.append(matrix[top][j])
    top += 1

    for i in range(top, bottom + 1):
        res.append(matrix[i][right])
    right -= 1

    if top <= bottom:
        for j in range(right, left - 1, -1):
            res.append(matrix[bottom][j])
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

return res
```

复杂度：

```text
时间复杂度：O(mn)
空间复杂度：O(1)
```

不计算返回结果。

### 3. 旋转图像：`matrix/48.py`

题目特点：

给定 `n x n` 矩阵，原地顺时针旋转 `90` 度。

核心思路：

```text
先上下翻转，再沿主对角线翻转
```

位置变化：

```text
matrix[i][j] -> matrix[j][n - 1 - i]
```

上下翻转后：

```text
matrix[i][j] -> matrix[n - 1 - i][j]
```

再沿主对角线翻转：

```text
matrix[n - 1 - i][j] -> matrix[j][n - 1 - i]
```

刚好等于顺时针旋转后的目标位置。

模板：

```python
n = len(matrix)

for i in range(n // 2):
    matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]

for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

复杂度：

```text
时间复杂度：O(n^2)
空间复杂度：O(1)
```

## 七、链表 link

链表题常见套路：

- 使用虚拟头节点简化边界
- 用 `prev`、`cur`、`next` 反转指针
- 快慢指针找中点或判断环
- 双指针同步移动消除长度差
- 比较节点是否相同，要比较节点对象，不是节点值
- 哈希表 + 双向链表维护访问顺序

### 1. 合并两个有序链表：`link/21.py`

题目特点：

给定两个升序链表，合并成一个新的升序链表。

核心思路：

使用虚拟头节点 `dummy`，每次把较小节点接到结果链表后面。

模板：

```python
dummy = ListNode()
cur = dummy

while list1 and list2:
    if list1.val <= list2.val:
        cur.next = list1
        list1 = list1.next
    else:
        cur.next = list2
        list2 = list2.next
    cur = cur.next

cur.next = list1 if list1 else list2
return dummy.next
```

复杂度：

```text
时间复杂度：O(m+n)
空间复杂度：O(1)
```

### 2. 反转链表：`link/206.py`

题目特点：

把单链表整体反转。

核心思路：

遍历链表，用 `prev` 保存已经反转好的前半部分，用 `cur` 指向当前节点。

每次需要先保存下一个节点：

```python
next_node = cur.next
```

然后反转当前节点指向：

```python
cur.next = prev
```

模板：

```python
prev = None
cur = head

while cur:
    next_node = cur.next
    cur.next = prev
    prev = cur
    cur = next_node

return prev
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(1)
```

### 3. 相交链表：`link/160.py`

题目特点：

给定两个链表头节点，返回它们相交的第一个节点。如果不相交，返回 `None`。

核心思路一：长度对齐。

先分别计算两个链表长度，让长链表先走长度差，然后两个指针一起走。

模板：

```python
len_a = get_len(headA)
len_b = get_len(headB)

while len_a > len_b:
    headA = headA.next
    len_a -= 1

while len_b > len_a:
    headB = headB.next
    len_b -= 1

while headA and headB:
    if headA == headB:
        return headA
    headA = headA.next
    headB = headB.next

return None
```

核心思路二：双指针换头。

```python
pA = headA
pB = headB

while pA != pB:
    pA = pA.next if pA else headB
    pB = pB.next if pB else headA

return pA
```

两个指针都走 `a + b` 的长度，如果有交点会在交点相遇，否则一起变成 `None`。

复杂度：

```text
时间复杂度：O(m+n)
空间复杂度：O(1)
```

### 4. 环形链表与入环点：`link/141.py`

题目特点：

判断链表是否有环；进一步可以返回入环的第一个节点。

判断是否有环：

使用快慢指针。`slow` 每次走一步，`fast` 每次走两步。

```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        return True

return False
```

寻找入环点：

快慢指针相遇后，一个指针从 `head` 出发，另一个从相遇点出发，每次都走一步，再次相遇的位置就是入环点。

```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        p1 = head
        p2 = slow

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1

return None
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(1)
```

### 5. 回文链表：`link/234.py`

题目特点：

判断链表从前往后和从后往前读是否一样，进阶要求 `O(1)` 空间。

核心思路：

```text
快慢指针找中点 -> 反转后半部分 -> 前半部分和后半部分逐个比较
```

模板：

```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

if fast:
    slow = slow.next

prev = None
cur = slow
while cur:
    next_node = cur.next
    cur.next = prev
    prev = cur
    cur = next_node

p1 = head
p2 = prev

while p2:
    if p1.val != p2.val:
        return False
    p1 = p1.next
    p2 = p2.next

return True
```

注意：

如果链表长度为奇数，可以跳过中间节点：

```python
if fast:
    slow = slow.next
```

不跳过也能判断，因为中间节点会和自己比较，但跳过更清晰。

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(1)
```

### 6. LRU 缓存：`link/146.py`

题目特点：

设计最近最少使用缓存，要求 `get` 和 `put` 平均时间复杂度都是 `O(1)`。

核心思路：

```text
哈希表 + 双向链表
```

哈希表负责通过 `key` 在 `O(1)` 时间内找到节点：

```python
cache = {}  # key -> Node
```

双向链表负责维护使用顺序：

```text
head <-> 最近使用 ... 最久未使用 <-> tail
```

其中：

```text
head 后面的节点是最近使用
tail 前面的节点是最久未使用
```

节点需要保存 `key`，因为淘汰尾部节点时，要从哈希表中删除对应 key。

常用辅助操作：

```python
def _remove(node):
    node.prev.next = node.next
    node.next.prev = node.prev


def _add_to_head(node):
    node.prev = head
    node.next = head.next
    head.next.prev = node
    head.next = node
```

`get` 思路：

```text
1. key 不存在，返回 -1
2. key 存在，取出节点
3. 把节点移动到头部，表示最近使用
4. 返回节点 value
```

`put` 思路：

```text
1. key 已存在：更新 value，并移动到头部
2. key 不存在：新建节点，加入哈希表和链表头部
3. 如果超过容量：删除 tail 前面的最久未使用节点，并从哈希表删除
```

模板：

```python
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_head(node)

        if len(self.cache) > self.capacity:
            removed = self._remove_tail()
            del self.cache[removed.key]
```

复杂度：

```text
get 时间复杂度：O(1)
put 时间复杂度：O(1)
空间复杂度：O(capacity)
```

## 八、二叉树 bitree

二叉树题常见套路：

- 递归处理左右子树
- 前序、中序、后序遍历
- 层序遍历使用队列
- 自底向上返回高度或状态
- 二叉搜索树利用中序有序性质

常见递归结构：

```python
def dfs(root):
    if not root:
        return

    dfs(root.left)
    dfs(root.right)
```

### 1. 二叉树中序遍历：`bitree/94.py`

题目特点：

返回二叉树的中序遍历结果。

核心思路：

中序遍历顺序是：

```text
左子树 -> 当前节点 -> 右子树
```

模板：

```python
res = []

def inorder(root):
    if not root:
        return
    inorder(root.left)
    res.append(root.val)
    inorder(root.right)

inorder(root)
return res
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(h)
```

其中 `h` 是树高。

### 2. 对称二叉树：`bitree/101.py`

题目特点：

判断一棵二叉树是否关于中轴线对称。

核心思路：

不要分别判断左右子树是否各自对称，而是判断左右子树是否互为镜像。

镜像关系：

```text
left.left  对应  right.right
left.right 对应  right.left
```

模板：

```python
def compare(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False

    return (
        left.val == right.val
        and compare(left.left, right.right)
        and compare(left.right, right.left)
    )

return compare(root.left, root.right)
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(h)
```

### 3. 二叉树层序遍历：`bitree/102.py`

题目特点：

逐层从左到右返回节点值。

核心思路：

层序遍历是 BFS，用队列保存当前待访问节点。

每一轮先记录当前层节点数：

```python
size = len(queue)
```

然后只处理这 `size` 个节点。它们的孩子加入队列后，属于下一层。

模板：

```python
from collections import deque

res = []
queue = deque([root])

while queue:
    size = len(queue)
    level = []

    for _ in range(size):
        node = queue.popleft()
        level.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    res.append(level)

return res
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(n)
```

### 4. 二叉树最大深度：`bitree/104.py`

题目特点：

求根节点到最远叶子节点的节点数。

核心思路：

递归求左右子树深度，当前节点深度等于较大值加 `1`。

模板：

```python
if not root:
    return 0

left = maxDepth(root.left)
right = maxDepth(root.right)
return max(left, right) + 1
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(h)
```

### 5. 有序数组转换为平衡 BST：`bitree/108.py`

题目特点：

给定升序数组，构造一棵高度平衡的二叉搜索树。

核心思路：

每次选择当前区间的中点作为根节点：

```text
左半部分构造左子树
右半部分构造右子树
```

这样左右子树元素数量尽量接近，树高也保持平衡。

模板：

```python
def build(left, right):
    if left > right:
        return None

    mid = (left + right) // 2
    root = TreeNode(nums[mid])
    root.left = build(left, mid - 1)
    root.right = build(mid + 1, right)
    return root

return build(0, len(nums) - 1)
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(log n)
```

### 6. 翻转二叉树：`bitree/226.py`

题目特点：

交换每个节点的左右子树。

核心思路：

递归处理左右子树，然后交换当前节点的左右孩子。

模板：

```python
if not root:
    return None

invertTree(root.left)
invertTree(root.right)
root.left, root.right = root.right, root.left
return root
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(h)
```

### 7. 二叉搜索树第 K 小元素：`bitree/230.py`

题目特点：

在 BST 中找第 `k` 小的元素。

核心思路：

二叉搜索树的中序遍历结果是升序：

```text
第 k 小 = 中序遍历第 k 个节点
```

模板：

```python
res = []

def inorder(root):
    if not root:
        return
    inorder(root.left)
    res.append(root.val)
    inorder(root.right)

inorder(root)
return res[k - 1]
```

优化方向：

中序遍历时用计数器，访问到第 `k` 个节点后提前停止。

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(h) 或 O(n)
```

如果保存完整中序数组，额外空间是 `O(n)`。

### 8. 二叉树的直径：`bitree/543.py`

题目特点：

求任意两个节点之间最长路径的边数，路径不一定经过根节点。

核心思路：

对每个节点，经过它的最长路径是：

```text
左子树最大深度 + 右子树最大深度
```

DFS 返回当前节点向下的最大深度，同时用全局答案记录最大直径。

模板：

```python
ans = 0

def depth(root):
    nonlocal ans

    if not root:
        return 0

    left = depth(root.left)
    right = depth(root.right)

    ans = max(ans, left + right)
    return max(left, right) + 1

depth(root)
return ans
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(h)
```

## 九、图 graph

图题常见套路：

- DFS 一条路走到底
- BFS 一层一层向外扩散
- 普通图通常需要 `visited`
- 网格图可以把访问过的格子直接改值
- 求岛屿数量、本质是求连通块数量

二维网格常用方向数组：

```python
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
```

### 1. 岛屿数量：`graph/200.py`

题目特点：

给定由 `'1'` 和 `'0'` 组成的网格，统计由上下左右相邻陆地组成的岛屿数量。

核心思路：

遍历整个网格。每遇到一个新的 `'1'`，说明发现一座新岛：

```text
岛屿数量 +1
从这个位置开始 DFS/BFS，把整座岛都标记为已访问
```

标记方式：

```python
grid[i][j] = "0"
```

相当于把已经访问过的陆地淹掉，避免重复统计。

DFS 模板：

```python
def dfs(i, j):
    if i < 0 or i >= m or j < 0 or j >= n:
        return
    if grid[i][j] == "0":
        return

    grid[i][j] = "0"

    dfs(i - 1, j)
    dfs(i + 1, j)
    dfs(i, j - 1)
    dfs(i, j + 1)
```

外层遍历：

```python
count = 0

for i in range(m):
    for j in range(n):
        if grid[i][j] == "1":
            count += 1
            dfs(i, j)

return count
```

关键边界：

```text
i 是行下标，用 m 判断
j 是列下标，用 n 判断
```

复杂度：

```text
时间复杂度：O(mn)
空间复杂度：O(mn)
```

最坏情况下整张网格都是陆地，递归栈可能达到 `O(mn)`。

### 2. 腐烂的橘子：`graph/994.py`

题目特点：

多个腐烂橘子会同时向上下左右扩散，要求所有新鲜橘子腐烂的最少分钟数。

核心思路：

这是多源 BFS。先把所有初始腐烂橘子加入同一个队列，并统计新鲜橘子数量：

```python
queue = deque()
fresh = 0
```

每一轮 BFS 表示经过 `1` 分钟。当前队列中的节点是这一分钟同时扩散的腐烂橘子：

```python
size = len(queue)

for _ in range(size):
    i, j = queue.popleft()
```

新腐烂的橘子加入队列，下一分钟继续扩散。

关键点：

```text
所有起点先入队
每轮处理当前队列长度 size 个节点
每腐烂一个新鲜橘子，fresh -= 1
```

结束判断：

```text
如果 fresh == 0，返回分钟数
如果 BFS 结束仍有 fresh，返回 -1
```

复杂度：

```text
时间复杂度：O(mn)
空间复杂度：O(mn)
```

## 十、回溯 backtrack

回溯题常见套路：

- 枚举所有可能选择
- 用 `path` 保存当前路径
- 用递归进入下一层选择
- 递归返回后撤销选择
- 排列问题常用 `used`
- 组合/子集问题常用 `start`

基本结构：

```python
def backtrack(...):
    if 到达结束条件:
        res.append(path[:])
        return

    for 选择 in 选择列表:
        做选择
        backtrack(...)
        撤销选择
```

### 1. 全排列：`backtrack/46.py`

题目特点：

给定不含重复数字的数组，返回所有可能的排列。

核心思路：

每个位置都可以选择一个还没用过的数字。用 `used[i]` 记录 `nums[i]` 是否已经放进当前排列。

模板：

```python
res = []
path = []
used = [False] * len(nums)

def backtrack():
    if len(path) == len(nums):
        res.append(path[:])
        return

    for i in range(len(nums)):
        if used[i]:
            continue

        path.append(nums[i])
        used[i] = True
        backtrack()
        path.pop()
        used[i] = False
```

复杂度：

```text
时间复杂度：O(n * n!)
空间复杂度：O(n)
```

不计算返回结果。

### 2. 子集：`backtrack/78.py`

题目特点：

给定不含重复数字的数组，返回所有可能子集。

核心思路：

每一个 `path` 都是合法子集，所以进入递归时先收集当前路径。用 `start` 控制下一次只能从后面选择，避免重复子集。

模板：

```python
res = []
path = []

def backtrack(start):
    res.append(path[:])

    for i in range(start, len(nums)):
        path.append(nums[i])
        backtrack(i + 1)
        path.pop()
```

复杂度：

```text
时间复杂度：O(n * 2^n)
空间复杂度：O(n)
```

不计算返回结果。

## 十一、二分查找 bisearch

二分题常见套路：

- 有序数组查找
- 找第一个满足条件的位置
- 找左边界和右边界
- 把二维矩阵映射成一维数组
- 旋转有序数组先判断有序区间或先找旋转点

普通二分模板：

```python
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

### 1. 搜索旋转排序数组：`bisearch/33.py`

题目特点：

升序数组在某个位置旋转后，查找 `target` 下标。

核心思路：

可以先找旋转点 `k`，也就是最小值下标。旋转后数组由两段升序区间组成：

```text
[0, k - 1]
[k, n - 1]
```

找旋转点：

```python
while left < right:
    mid = (left + right) // 2

    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid
```

然后判断 `target` 落在哪一段，对对应区间做普通二分。

复杂度：

```text
时间复杂度：O(log n)
空间复杂度：O(1)
```

### 2. 在排序数组中查找元素的第一个和最后一个位置：`bisearch/34.py`

题目特点：

给定非递减数组，返回 `target` 的起始和结束下标。

核心思路：

用边界二分：

```text
左边界 = 第一个 >= target 的位置
右边界 = 第一个 >= target + 1 的位置 - 1
```

`lower_bound` 模板：

```python
def lower_bound(x):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] >= x:
            right = mid - 1
        else:
            left = mid + 1

    return left
```

判断不存在：

```python
if left == len(nums) or nums[left] != target:
    return [-1, -1]
```

复杂度：

```text
时间复杂度：O(log n)
空间复杂度：O(1)
```

### 3. 搜索二维矩阵：`bisearch/74.py`

题目特点：

矩阵每行递增，且下一行第一个数大于上一行最后一个数。

核心思路：

把 `m x n` 矩阵看成一个长度为 `m * n` 的升序数组，不需要真的展开。

一维下标转二维下标：

```python
i = mid // n
j = mid % n
```

二分范围：

```python
left = 0
right = m * n - 1
```

复杂度：

```text
时间复杂度：O(log(mn))
空间复杂度：O(1)
```

## 十二、栈 stack

栈题常见套路：

- 后进先出
- 用辅助栈维护额外状态
- 处理括号或嵌套结构
- 遇到开始符号入栈，遇到结束符号出栈

常用操作：

```python
stack.append(x)
stack.pop()
stack[-1]
```

### 1. 最小栈：`stack/155.py`

题目特点：

设计一个栈，要求 `push`、`pop`、`top`、`getMin` 都是 `O(1)`。

核心思路：

维护两个栈：

```text
stack：正常保存元素
min_stack：同步保存每一层对应的最小值
```

每次入栈：

```python
stack.append(value)
min_stack.append(min(value, min_stack[-1]))
```

每次出栈时两个栈同步弹出。当前最小值就是：

```python
min_stack[-1]
```

复杂度：

```text
每个操作时间复杂度：O(1)
空间复杂度：O(n)
```

### 2. 字符串解码：`stack/394.py`

题目特点：

解码形如 `k[encoded_string]` 的字符串，括号可能嵌套。

核心思路：

维护当前数字 `num`、当前字符串 `cur` 和栈 `stack`。

遍历字符：

```text
数字：累积 num
[：把当前 cur 和 num 入栈，开始新一层
字母：加入 cur
]：弹出上一层状态，拼接 prev + cur * repeat
```

模板：

```python
stack = []
cur = ""
num = 0

for ch in s:
    if ch.isdigit():
        num = num * 10 + int(ch)
    elif ch == "[":
        stack.append((cur, num))
        cur = ""
        num = 0
    elif ch == "]":
        prev, repeat = stack.pop()
        cur = prev + cur * repeat
    else:
        cur += ch
```

复杂度：

```text
时间复杂度：O(输出字符串长度)
空间复杂度：O(输出字符串长度 + 嵌套深度)
```

## 十三、堆 heap

堆题常见套路：

- Top K 问题
- 维护大小为 `k` 的小顶堆
- Python `heapq` 默认是小顶堆
- 堆里存元组时按元组字典序比较

常用操作：

```python
heapq.heappush(heap, x)
heapq.heappop(heap)
heap[0]
```

### 1. 数组中的第 K 个最大元素：`heap/215.py`

题目特点：

返回排序后的第 `k` 个最大元素，重复元素正常参与排名。

核心思路：

维护大小为 `k` 的小顶堆：

```text
堆里始终保存当前见过的最大的 k 个数
堆顶就是第 k 大
```

模板：

```python
heap = []

for num in nums:
    heapq.heappush(heap, num)

    if len(heap) > k:
        heapq.heappop(heap)

return heap[0]
```

复杂度：

```text
时间复杂度：O(n log k)
空间复杂度：O(k)
```

如果严格要求平均 `O(n)`，可使用快速选择。

### 2. 前 K 个高频元素：`heap/347.py`

题目特点：

返回数组中出现频率前 `k` 高的元素，答案顺序任意。

核心思路：

先用哈希表统计频率，再维护大小为 `k` 的小顶堆。堆里放：

```python
(freq, num)
```

`heapq` 会先按 `freq` 比较，频率相同再比较 `num`。

模板：

```python
count = {}

for num in nums:
    count[num] = count.get(num, 0) + 1

heap = []

for num, freq in count.items():
    heapq.heappush(heap, (freq, num))

    if len(heap) > k:
        heapq.heappop(heap)

return [num for freq, num in heap]
```

复杂度：

```text
时间复杂度：O(n log k)
空间复杂度：O(n)
```

也可以用桶排序做到 `O(n)`。

## 十四、贪心 greedy

贪心题常见套路：

- 只维护当前最优状态
- 不关心完整路径，只关心能否覆盖或当前最大收益
- 每一步做局部最优选择，并能推出全局最优
- 常见变量有最小值、最大值、最远边界、当前覆盖范围

### 1. 买卖股票的最佳时机：`greedy/121.py`

题目特点：

只能买入一次、卖出一次，并且必须先买后卖，求最大利润。

核心思路：

遍历每一天，把当天价格当作卖出价。为了利润最大，买入价应该是这一天之前出现过的最低价格。

维护两个变量：

```python
min_price
max_profit
```

模板：

```python
min_price = prices[0]
max_profit = 0

for price in prices:
    max_profit = max(max_profit, price - min_price)
    min_price = min(min_price, price)

return max_profit
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(1)
```

### 2. 跳跃游戏：`greedy/55.py`

题目特点：

每个位置表示最大跳跃长度，判断能否到达最后一个下标。

核心思路：

维护当前最远可达位置：

```python
farthest
```

遍历到下标 `i` 时，如果 `i > farthest`，说明当前位置都到不了，直接返回 `False`。否则用当前位置继续扩展最远可达范围：

```python
farthest = max(farthest, i + nums[i])
```

模板：

```python
farthest = 0

for i in range(len(nums)):
    if i > farthest:
        return False

    farthest = max(farthest, i + nums[i])

    if farthest >= len(nums) - 1:
        return True

return True
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(1)
```

### 3. 跳跃游戏 II：`greedy/45.py`

题目特点：

保证可以到达最后一个下标，求到达终点的最少跳跃次数。

核心思路：

按 BFS 层的方式理解每一次跳跃。维护：

```text
cur_end：当前这一跳能覆盖到的最远边界
farthest：在当前覆盖范围内，下一跳能到达的最远位置
steps：已经跳了几次
```

遍历到 `cur_end` 时，说明当前这一跳的范围已经看完，必须跳下一次：

```python
steps += 1
cur_end = farthest
```

模板：

```python
steps = 0
cur_end = 0
farthest = 0

for i in range(len(nums) - 1):
    farthest = max(farthest, i + nums[i])

    if i == cur_end:
        steps += 1
        cur_end = farthest

return steps
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(1)
```

## 十五、一维动态规划 dynamic

动态规划题常见套路：

- 定义 `dp[i]` 的含义
- 找当前状态和前面状态的关系
- 明确初始化
- 按状态依赖顺序遍历
- 如果只依赖前几个状态，可以用变量压缩空间

### 1. 爬楼梯：`dynamic/70.py`

题目特点：

每次可以爬 `1` 或 `2` 阶，求到达第 `n` 阶的方法数。

核心思路：

到达第 `i` 阶只有两种来源：

```text
从 i - 1 阶爬 1 步
从 i - 2 阶爬 2 步
```

所以：

```text
dp[i] = dp[i - 1] + dp[i - 2]
```

初始化：

```text
dp[1] = 1
dp[2] = 2
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(n)，可优化为 O(1)
```

### 2. 打家劫舍：`dynamic/198.py`

题目特点：

不能偷相邻房屋，求能偷到的最大金额。

核心思路：

每间房有两个选择：

```text
偷当前：前前最大金额 + 当前金额
不偷当前：前一个最大金额
```

状态转移：

```text
dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
```

空间优化时只维护两个变量：

```python
ppre = 0
pre = 0

for num in nums:
    cur = max(num + ppre, pre)
    ppre = pre
    pre = cur

return pre
```

复杂度：

```text
时间复杂度：O(n)
空间复杂度：O(1)
```

### 3. 完全平方数：`dynamic/279.py`

题目特点：

用最少数量的完全平方数凑出 `n`。

核心思路：

定义：

```text
dp[i] 表示凑出 i 所需要的最少完全平方数数量
```

枚举最后使用的平方数 `j*j`：

```text
dp[i] = min(dp[i], dp[i - j*j] + 1)
```

模板：

```python
dp = [float("inf")] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    j = 1
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

return dp[n]
```

复杂度：

```text
时间复杂度：O(n * sqrt(n))
空间复杂度：O(n)
```

## 十六、二维动态规划 2d_dynamic

二维 DP 题常见套路：

- `dp[i][j]` 表示到达或处理到某个格子的最优值
- 当前格子通常依赖上方和左方
- 第一行、第一列通常需要特殊初始化
- 如果只依赖上一行和当前行左侧，可以压缩成一维 DP

### 1. 不同路径：`2d_dynamic/62.py`

题目特点：

从左上角到右下角，每次只能向右或向下，求路径数量。

核心思路：

二维状态：

```text
dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
```

第一行和第一列都只有一种走法。空间优化后，用一维数组保存当前行：

```python
dp = [1] * n

for _ in range(1, m):
    for j in range(1, n):
        dp[j] += dp[j - 1]

return dp[-1]
```

其中：

```text
dp[j] 是上方路径数
dp[j - 1] 是左方路径数
```

复杂度：

```text
时间复杂度：O(mn)
空间复杂度：O(n)
```

### 2. 最小路径和：`2d_dynamic/64.py`

题目特点：

从左上角到右下角，每次只能向右或向下，求路径上的最小数字和。

核心思路：

到达当前格子只能来自上方或左方，所以：

```text
dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
```

边界处理：

```text
第一行只能从左边来
第一列只能从上边来
左上角就是 grid[0][0]
```

也可以像当前题解一样，把越界方向视为 `inf`，这样 `min` 时自然不会选到越界方向。

复杂度：

```text
时间复杂度：O(mn)
空间复杂度：O(mn)，可优化为 O(n)
```

## 十七、刷题时如何判断用哪类方法

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
| 矩阵顺时针遍历 | 上下左右边界模拟 |
| 矩阵原地修改 | 第一行第一列做标记 |
| 矩阵旋转 | 翻转 + 转置 |
| 链表合并/拼接 | 虚拟头节点 |
| 链表反转 | `prev` / `cur` / `next` 三指针 |
| 链表找中点或判环 | 快慢指针 |
| 两链表相交 | 长度对齐或双指针换头 |
| LRU 缓存 | 哈希表 + 双向链表 |
| 二叉树遍历 | DFS 前序/中序/后序 |
| 二叉树逐层访问 | BFS + `deque` |
| 二叉树高度/直径/平衡 | 后序 DFS |
| 二叉搜索树第 k 小 | 中序遍历 |
| 有序数组构造平衡 BST | 取中点递归 |
| 网格连通块/岛屿数量 | DFS/BFS + visited |
| 多起点同时扩散/最少分钟数 | 多源 BFS |
| 排列/子集/组合枚举 | 回溯 |
| 有序数组查找 | 二分查找 |
| 查找第一个/最后一个位置 | 边界二分 |
| 旋转有序数组查找 | 找旋转点或判断有序半边 |
| 括号嵌套/字符串解码 | 栈 |
| 常数时间获取栈内最小值 | 辅助栈 |
| 第 k 大/Top K | 小顶堆 |
| 高频元素前 k 个 | 哈希表计数 + 堆/桶 |
| 股票一次买卖最大利润 | 贪心维护历史最低价 |
| 跳跃能否到达 | 贪心维护最远覆盖 |
| 跳跃最少次数 | 贪心分层覆盖 |
| 当前状态依赖前几个状态 | 一维动态规划 |
| 不能选择相邻元素 | 动态规划选/不选 |
| 最少数量凑目标值 | 动态规划 / 完全背包 |
| 网格路径数量或最小路径和 | 二维动态规划 |

## 十八、复杂度速查

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
| 矩阵边界模拟 | `O(mn)` | `O(1)` 不算返回结果 |
| 矩阵原地标记 | `O(mn)` | `O(1)` |
| 链表一次遍历 | `O(n)` | `O(1)` |
| 链表快慢指针 | `O(n)` | `O(1)` |
| LRU Cache | `O(1)` get / `O(1)` put | `O(capacity)` |
| 二叉树 DFS | `O(n)` | `O(h)` |
| 二叉树 BFS | `O(n)` | `O(n)` |
| BST 中序遍历 | `O(n)` | `O(h)` 到 `O(n)` |
| 网格 DFS/BFS | `O(mn)` | `O(mn)` |
| 多源 BFS | `O(mn)` | `O(mn)` |
| 回溯全排列 | `O(n * n!)` | `O(n)` 不算返回结果 |
| 回溯子集 | `O(n * 2^n)` | `O(n)` 不算返回结果 |
| 二分查找 | `O(log n)` | `O(1)` |
| 矩阵二分 | `O(log(mn))` | `O(1)` |
| 栈模拟 | `O(n)` | `O(n)` |
| 辅助栈操作 | `O(1)` | `O(n)` |
| 大小为 k 的小顶堆 | `O(n log k)` | `O(k)` |
| 贪心一次遍历 | `O(n)` | `O(1)` |
| 一维动态规划 | `O(n)` 或 `O(n * sqrt(n))` | `O(n)`，可视依赖优化 |
| 二维动态规划 | `O(mn)` | `O(mn)`，可优化为 `O(n)` |
