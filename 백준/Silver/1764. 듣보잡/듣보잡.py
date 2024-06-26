n, m = map(int, input().split())

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input().strip())

for _ in range(m):
    m_set.add(input().strip())

# 두 집합의 교집합 찾기
common_elements = n_set & m_set

# 출력
print(len(common_elements))
for name in sorted(common_elements):
    print(name)