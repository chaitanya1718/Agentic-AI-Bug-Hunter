import difflib

def find_bug_lines(code, correct_code):

    code_lines = code.split("\n")
    correct_lines = correct_code.split("\n")

    diff = difflib.ndiff(code_lines, correct_lines)

    bug_lines = []

    line_no = 1

    for line in diff:

        if line.startswith("- "):
            bug_lines.append(line_no)

        if not line.startswith("+ "):
            line_no += 1

    return bug_lines