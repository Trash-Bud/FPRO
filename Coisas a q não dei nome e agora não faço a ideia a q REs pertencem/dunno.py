n = int(input())
n_Str = str(n)

for i in range (0, len(n_Str) + 1):
    if i == 0 or i == len(n_Str):
        in_l = abs(int(line(n_Str, 1)) - int(line(n_Str, 0)))
        in_r = abs(int(line(n_Str, i - 1)) - int(line(n_Str, i)))
        if in_l != 1:
            print(Not a looping number)
            break
        else:
            if i = len(n_Str):
                print(Looping number)
            else:
            pass
    elif i > 0:
        in_l = abs(int(line(n_Str, i + 1)) - int(line(n_Str, i)))
        in_r = abs(int(line(n_Str, i)) - int(line(n_Str, i - 1)))
        if in_l != 1 or in_r != 1:
            print(Not a looping number)
            break
        else:
            pass
