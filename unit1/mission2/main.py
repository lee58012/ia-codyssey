try:   # 예외 처리
    with open('mission_computer_main.log', 'r', encoding='UTF-8') as f:    #파일 읽기
        lines = f.readlines()
        print("--------------파일 출력--------------")                                              
        print(lines)                                                       
        lst = []
        
        for line in lines[1:]:                                            # 첫번째 줄 무시
            parts = line.rstrip().split(',')                              # 콤마를 기준으로 분류
            lst.append(parts)                                             # 리스트에 분류후 추가
        print("--------------리스트 출력--------------")
        print(lst)     # 리스트 객체 출력
        
    print("--------------역순 정렬 후--------------")
    lst.sort(key=lambda x: x[0], reverse=True)                            #리스트 연순 정렬
    print(lst)                                                            #역순 정렬 후 출력
    dict_list = []
    for item in lst:
        dict_list.append({"timestamp": item[0], "event":item[1], "message":item[2]})
                                                                # 리스트를 사전 객체로 전환후 리스트에 저장
    
    with open('mission_computer_main.json', 'w') as f:                    #사전 객체를 json 파일로 저장
        f.write(str(dict_list))
    
except Exception as e:  # 예외 처리
    print(e)