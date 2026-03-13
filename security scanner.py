def run_security_scan(code):

    warnings = []

    if "eval(" in code:
        warnings.append("Security risk: eval() detected")

    if "exec(" in code:
        warnings.append("Security risk: exec() detected")

    if "os.system" in code:
        warnings.append("Possible command injection")

    return warnings