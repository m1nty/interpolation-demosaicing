def cubic(p, x):
    sol = p[1] + 0.5 * x*(p[2] - p[0] + x*(2.0*p[0] - 5.0*p[1] + 4.0*p[2] - p[3] + x*(3.0*(p[1] - p[2]) + p[3] - p[0])))
    if sol<0: return 0
    elif sol>255: return 255
    else: return sol

def bicubic(p, x, y):
    interm = []
    interm.append(cubic(p[0], y))
    interm.append(cubic(p[1], y))
    interm.append(cubic(p[2], y))
    interm.append(cubic(p[3], y))
    return cubic(interm, x)

# p = [[46, 46, 46, 45],[48, 46, 48, 46],[46, 46, 46, 45],[47, 48, 47, 45]]
# print(bicubic(p, 0.5 , 0.5))