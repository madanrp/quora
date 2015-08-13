

n, k = map(int, raw_input().split())
a = map(int, raw_input().split())

increasing = [[0]*n for i in [1,2]]
decreasing = [[0]*n for i in [1,2]]

for i in range(0, n):
    increasing[0][i] = 1 + (increasing[0][i-1] if (i and (a[i] >= a[i-1])) else 0)
    decreasing[0][i] = 1 + (decreasing[0][i-1] if (i and (a[i] <= a[i-1])) else 0)

for i in range(n-1, -1, -1):
    increasing[1][i] = 1 + (increasing[1][i+1] if ((i < n-1) and (a[i] >= a[i+1])) else 0)
    decreasing[1][i] = 1 + (decreasing[1][i+1] if ((i < n-1) and (a[i] <= a[i+1])) else 0)


num_inc = 0
num_dec = 0

for i in range(0, k-1):
    num_inc += increasing[0][i]
    num_dec += decreasing[0][i]


for i in range(k-1, n):
    num_inc += min([k, increasing[0][i]])
    num_dec += min([k, decreasing[0][i]])

    print (num_inc - num_dec)
    num_inc -= min([k, decreasing[1][i-k+1]])
    num_dec -= min([k, increasing[1][i-k+1]])



