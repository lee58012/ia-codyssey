try:   # 예외 처리
    with open('./Mars_Base_Inventory_List.csv', 'r', encoding='UTF-8') as f:    #파일 읽기
        lines = f.readlines()
        print("--------------파일 출력--------------")                  #파일 출력
        print(lines)
        lst = []                                            
        for line in lines[1:]:                                            # 첫번째 줄 무시
            parts = line.rstrip().split(',')                              # 콤마를 기준으로 분류
            lst.append(parts)                           
        print("--------------역순 정렬 후--------------")
        lst.sort(key=lambda x:x[4], reverse=True)                             #인화성 높은순으로 정렬 
        print(lst)
        print("--------------인화성 0.7이상--------------")
        Danger_list=[]
        for i in lst:
            if float(i[4]) >= 0.7:              #비교를 위한 형변환
                print(i)                        #인화성 0.7이상이면 출력
                Danger_list.append(i)
    with open('./Mars_Base_Inventory_danger.csv','w',encoding='UTF-8') as f:
        for i in Danger_list:                        #인화성 지수가 0.7 이상되는 목록을 저장
            for j in range(len(i)):                  #반복문으로 리스트 안에 있는 데이터들을 하나씩 저장
                f.write(str(i[j]))
                if(j<len(i)-1):
                    f.write(",")                
            f.write("\n")      
    
except Exception as e:  # 예외 처리
    print(e)