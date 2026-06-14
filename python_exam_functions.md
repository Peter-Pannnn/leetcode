# Python 笔试常见函数与复杂度速查

本文按笔试刷题常见场景整理：数组、字符串、哈希表、排序、栈队列、堆、二分、数学与常用模块。

复杂度中的 `n` 通常表示元素个数，`k` 表示字符串长度或额外参数大小。

## 一、常见内置函数

| 函数 | 作用 | 用法 | 时间复杂度 | 备注 |
|---|---|---|---|---|
| `len(x)` | 获取长度 | `len(nums)` | `O(1)` | 列表、字符串、字典、集合都常用 |
| `range(n)` | 生成整数序列 | `for i in range(n)` | 创建 `O(1)`，遍历 `O(n)` | 常用于下标循环 |
| `enumerate(x)` | 同时拿下标和值 | `for i, v in enumerate(nums)` | `O(n)` | 做题中非常常用 |
| `zip(a, b)` | 并行遍历多个序列 | `for x, y in zip(a, b)` | `O(min(len(a), len(b)))` | 常用于比较两个数组 |
| `sum(x)` | 求和 | `sum(nums)` | `O(n)` | 数字数组常用 |
| `max(x)` | 最大值 | `max(nums)` | `O(n)` | 也可传多个参数：`max(a, b)` |
| `min(x)` | 最小值 | `min(nums)` | `O(n)` | 也可传多个参数：`min(a, b)` |
| `abs(x)` | 绝对值 | `abs(-3)` | `O(1)` | 数学题常用 |
| `pow(a, b)` | 幂运算 | `pow(2, 10)` | 约 `O(log b)` | 快速幂 |
| `pow(a, b, mod)` | 带模幂运算 | `pow(2, 10, 1000000007)` | `O(log b)` | 比 `(a ** b) % mod` 更好 |
| `sorted(x)` | 返回排序后的新列表 | `sorted(nums)` | `O(n log n)` | 不修改原对象 |
| `reversed(x)` | 反向迭代 | `list(reversed(nums))` | 遍历 `O(n)` | 不直接生成列表 |
| `all(x)` | 判断是否全部为真 | `all(v > 0 for v in nums)` | 最坏 `O(n)` | 遇到假值会提前停止 |
| `any(x)` | 判断是否存在真值 | `any(v > 0 for v in nums)` | 最坏 `O(n)` | 遇到真值会提前停止 |
| `ord(c)` | 字符转 ASCII/Unicode 编码 | `ord('a')` | `O(1)` | 字母计数常用 |
| `chr(x)` | 编码转字符 | `chr(97)` | `O(1)` | `chr(97) == 'a'` |

## 二、列表 list

| 操作 | 作用 | 用法 | 时间复杂度 |
|---|---|---|---|
| 下标访问 | 获取元素 | `nums[i]` | `O(1)` |
| 下标修改 | 修改元素 | `nums[i] = x` | `O(1)` |
| 末尾添加 | 添加元素 | `nums.append(x)` | 均摊 `O(1)` |
| 末尾删除 | 删除最后一个元素 | `nums.pop()` | `O(1)` |
| 指定位置删除 | 删除某个下标 | `nums.pop(i)` | `O(n)` |
| 插入 | 在指定位置插入 | `nums.insert(i, x)` | `O(n)` |
| 查找元素 | 判断是否存在 | `x in nums` | `O(n)` |
| 反转 | 原地反转 | `nums.reverse()` | `O(n)` |
| 排序 | 原地排序 | `nums.sort()` | `O(n log n)` |
| 切片 | 复制一段 | `nums[l:r]` | `O(r-l)` |

常见写法：

```python
nums = [3, 1, 2]
nums.append(4)
nums.pop()
nums.sort()
nums.sort(reverse=True)
```

注意：

```python
nums.sort()      # 原地排序，返回 None
sorted(nums)     # 返回新列表，不改 nums
```

## 三、字符串 str

| 操作 | 作用 | 用法 | 时间复杂度 |
|---|---|---|---|
| 下标访问 | 获取字符 | `s[i]` | `O(1)` |
| 切片 | 截取字符串 | `s[l:r]` | `O(r-l)` |
| 拼接 | 拼接字符串 | `a + b` | `O(len(a)+len(b))` |
| 查找 | 判断子串是否存在 | `sub in s` | 平均接近 `O(n)` |
| 分割 | 按分隔符切分 | `s.split()` | `O(n)` |
| 合并 | 合并字符串列表 | `"".join(arr)` | `O(n)` |
| 去空格 | 去除两边空白 | `s.strip()` | `O(n)` |
| 替换 | 替换子串 | `s.replace(a, b)` | `O(n)` |
| 排序字符 | 得到排序后的字符 | `"".join(sorted(s))` | `O(k log k)` |

