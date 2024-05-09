## Приклад сортування:

### Shuffled sequence of range(10):
        Time of merge_sort          : 0.0008109999999999992
        Time of insertion_sort      : 0.00027054099999999914
        Time of sorted              : 2.016700000000149e-05

### Shuffled sequence of range(100):
        Time of merge_sort          : 0.010626041999999999
        Time of insertion_sort      : 0.015593958999999998
        Time of sorted              : 0.0002197089999999985

### Shuffled sequence of range(1000):
        Time of merge_sort          : 0.138523166
        Time of insertion_sort      : 1.48935675
        Time of sorted              : 0.0032691670000000173

### Shuffled sequence of range(10000):
        Time of merge_sort          : 1.7488564580000001
        Time of insertion_sort      : 163.09669116700002
        Time of sorted              : 0.06993741700000555

## Висновки
Найкращій алгоритм ––  timsort (sorted) : складність О(n•log(n))


Найгірший алгоритм ––  сортування вставками (insertion_sort) : складність О(n^2)


З іншого боку для малої кількості елементів сортування вставками (insertion_sort) працює кращє ніж сортування злиттям (merge_sort) : складність О(n•log(n))
