try:   # 예외 처리
    with open('mission_computer_main.log', 'r', encoding='UTF-8') as f:    #파일 읽기
        lines = f.readlines()                                              
        print(lines)                                                       #출력
        lst = []
        
        for line in lines[1:]:                                             # 첫번째 줄 무시
            parts = line.rstrip().split(',')                               # 콤마를 기준으로 분류
            lst.append([parts[0],parts[2]])                                # 리스트에 분류후 추가
        print(lst)     # 리스트 객체 출력
        
    print("--------------역순 정렬 후--------------")
    lst.sort(key=lambda x: x[0], reverse=True)                            #리스트 연순 정렬
    print(lst)                                                            #역순 정렬 후 출력
    
    my_dict = {item[0]: item[1] for item in lst}                          # 리스트를 사전 객체로 전환
    
    
    with open('mission_computer_main.json', 'w') as f:                    #사전 객체를 json 파일로 저장
        f.write(str(my_dict))

    
except Exception as e:  # 예외 처리
    print(e)