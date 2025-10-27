def maxArea(h):
    l, r, m = 0, len(h) - 1, 0
    while l < r:
        m = max(m, (r - l) * min(h[l], h[r]))
        if h[l] < h[r]: l += 1
        else: r -= 1
    return m

print(maxArea([1,8,6,2,5,4,8,3,7]))
