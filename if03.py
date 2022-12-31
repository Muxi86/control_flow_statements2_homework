def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    ans = a
    if a < b:
        if a > c:
            ans = a
    if a > b:
        if b > c:
            ans = b
    if a > c:
        if b < c:
            ans = c

    return ans

print(main(7,1,3))