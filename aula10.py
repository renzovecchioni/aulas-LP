def fatorial(num: str)->int:
    """_summary_

    Args:
        num (int): _description_

    Returns:
        int: _description_
    """
    if num <=1:
        return 1
    return num * fatorial(num-1)

print(fatorial(9.01))