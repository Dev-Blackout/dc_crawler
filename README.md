# dc_crawler
python 기반의 웹 크롤러입니다.  
default : dcinside.com  
requirements : `requests, bs4`
## Reference
1. 다운로드 : https://github.com/Dev-Blackout/dc_crawler/releases
2. requests, bs4 설치(cmd.exe)  
python : https://www.python.org/downloads/  
```
pip install --upgrade requests
pip install --upgrade bs4
```
3. 프로그램 실행 
```
Gallery ID : # 갤러리 아이디 입력
Types = (정식:1 마이너:2 미니:3) # 갤러리 타입
Gallery Type : # 갤러리 타입 입력
Gallery Name = # 갤러리 이름 출력
First Page : # 시작 페이지 입력
Last Page : # 종료 페이지 입력
Processing Page = 1/10 # 작업 현황 표시
File Path = C:\Users\Administrator\Desktop # 파일 경로 출력
Saving File = 갤러리-yyyy_mm_dd-hh_mm # 파일 이름 출력
End Of Process # 작업 종료
```
## Output Data Example
```
총 글수: 500
랭킹 닉네임    글  지분(%)
1	ㅇㅇ(uid_1)	29	5.80
2	name_1(uid_2)	16	3.20
3	ㅇㅇ(39.7)	14	2.80
4	ㅇㅇ(223.62)	14	2.80
5	name_2(uid_3)	13	2.60
... 
```
## Others
- v1.1 title을 포함한 데이터를 .csv 파일로 output하는 코드 추가 예정
