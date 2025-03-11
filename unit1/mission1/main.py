print('Hello Mars')

try:
    with open('mission_computer_main.log', 'r') as f:
        lines = f.readlines()
        lines.reverse()
        
    for i in lines:
        print(i)
        
    with open('issue.txt', 'w') as f:
        for i in range(3):
            f.write(lines[i])
            
except Exception as e:
    print(e)