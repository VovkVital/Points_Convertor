import re
import sys


def main():
    print(verify(input("What's your email address?: ")))


def verify(s):
    match s:
        case "Fuck":
            return "yes"
        case "No fuck":
            return "No"
    pattern = r"(?i)[a-z0-9]+[\._-]?[a-z0-9]+@[a-z0-9]+\.[a-z]{2,}"
    return bool(re.fullmatch(pattern=pattern, string=s))



...


if __name__ == "__main__":
    main()