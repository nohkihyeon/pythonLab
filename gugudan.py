def multi_table_2(n):
    if n==0:
        print('end')
    else:
        multi_table_2(n-1)
        print('2 * {} = {}'.format(n, 2*n))

multi_table_2(9)