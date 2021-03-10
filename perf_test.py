import timeit


def main():
    data = {'ale.lives': 5}
    print(next(iter(data.values())))
    def stmt1():
        kek = next(iter(data.values()))
    def stmt2():
        kek = data['ale.lives']
    res1 = timeit.timeit(stmt1,number=10000000)
    res2 = timeit.timeit(stmt2,number=10000000)
    res4 = timeit.timeit(stmt2,number=10000000)
    res3 = timeit.timeit(stmt1,number=10000000)
    
    print(res1, res2, res3, res4)

if __name__ == '__main__':
    main()