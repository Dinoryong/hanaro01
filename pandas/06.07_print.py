# 주석 = ctrl + /

# 좌측에 extensions 에서
# 1) korean
# 2) python
# 3) python extension
# 설치

print("hello world")
# 실행하는 방법
# 1) 우측 상단 화살표 버튼 누르고 파이썬 파일 실행 클릭
# 2) 명령 프롬프트에서 이 파일이 저장된 위치로 가서 Python prinst.py 실행
# 3) 한 줄 실행 = shift + enter

# 오라클 디비 접속
# 라이브러리 빙수 설치
# 새로운 터미널 열기 = shift+ctrl + `(backtick 기호)
# python -m pip install cx_Oracle -- upgrade
import cx_Oracle as oci
# 디비 연결
# "ID/PW@localhost:1521"
con = oci.connect("scott/tiger@localhost:1521")