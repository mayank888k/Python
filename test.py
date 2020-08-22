if __name__ == '__main__':
    N = int(input())
    lst=[]
    for _ in range(N):
        lst.append([a,b,c] for a,b,c in input().split())
    print(lst)