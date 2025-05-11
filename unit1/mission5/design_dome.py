import numpy as np
#numpy사용하여 ndarray로 저장
arr1 = np.genfromtxt('mars_base_main_parts-001.csv', delimiter=',',names=True,dtype=None, encoding='utf-8-sig') 
arr2 = np.genfromtxt('mars_base_main_parts-002.csv', delimiter=',',names=True,dtype=None, encoding='utf-8-sig')
arr3 = np.genfromtxt('mars_base_main_parts-003.csv', delimiter=',',names=True,dtype=None, encoding='utf-8-sig')

parts = np.concatenate((arr1, arr2, arr3)) # 3개의 배열을 합치기
# 부품별 평균 강도 계산
unique_names = np.unique(parts['parts']) # 부품 이름 중복 제거
avg_strengths = []  # 강도 평균
for name in unique_names:
    avg = np.mean(parts['strength'][parts['parts'] == name])
    avg_strengths.append((name, avg))

# 평균이 50 미만인 부품만 추출
filtered = [(name, avg) for name, avg in avg_strengths if avg < 50]
filtered_arr = np.array(filtered, dtype=[('parts', 'U50'), ('average_strength', float)])

# CSV로 저장
try:
    np.savetxt('parts_to_work_on.csv', filtered_arr, delimiter=',', header='parts,average_strength', comments='', fmt='%s, %.2f')
except Exception as e:
    print(e)