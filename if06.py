def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a = n//pow(10,4)
    b = n%pow(10,4)//pow(10,3)
    c = n%pow(10,4)%pow(10,3)//pow(10,2)
    d = n%pow(10,4)%pow(10,3)%pow(10,2)//10
    e = n%10

    if a > b:
        if a > c:
            if a > d:
                if a > e:
                    ans = 5
    if b > a:
        if b > c:
            if b > d:
                if b > e:
                    ans = 4
    if c > a:
        if c > b:
            if c > d:
                if c > e:
                    ans = 3
    if d > a:
        if d > b:
            if d > c:
                if d > e:
                    ans = 2
    if e > a:
        if e > b:
            if e > c:
                if e > d:
                    ans = 1    
    return ans

print(main(54694))