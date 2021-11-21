button_count = int(input())
buttons_params = list(map(int, input().split()))
button_MaxPressCount_dict = {}
for i in range(button_count):
    button_MaxPressCount_dict[i + 1] = buttons_params[i]

press_count = int(input())
buttons_line = list(map(int, input().split()))

button_PressCount_dict = {}
for i in buttons_line:
    if i not in button_PressCount_dict:
        button_PressCount_dict[i] = 0
    button_PressCount_dict[i] += 1

for i in button_MaxPressCount_dict:
    if button_PressCount_dict[i] > button_MaxPressCount_dict[i]:
        print('YES')
    else:
        print('NO')  #





