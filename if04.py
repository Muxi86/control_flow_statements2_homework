def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    ans = a
    
    if a > b:
        ans = a
    else:
        ans = b
    if a == b:
        ans = 0
    return ans

print(main(5,5))