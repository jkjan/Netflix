import os
from utils import *

print("잠시만 기다려주세요...")

cosine_sim = get_cosine_similarity()

os.system('cls')

while True:
    print("-------------------------------\n"
          "Netflix 에 오신 것을 환영합니다!\n\n"
          "1 : 영화 찾기\n"
          "2 : 만든 사람들\n"
          "3 : 종료하기\n"
          "-------------------------------\n")
    try:
        command = int(input("1 ~ 3 중 하나의 값을 입력해주세요 : "))
    except ValueError:
        print("\n잘못된 입력입니다.\n")

        continue

    if command == 1:
        title = input("영화 제목을 입력해주세요 : ")

        try:
            recommended = recommend_me_similar_to(title, method=cosine_sim)
        except KeyError:
            print("\n해당 영화가 데이터에 존재하지 않습니다.\n")
            continue

        print()
        for index, movie in enumerate(recommended):
            print("%2d : %s" % (index+1, movie))
        print()

    elif command == 2:
        print("\n팀명 : Netflix\n"
              "팀장 : 진교준\n"
              "팀원 : 김정수, 성시원\n"
              "")

    elif command == 3:
        print("\n이용해 주셔서 감사합니다.\n")
        break

    else:
        print("\n잘못된 입력입니다.\n")