常见写法：

```python
s = "eat"
key = "".join(sorted(s))  # "aet"
```

注意：字符串不可变，频繁拼接时不要这样：

```python
ans = ""
for c in chars:
    ans += c
```

更推荐：

```python
arr = []
for c in chars:
    arr.append(c)
ans = "".join(arr)
```

## 四、字典 dict

| 操作 | 作用 | 用法 | 平均时间复杂度 |
|---|---|---|---|
| 创建 | 创建哈希表 | `mp = {}` | `O(1)` |
| 插入/修改 | 设置键值 | `mp[key] = value` | `O(1)` |
| 读取 | 根据 key 取值 | `mp[key]` | `O(1)` |
| 安全读取 | 不存在时给默认值 | `mp.get(key, 0)` | `O(1)` |
| 判断 key | key 是否存在 | `key in mp` | `O(1)` |
| 删除 | 删除 key | `del mp[key]` | `O(1)` |
| 遍历 key | 遍历所有 key | `for key in mp` | `O(n)` |
| 遍历键值 | 遍历 key 和 value | `for k, v in mp.items()` | `O(n)` |

常见场景：

```python
# 计数
cnt = {}
for x in nums:
    cnt[x] = cnt.get(x, 0) + 1

# 两数之和
seen = {}
for i, x in enumerate(nums):
    need = target - x
    if need in seen:
        return [seen[need], i]
    seen[x] = i
```

## 五、集合 set

| 操作 | 作用 | 用法 | 平均时间复杂度 |
|---|---|---|---|
| 创建 | 创建集合 | `st = set()` | `O(1)` |
| 添加 | 加入元素 | `st.add(x)` | `O(1)` |
| 删除 | 删除元素 | `st.remove(x)` | `O(1)` |
| 安全删除 | 不存在也不报错 | `st.discard(x)` | `O(1)` |
| 判断存在 | 元素是否存在 | `x in st` | `O(1)` |
| 去重 | 数组去重 | `set(nums)` | `O(n)` |
| 交集 | 共同元素 | `a & b` | 约 `O(min(len(a), len(b)))` |
| 并集 | 合并元素 | `a | b` | `O(len(a)+len(b))` |

常见场景：

```python
seen = set()
for x in nums:
    if x in seen:
        print("重复")
    seen.add(x)
```

## 六、排序

| 写法 | 作用 | 时间复杂度 |
|---|---|---|
| `nums.sort()` | 原地升序排序 | `O(n log n)` |
| `nums.sort(reverse=True)` | 原地降序排序 | `O(n log n)` |
| `sorted(nums)` | 返回升序新列表 | `O(n log n)` |
| `sorted(nums, key=lambda x: x[1])` | 按规则排序 | `O(n log n)` |

常见写法：

```python
intervals.sort(key=lambda x: x[0])     # 按第一个元素排序
intervals.sort(key=lambda x: (x[0], x[1]))  # 先按 x[0]，再按 x[1]
```

## 七、栈 stack

Python 中一般用列表模拟栈。

| 操作 | 用法 | 时间复杂度 |
|---|---|---|
| 入栈 | `stack.append(x)` | `O(1)` |
| 出栈 | `stack.pop()` | `O(1)` |
| 看栈顶 | `stack[-1]` | `O(1)` |
| 判断非空 | `if stack:` | `O(1)` |

常见场景：括号匹配、单调栈、DFS。

```python
stack = []
for x in nums:
    while stack and stack[-1] > x:
        stack.pop()
    stack.append(x)
```

## 八、队列 deque

普通列表 `pop(0)` 是 `O(n)`，笔试中队列推荐用 `collections.deque`。

```python
from collections import deque
```

| 操作 | 用法 | 时间复杂度 |
|---|---|---|
| 右侧入队 | `q.append(x)` | `O(1)` |
| 左侧出队 | `q.popleft()` | `O(1)` |
| 左侧入队 | `q.appendleft(x)` | `O(1)` |
| 右侧出队 | `q.pop()` | `O(1)` |
| 查看队首 | `q[0]` | `O(1)` |

常见场景：BFS、滑动窗口最大值。

```python
q = deque([root])
while q:
    node = q.popleft()
```

## 九、堆 heapq

Python 的 `heapq` 默认是小根堆。

```python
import heapq
```

