print('Hello Mars')  # Hello Mars 출력

try:   # 예외 처리
    with open('mission_computer_main.log', 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for i in lines:  # 문제 발생 부분 출력
            print(i)
        lines.reverse()  # 역순 정렬
    
    print("--------------역순 정렬 후--------------")
    for i in lines:  #역순 정렬 후 출력
        print(i)
        
    with open('issue.txt', 'w', encoding='UTF-8') as f:  # 문제 발생 부분을 issue.txt파일로 저장
        for i in range(3):
            f.write(lines[i])
            
except Exception as e:  # 예외 처리
    print(e)