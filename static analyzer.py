def static_analysis(code):

    issues = []

    if "eval(" in code:
        issues.append("Avoid using eval()")

    if "==" in code and "if" not in code:
        issues.append("Possible incorrect comparison")

    if "print(" in code and "debug" in code.lower():
        issues.append("Debug print statement detected")

    return issues