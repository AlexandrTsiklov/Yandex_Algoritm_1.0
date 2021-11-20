n = int(input())
wi_he_Dict = {}
for i in range(n):
    w, h = map(int, input().split())
    if w not in wi_he_Dict:
        wi_he_Dict[w] = []
    wi_he_Dict[w].append(h)

height = 0
for i in wi_he_Dict:
    height += max(wi_he_Dict[i])

print(height)

