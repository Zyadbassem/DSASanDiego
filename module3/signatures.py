def signatures(sigments: list):
    s_sigments = sorted(sigments, key= lambda x: x[1])

    points = []
    current = 0

    while current < len(s_sigments):
        point_location = s_sigments[current][1]
        points.append(point_location)
        current += 1

        while current < len(s_sigments) and s_sigments[current][0] <= point_location and point_location <= s_sigments[current][1]:
            current += 1
    
    print(len(points))
    for p in points:
        print(p, end=' ')
    print('')



def main():
    num_of_s = int(input())
    sigments = []
    for _ in range(0, num_of_s):
        curr = [int(x) for x in input().split(' ')]
        sigments.append(curr)

    signatures(sigments)

main()
