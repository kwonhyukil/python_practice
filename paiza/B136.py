N, H, W = map(int,input().split())
sy, sx = map(int,input().split())
s = input()

choco_map = []
for i in range(H):
    choco_map.append(list(map(int, input().split())))

directions = {
    'F' : (-1, 0),
    'B' : (1, 0),
    'L' : (0, -1),
    'R' : (0, 1)
}

y, x = sy - 1, sx -1

visited = set()
visited.add((y, x))
result = []

for mov in s:
    dy, dx = directions[mov]
    ny, nx = y + dy , x + dx

    if 0 <= ny < H and 0 <= nx <= W:
        if (ny, nx) not in visited:
            visited.add((ny, nx))
            result.append(choco_map[ny][nx])
            y, x = ny, nx
        else:
            continue

for choco in result:
    print(choco)