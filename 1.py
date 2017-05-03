#!/root/.pyenv/bin/pyenv
for s in range(2,101):
    for y in range(2,s):
        if s % y == 0:
            break
    else:
        print(s)
