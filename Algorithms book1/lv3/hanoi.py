def print_pillar(pillar):
    for pil in pillar:
        print(f"{pil!r:15}", end='\t\t')
    print()
    return 0


def make_pillar(num):
    pillar = [[] for _ in range(3)]
    for i in range(num, 0, -1):
        pillar[0].append(i)
    return pillar


def hanoi(pillar, n, src_pil, dest_pil, tmp_pil):
    if n == 1:
        tmp = pillar[src_pil - 1].pop()
        pillar[dest_pil - 1].append(tmp)
        print_pillar(pillar)
    else:
        hanoi(pillar, n - 1, src_pil, tmp_pil, dest_pil)
        tmp = pillar[src_pil - 1].pop()
        pillar[dest_pil - 1].append(tmp)
        print_pillar(pillar)
        hanoi(pillar, n - 1, tmp_pil, dest_pil, src_pil)


def solve(num):
    pillar = make_pillar(num)
    print_pillar(pillar)
    hanoi(pillar, num, 1, 3, 2)


def main():
    num = int(input("num of hanoi : "))
    solve(num)

    return 0


main()
