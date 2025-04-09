#직위 입력
jik=input("직위...")
# 연봉 입력
don = int(input("연봉입력..."))

#직위가 사원이면서 연봉이 10원 이상이면 직위와 연봉을 출력
if jik == "사원" and don >= 10:
    print("직위는 {}이고, 연봉은 {}이다".format(jik, don))
