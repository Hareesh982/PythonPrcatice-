# Given the participants' score sheet for your University Sports Day, you are required to
# find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m = max(arr)
    s = None

    for num in arr:
        if num == m:
            pass
        elif s == None:
            s = num
        elif num > s:
            s = num

    print(s)


# *****************SAMPLE_INPUT******************

# 5
# 2 3 6 6 5

# ******************OUTPUT******************

# 5
