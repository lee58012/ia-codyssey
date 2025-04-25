material = ''   # 전역변수 선언
diameter = 0
thickness = 0
area = 0
weight = 0

m_list=['유리', '알루미늄', '탄소강']
def  sphere_area(material='유리',diameter=0,thickness=1): #함수 기본값 설정
    global area, weight #전역변수 선언
    r=(diameter//2)*100 # 반지름 구하고 cm로 변환
    area=2*3.14*r**2  #면적 구하기
    if material == '유리':
        weight = 2.4*area*0.001*thickness*0.3721     #kg으로 변환후 화성 중력으로 변환
    elif material == '알루미늄':
        weight = 2.7 *area*0.001*thickness*0.3721
    elif material == '탄소강':
        weight = 7.85*area*0.001*thickness*0.3721
    return material,diameter,area

while True:
    while True:
        material = input('재질(유리, 알루미늄, 탄소강)을 입력하시오.(기본값:유리) (종료 입력 시 종료)\n')
        if material == '종료':
            exit()
        elif material == '':
            material='유리'
            break
        elif material in m_list:
            break
        else:
            print("공백 또는 셋중 하나를 입력해 주세요.")             
    while True:
            diameter = input('지름(m)를 입력하시오 (종료 입력 시 종료)\n')
            if diameter == '종료':
                exit()
            try:
                diameter = float(diameter)  # 지름 값을 실수로 변환
                if diameter == 0:
                    print('지름의 값이 0이 되면 안됩니다.')
                else:
                    break
            except:
                print('실수 값을 입력해주세요')
    while True:
            thickness = input('두께(cm)를 입력하시오 (종료 입력 시 종료)\n')
            if thickness == '종료':
                exit()
            try:
                thickness = float(thickness)  # 두께 값을 실수로 변환
                if thickness == 0:
                    print('두께의 값이 0이 되면 안됩니다.')
                else:
                    break
            except:
                print('실수 값을 입력해주세요')
            
    material,diameter,area = sphere_area(material,diameter)
    print(f'재질 =⇒ {material}, 지름 =⇒ {diameter:.3f}, 두께 =⇒ {thickness:.3f}, 면적 =⇒ {area:.3f}, 무게 =⇒ {weight:.3f} kg')
            


