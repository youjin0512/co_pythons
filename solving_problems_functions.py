# 문제 출력/사용자 입력 받는 function
def problems_main(questions) :      # hint #탈자 추가 : problems_m => problems_main 
    
    #list_problems 에서 질문에만 번호 부여하기 위해 인덱스 홀수 짝수로 나눔
    problems_first = questions[1], questions[3], questions[5], questions[7]
    problems_second = questions[0], questions[2], questions[4], questions[6]
    
    # 답을 저장할 빈 리스트
    list_results = []

    #각 그룹에서 질문 가져옴
    for question in [questions]:       # hint : []사이 questions 추가
        question_a = problems_second[question]
        question_b = problems_first[question]
        
        #질문 표시
        print("{}. {}".format(question + 1, question_a))
        print("{}".format(question_b))
        
        #답변 input
        question_result = input("-정답 : ")
        print("")
        
        #리스트에 결과 추가
        list_results.append(question_result)
        
        #답을 정수로 변환하고 결과 반환
        input_temp = [int(i) for i in list_results]

    # 점수 합계/학점 출력 function
    def total_responses(score):

        # 문제 당 점수
        score_temp = [10, 15, 10, 5]
        score = 0

        # 점수 합계
        for i in range(len(input_temp)):
            if list_corrects[i] == input_temp[i]:
                score += score_temp[i]

        # 학점 기준 : 
        # A : 30 이상, B : 20 점 이상,  F : 20점 미만 
        if score >= 30:
            score_result = "A"
        elif score >= 20:       # hint : else => elif
            score_result = "B"
        else:
            score_result = "F"
        
        # 결과 출력
        print("—----- 결과 —-------------")
        print("응답한 내용 : 1번 {}, 2번 {}, 3번 {}, 4번 {}".format(input_temp[0], input_temp[1], input_temp[2], input_temp[3]))
        print("당신 응답 합계 : {}점".format(score))
        print("학점은 {} 입니다.".format(score_result))
        return 
    
    return total_responses(input_temp)
    
if __name__ == "__main__":
    # 출제 문제
    list_problems = [
            'Python에서 변수를 선언하는 방법은? (점수: 10점)',
            '1) var name 2) name = value 3) set name 4) name == value',    # 누락된 답항 추가
            'Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)',
            '1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다', 
            'Python에서 조건문을 작성하는 방법은? (점수: 10점)', 
            '1) if-else, 2) for-in, 3) while, 4) def',
            'Python에서 함수를 정의하는 방법은? (점수: 5점)', 
            '1) class, 2) def, 3) import, 4) return'
    ]       # hint
    # 문제 당 정답
    list_corrects = [2, 4, 4, 3 ]    # hint : [] 사이 정답 추가


    problems_main(list_problems) 