| 操作 | 用法 | 时间复杂度 |
|---|---|---|
| 建堆 | `heapq.heapify(nums)` | `O(n)` |
| 入堆 | `heapq.heappush(heap, x)` | `O(log n)` |
| 出堆 | `heapq.heappop(heap)` | `O(log n)` |
| 看堆顶 | `heap[0]` | `O(1)` |

常见写法：

```python
heap = []
heapq.heappush(heap, x)
smallest = heapq.heappop(heap)
```

大根堆写法：存负数。

```python
heapq.heappush(heap, -x)
largest = -heapq.heappop(heap)
```

常见场景：Top K、合并 K 个有序链表、数据流中位数。

## 十、二分 bisect

```python
import bisect
```

| 函数 | 作用 | 用法 | 时间复杂度 |
|---|---|---|---|
| `bisect_left` | 找第一个 `>= x` 的位置 | `bisect.bisect_left(nums, x)` | `O(log n)` |
| `bisect_right` | 找第一个 `> x` 的位置 | `bisect.bisect_right(nums, x)` | `O(log n)` |
| `insort` | 插入并保持有序 | `bisect.insort(nums, x)` | `O(n)` |

注意：二分要求数组已经有序。

```python
i = bisect.bisect_left(nums, target)
if i < len(nums) and nums[i] == target:
    print("找到了")
```

## 十一、计数器 Counter

```python
from collections import Counter
```

| 操作 | 作用 | 用法 | 时间复杂度 |
|---|---|---|---|
| 计数 | 统计出现次数 | `Counter(nums)` | `O(n)` |
| 取次数 | 获取某元素次数 | `cnt[x]` | `O(1)` |
| 最常见元素 | 取出现最多的元素 | `cnt.most_common(k)` | 约 `O(n log k)` |

常见写法：

```python
cnt = Counter("aabbc")
print(cnt["a"])  # 2
```

字母异位词判断：

```python
Counter(s) == Counter(t)
```

## 十二、默认字典 defaultdict

```python
from collections import defaultdict
```

常见用法：

```python
groups = defaultdict(list)
for word in strs:
    key = "".join(sorted(word))
    groups[key].append(word)
```

复杂度：

| 操作 | 时间复杂度 |
|---|---|
| 访问/插入 key | 平均 `O(1)` |
| 遍历所有元素 | `O(n)` |

适合：分组、建图、计数。

## 十三、数学常用函数

```python
import math
```

| 函数 | 作用 | 用法 | 复杂度 |
|---|---|---|---|
| `math.sqrt(x)` | 平方根 | `math.sqrt(9)` | `O(1)` |
| `math.isqrt(x)` | 整数平方根 | `math.isqrt(10)` | 接近 `O(1)` |
| `math.gcd(a, b)` | 最大公约数 | `math.gcd(12, 18)` | `O(log min(a,b))` |
| `math.lcm(a, b)` | 最小公倍数 | `math.lcm(12, 18)` | `O(log min(a,b))` |
| `math.ceil(x)` | 向上取整 | `math.ceil(3.2)` | `O(1)` |
| `math.floor(x)` | 向下取整 | `math.floor(3.8)` | `O(1)` |

常见写法：

```python
# 向上整除
ans = (a + b - 1) // b
```

## 十四、常见输入写法

笔试平台常见读取：

```python
n = int(input())
nums = list(map(int, input().split()))
```

多行输入：

```python
n = int(input())
arr = []
for _ in range(n):
    arr.append(input().strip())
```

快速输入：

```python
import sys
input = sys.stdin.readline
```

读取全部输入：

```python
import sys
data = sys.stdin.read().split()
```

## 十五、常见复杂度速记

| 场景 | 常见复杂度 |
|---|---|
| 一次遍历 | `O(n)` |
| 双重循环 | `O(n^2)` |
| 排序 | `O(n log n)` |
| 哈希表查找 | 平均 `O(1)` |
| 二分查找 | `O(log n)` |
| 堆插入/删除 | `O(log n)` |
| BFS/DFS 图遍历 | `O(V + E)` |
| 字符串排序作为 key | `O(k log k)` |
| 26 字母计数作为 key | `O(k)` |

## 十六、做题时的选择建议

| 需求 | 推荐工具 |
|---|---|
| 快速查找某个数是否出现 | `set` |
| 记录数字对应下标 | `dict` |
| 统计出现次数 | `dict` 或 `Counter` |
| 按类别分组 | `defaultdict(list)` |
| 后进先出 | `list` 当栈 |
| 先进先出 | `deque` |
| 求 Top K | `heapq` |
| 有序数组查找位置 | `bisect` |
| 字符串异位词分组 | 排序 key 或 26 字母计数 key |

