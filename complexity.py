def detect_complexity(code):
    """
    Estimate time complexity based on loop patterns in the code.
    This is a simple heuristic for hackathon demonstration.
    """

    code_lower = code.lower()

    # Count occurrences of loops
    for_count = code_lower.count("for")
    while_count = code_lower.count("while")

    total_loops = for_count + while_count

    # Basic heuristic rules
    if total_loops == 0:
        return "O(1) - Constant time (no loops detected)"

    elif total_loops == 1:
        return "O(n) - Linear time (single loop detected)"

    elif total_loops == 2:
        return "O(n^2) - Quadratic time (nested loops possible)"

    elif total_loops >= 3:
        return "O(n^3) or higher - Multiple nested loops detected"

    else:
        return "Complexity could not be determined"