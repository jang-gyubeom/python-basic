# 슬라이싱

'''
- 문자열 (또는 리스트) n 번째 인덱스에 있는 문자 (또는 데이터) 하나만 가져오기
변수명[인덱스]

- 슬라이싱
변수명[시작인덱스:종료인덱스]
종료인덱스의 경우 종료인덱스 전까지의 문자 (또는 데이터) 를 가져옴

변수명 [:인덱스]
: 처음부터 인덱스 직전까지 슬라이싱
변수명 [인덱스:]
: 인덱스부터 끝까지 슬라이싱
변수명 [:]
: 처음부터 끝까지 슬라이싱
'''

jumin = '960530-1234567'

# 인덱스
print('성별 : ' + jumin[7]) # 성별 : 1

# 슬라이싱
print('연 : ' + jumin[0:2]) # 연 : 96
print('월 : ' + jumin[2:4]) # 월 : 05
print('일 : ' + jumin[4:6]) # 일 : 30
print('생년월일 : ' + jumin[:6]) # 생년월일 : 960530
print('뒤 7자리 : ' + jumin[7:]) # 뒤 자리 : 1234567
print('뒤 7자리 (뒤에부터) : ' + jumin[-7:]) # 뒤 7자리 (뒤에부터) : 1234567