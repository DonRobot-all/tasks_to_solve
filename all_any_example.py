x = [True, True, False]
if any(x):
    print("Как минимум один True")

if all(x):
    print("Ни одного False")

if any(x) and not all(x):
    print("Как минимум один True и один False")