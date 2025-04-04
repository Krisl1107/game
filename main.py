import random
import local as lcl


def student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e):
    theory = th + a
    tasks = tsks + b
    luck = lk + c
    teacher = tchr + d
    condition = cnd + e
    print("theory=", theory,
          "tasks=", tasks,
          "luck=", luck,
          "teacher=", teacher,
          "condition=", condition)
    return student_1


def student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e):
    theory = th + a
    tasks = tsks + b
    luck = lk + c
    teacher = tchr + d
    condition = cnd + e
    print("theory=", theory,
          "tasks=", tasks,
          "luck=", luck,
          "teacher=", teacher,
          "condition=", condition)
    return student_2


def student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e):
    theory = th + a
    tasks = tsks + b
    luck = lk + c
    teacher = tchr + d
    condition = cnd + e
    print("theory=", theory,
          "tasks=", tasks,
          "luck=", luck,
          "teacher=", teacher,
          "condition=", condition)
    return student_3


def day_1():
    print(f"{lcl.INTRODUCTION_DAY_1}")
    print(f"{lcl.MANIUAL_DAY_1}")
    cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases)
    match m:
        case 1:
            e = 90
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_1}")
        case 2:
            e = -90
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_2}")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print(f"{lcl.LUCK_R_1}")
        case 4:
            print(f"{THEORY_R_1}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -80
            d = -60
            a, b, e = (0,) * 3
            print(f"{lcl.LUCK_R_2}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_1}")
        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_2}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{THEORY_R_2}")
        case 9:
            d = 90
            a, b, c, e = (0,) * 4
            print(f"{LECTURER_R_1}")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print(f"{LECTURER_R_2}")

    k = int(input(""))
    match k:
        case 1:
            student_1(500, 500, 500, 500, 500, a, b, c, d, e)
            th = 500 + a
            tsks = 500 + b
            lk = 500 + c
            tchr = 500 + d
            cnd = 500 + e
        case 2:
            student_2(500, 500, 500, 500, 500, a, b, c, d, e)
            th = 500 + a
            tsks = 500 + b
            lk = 500 + c
            tchr = 500 + d
            cnd = 500 + e
        case 3:
            student_3(500, 500, 500, 500, 500, a, b, c, d, e)
            th = 500 + a
            tsks = 500 + b
            lk = 500 + c
            tchr = 500 + d
            cnd = 500 + e
    cases_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases_1)
    match m:
        case 1:
            e = 80
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_3}")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_4}")
        case 3:
            c = 100
            e = 80
            a, b, d = (0,) * 3
            print(f"{lcl.LUCK_R_3}")
        case 4:
            print(f"{THEORY_R_3}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -80
            a, b, d, e = (0,) * 4
            print(f"{lcl.LUCK_R_4}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_3}")
        case 7:
            b = - 70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_2}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{THEORY_R_4}")
        case 9:
            d = 90
            a, b, c, e = (0,) * 4
            print(f"{LECTURER_R_3}")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print(f"{LECTURER_R_4}")
    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    cases_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases_2)
    match m:
        case 1:
            e = 80
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_5}")
        case 2:
            e = -80
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_6}")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print(f"{lcl.LUCK_R_1}")
        case 4:
            print(f"{lcl.THEORY_R_1}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -100
            a, b, d, e = (0,) * 4
            print(f"{lcl.LUCK_R_5}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_1}")
        case 7:
            b = -80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_2}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{lcl.THEORY_R_2}")
        case 9:
            d = 90
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_4}")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_5}")
    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    cases_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases_3)
    match m:
        case 1:
            e = 70
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_1}")
        case 2:
            e = -70
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_2}")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print(f"{lcl.LUCK_R_1}")
        case 4:
            print(f"{lcl.THEORY_R_1}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -80
            d = -70
            a, b, e = (0,) * 3
            print(f"{lcl.LUCK_R_2}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_1}")
        case 7:
            b = - 70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_2}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{lcl.THEORY_R_4}")
        case 9:
            d = 70
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_1}")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_2}")
    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e

    cases_4 = [1, 2, 3, 4, 5]
    m = random.choice(cases_4)
    match m:
        case 1:
            print(f"{lcl.RESULT_D1_1}")
            awns=int(input())
            match awns:
                case 1:
                 e = -80
                 b = -70
                 a, c, d = (0,) * 3
                 print(f"{lcl.DEPENDENT_1}")
                case 2:
                 b = 70
                 a, c, d, e = (0,) * 4
                 print(f"{lcl.RESULT_D1_2}")
        case 2:
            print(f"{lcl.DEPENDENT_2}")
            awns=int(input())
            match awns:
                case 1:
                 a = 100
                 b = -80
                 e, c, d = (0,) * 3
                 print(f"{lcl.RESULT_D2_1}")
                case 2:
                 b = 100
                 a = -80
                 c, d, e = (0,) * 3
                 print(f"{lcl.RESULT_D2_2}")
                case 3:
                 b = 70
                 a = 70
                 c, d, e = (0,) * 3
                 print(f"{lcl.RESULT_D2_3}")
        case 3:
            print(f"{lcl.DEPENDENT_3}")
            awns=int(input())
            match awns:
                case 1:
                 a = 90
                 b,e, c, d = (0,) * 4
                 print(f"{lcl.RESULT_D3_1}")
                case 2:
                 a = -100
                 c, d, e,b = (0,) * 4
                 print(f"{lcl.RESULT_D3_2}")
        case 4:
            print(f"{lcl.DEPENDENT_4}")
            awns=int(input())
            match awns:
                case 1:
                 a = 100
                 e = -120
                 b, c, d = (0,) * 3
                 print(f"{lcl.RESULT_D4_1}")
                case 2:
                 a, c, d, e,b = (0,) * 5
                 print(f"{lcl.RESULT_D4_2}")
        case 5:
            print(f"{lcl.DEPENDENT_5}")
            awns=int(input())
            match awns:
                case 1:
                 d = 100
                 e = -90
                 b, c, a = (0,) * 3
                 print(f"{lcl.RESULT_D5_1}")
                case 2:
                 d = -50
                 a, c, e, b = (0,) * 4
                 print(f"{lcl.RESULT_D5_2}")
    k = int(input())
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    print(f"{lcl.CONCLUSION_DAY_1} ")
    print(th, tsks, lk, tchr, cnd)


def day_2():
    print(f"{lcl.INTRODUCTION_DAY_2} ")
    print(f"{lcl.MANIUAL_DAY_2}")
    th, tsks, lk, tchr, cnd = map(int, input().split())
    cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases)
    match m:
        case 1:
            e = 50
            a, b, c, d = (0,) * 4
            print("Тебе пришла стипендия (УРАААААА, ГУЛЯЕМ)")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print("Начались магнитные бури и у тебя целыми днями "
                  "болит голова (метеозависимость - отстой)")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print("Ты переслал видео в тик токе об удачной сдаче сессии 10 друзьям"
                  "(успех обеспечен)")
        case 4:
            print("Ты уснул на тетради во время подготовки и вся теория телепортировалась в твой мозг")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            d = -60
            a, b, e, c = (0,) * 4
            print("Ты ехал на машине и попал в яму, из-за этого обрызгал прохожего,"
                  " который оказался твой преподаватель(минус реп...)")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print("Во сне пришел Демидович и передал все свои знания")

        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print("Сосед сверху каждый день включал дрип фонк и ты запомнил только его,"
                  " а решать задачи так и не научился")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print("Спал 2 часа и начал путать Бином Ньютона с меню Бургер Кинга"
                  "(хороший сон - залог успеха, а пока минус теория)")
        case 9:
            d = 50
            a, b, c, e = (0,) * 4
            print("Сегодня ты случайно оделся в такую же рубашку, как преподаватель"
                  " и при встрече он оценил твой вкус в одежде(+ уважение)")
        case 10:
            c = -60
            d = -90
            a, b, e = (0,) * 3
            print("Решил поесть, но разбил тарелку и чашку,"
                  "а это приводит к ссорам и неудачам, особенно если это"
                  " происходит перед важным событием."
                  "Поздравляю, минус отношения с преподавателем и удача")

    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c , d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    cases_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases_1)
    match m:
        case 1:
            e = 50
            a, b, c, d = (0,) * 4
            print("Питомец уснул у тебя на коленях, пока ты готовился, поднялось настроение")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print("Начались магнитные бури и у тебя целыми днями "
                  "болит голова (метеозависимость - отстой)")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print("Ты переслал видео в тик токе об удачной сдаче сессии 10 друзьям"
                  "(успех обеспечен)")
        case 4:
            print("Ты уснул на тетради во время подготовки и вся теория телепортировалась в твой мозг")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            d = -60
            a, b, c, e = (0,) * 4
            print("Ты ехал на машине и попал в яму, из-за этого обрызгал прохожего,"
                  " который оказался твой преподаватель(минус реп...)")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print("Во сне пришел Демидович и передал все свои знания")

        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print("Сосед сверху каждый день включал дрип фонк и ты запомнил только его,"
                  " а решать задачи так и не научился")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print("Спал 2 часа и начал путать Бином Ньютона с меню Бургер Кинга"
                  "(хороший сон - залог успеха, а пока минус теория)")
        case 9:
            d = 50
            a, b, c, e = (0,) * 4
            print("Сегодня ты случайно оделся в такую же рубашку, как преподаватель"
                  " и при встрече он оценил твой вкус в одежде(+ уважение)")
        case 10:
            c = -100
            d = -90
            a, b, e = (0,) * 3
            print("Решил поесть, но разбил тарелку и чашку,"
                  "а это приводит к ссорам и неудачам, особенно если это"
                  " происходит перед важным событием."
                  "Поздравляю, минус отношения с преподавателем и удача")

    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    cases_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases_2)
    match m:
        case 1:
            e = 50
            a, b, c, d = (0,) * 4
            print("Тебе пришла стипендия (УРАААААА, ГУЛЯЕМ)")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print("Дома закончился кофе, а ты зависим от него(- состояние)")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print("Ты переслал видео в тик токе об удачной сдаче сессии 10 друзьям"
                  "(успех обеспечен)")
        case 4:
            print("Ты уснул на тетради во время подготовки и вся теория телепортировалась в твой мозг")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            d = -60
            a, b, c, e = (0,) * 4
            print("Ты ехал на машине и попал в яму, из-за этого обрызгал прохожего,"
                  " который оказался твой преподаватель(минус реп...)")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print("Во сне пришел Демидович и передал все свои знания")

        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print("Сосед сверху каждый день включал дрип фонк и ты запомнил только его,"
                  " а решать задачи так и не научился")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print("Спал 2 часа и начал путать Бином Ньютона с меню Бургер Кинга"
                  "(хороший сон - залог успеха, а пока минус теория)")
        case 9:
            d = 50
            a, b, c, e = (0,) * 4
            print("Сегодня ты случайно оделся в такую же рубашку, как преподаватель"
                  " и при встрече он оценил твой вкус в одежде(+ уважение)")
        case 10:
            c = -100
            d = -90
            a, b, e = (0,) * 3
            print("Решил поесть, но разбил тарелку и чашку,"
                  "а это приводит к ссорам и неудачам, особенно если это"
                  " происходит перед важным событием."
                  "Поздравляю, минус отношения с преподавателем и удача")

    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    cases_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases_3)
    match m:
        case 1:
            e = 50
            a, b, c, d = (0,) * 4
            print("Тебе пришла стипендия (УРАААААА, ГУЛЯЕМ)")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print("Начались магнитные бури и у тебя целыми днями "
                  "болит голова (метеозависимость - отстой)")
        case 3:
            c = 100
            a, b, e, d = (0,) * 4
            print("Ты переслал видео в тик токе об удачной сдаче сессии 10 друзьям"
                  "(успех обеспечен)")
        case 4:
            print("Ты уснул на тетради во время подготовки и вся теория телепортировалась в твой мозг")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            d = -60
            a, b, c, e = (0,) * 4
            print("Ты ехал на машине и попал в яму, из-за этого обрызгал прохожего,"
                  " который оказался твой преподаватель(минус реп...)")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print("Во сне пришел Демидович и передал все свои знания")

        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print("Сосед сверху каждый день включал дрип фонк и ты запомнил только его,"
                  " а решать задачи так и не научился")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print("Спал 2 часа и начал путать Бином Ньютона с меню Бургер Кинга"
                  "(хороший сон - залог успеха, а пока минус теория)")
        case 9:
            d = 50
            a, b, c, e = (0,) * 4
            print("Сегодня ты случайно оделся в такую же рубашку, как преподаватель"
                  " и при встрече он оценил твой вкус в одежде(+ уважение)")
        case 10:
            c = -100
            d = -90
            a, b, e = (0,) * 3
            print("Решил поесть, но разбил тарелку и чашку,"
                  "а это приводит к ссорам и неудачам, особенно если это"
                  " происходит перед важным событием."
                  "Поздравляю, минус отношения с преподавателем и удача")


    cases_4 = [1, 2, 3, 4, 5]
    m = random.choice(cases_4)
    match m:
        case 1:
            print("Открыть/не открывать окно"
                  " (Введи 1, если да и 2, если нет)")
            awns=int(input())
            match awns:
                case 1:
                 e = 100
                 a, c, d, b = (0,) * 4
                 print("Открыл окно-подышал-зарядился энергией +состояние")
                case 2:
                 e = -100
                 a, c, d, b = (0,) * 4
                 print("Ты сидел в душном помещении и заболела голова - состояние")
        case 2:
            print("Идёшь спать? (Введи 1, если да и 2, если нет)")
            awns=int(input())
            match awns:
                case 1:
                 e = 100
                 b =-80
                 a, c, d = (0,) * 3
                 print("Споки ноки, но задачки ты не порешал")
                case 2:
                 print("А сейчас? (Введи 1, если да и 2, если нет)")
                 awns_1= int(input())
                 match awns_1:
                     case 1:
                      e = 80
                      a = 50
                      c, d, b = (0,) * 3
                      print("Сладких снов, ты хорошо поработал")
                     case 2:
                      print("Ну может пора? (Введи 1, если да и 2, если нет)")
                      awns_2 = int(input())
                      match awns_2:
                        case 1:
                         e=30
                         a=30
                         c, d, b = (0,) * 3
                         print("Ты уже очень устал, но хить немного поучиться удалось, спкнч ")
                        case 2:
                         e = -80
                         a = 10
                         c, d, b = (0,) * 3
                         print("Хватит уже, всё равно мозг уже не работает, иди спи!  ")
                case 3:
                 b=40
                 a=40
                 c, d, e = (0,) * 3
                 print("Баланс- хорошая тактика. Мог бы получить в 2 раза больше,"
                       " но зато ничего не потерял")
        case 3:
            print("В ночь перед экзаменом крикнуть “ХАЛЯВА ПРИДИ”?"
                  "(Введи 1, если да и 2, если нет)")
            awns=int(input())
            match awns:
                case 1:
                 c = 180
                 b, e, a, d = (0,) * 4
                 print("Красавчик, и не важно, что подумали проходие +удача")
                case 2:
                 c, d, e, b, a= (0,) * 5
                 print("Всё осталось на месте, зря ты постеснялся")
        case 4:
            print("Взять карты таро у своего одногруппника?"
                  "(Введи 1, если да и 2, если нет)")
            awns=int(input())
            match awns:
                case 1:
                 (th_1, tsks_1, lk_1,
                        tchr_1, cnd_1) = map(int, input("Введите значения с предыдущего раунда того студента,"
                                                          " у кото вы хотите взять карты").split())
                 th_2 = th_1
                 tsks_2 = tsks_1
                 lk_2= lk_1 - 100
                 tchr_2 = tchr_1
                 cnd_2 = cnd_1 + 50
                 print(th_2,tsks_2,lk_2,tchr_2,cnd_2)
                 e = 100
                 b, c, d, a = (0,) * 4
                 print("Твоё состояние улучшилось, и у твоего друга оно тоже немного улучшилось, однако, "
                       "давать другому свои карты таро- плохое дело, так что у него уменьшилась удача")
                case 2:
                 a, c, d, e, b = (0,) * 5
                 print("Ничего страшного, твои показатели остались прежними")
        case 5:
            print("Хочешь отправить тикток другу?" "(Введи 1, если да и 2, если нет)")
            awns=int(input())
            match awns:
             case 1:
              (th_1, tsks_1, lk_1,
               tchr_1, cnd_1) = map(int, input("Введите значения с предыдущего раунда того студента,"
                                             " кому вы хотите отправить тикток").split())
              th_2 = th_1
              tsks_2 = tsks_1
              lk_2 = lk_1 - 150
              tchr_2 = tchr_1
              cnd_2 = cnd_1
              print(th_2, tsks_2, lk_2, tchr_2, cnd_2)
              e = 30
              b, c, d, a = (0,) * 4
              print("Твоё состояние немного улучшилось, потому что он посмотрел твой тикток."
                  "В этом тиктоке на него прочитали "
                  "заклинание на неудачу и она у него снизилась ")
        case 2:
            e = -100
            c, d, a, b = (0,) * 4
            print("Ты стал загоняться, что вы поссоритесь из за вашего спора,"
                  " а ты ещё и так с ними потупаешь, даже тикток не отправил, "
                  "твоё состояние ухудшилось")
    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    cases_5 = [1, 2, 3, 4, 5]
    m = random.choice(cases_5)
    match m:
        case 1:
            print("На консультации ты можешь изъявить желание выйти к доске, "
                  "тогда будет + респект от преподавателя, "
                  "однако у этого может быть последствия…Готов?"
                  " (Введи 1, если да и 2, если нет)")
            awns = int(input())
            match awns:
                case 1:
                    b = -100
                    c= 150
                    a, e, d = (0,) * 3
                    print("Ты вышел к доске и получил жёсткий респект от преподавателя, "
                          "но окончательно запутался, как решать такой тип задач")
                case 2:
                    a, c, d, b,e = (0,) * 5
                    print("Ну и сиди дальше, прохлаждайся, ничего не поменялось")
        case 2:
            print("Можешь попробовать скинуть в группу мем, однако"
                  " это может как понравится, так и не понравится преподавателю."
                  " Рискнёшь? (Введи 1, если да и 2, если нет)")
            awns = int(input())
            match awns:
                case 1:
                    n=[1,2]
                    n_1=random.choice(n)
                    match n_1:
                        case 1:
                          d = -100
                          a, c, b, e = (0,) * 4
                          print("Тебе не повезло и он не оценил")
                        case 2:
                          d = 100
                          a, c, b, e = (0,) * 4
                          print("Тебе повезло и он оценил")
                case 2:
                    a, c, b, e, d = (0,) * 5
                    print("Ничего не поменялось, а мог бы попробовать")

        case 3:
            print("Поставить себе цель по SMART?"
                  "(Введи 1, если да и 2, если нет)")
            awns = int(input())
            match awns:
                case 1:
                    a = 100
                    b, e, c, d = (0,) * 4
                    print("Ты четко видишь свою цель и путь к ней +теория")
                case 2:
                    a = -100
                    c, d, e, b = (0,) * 4
                    print("Ты мечешься от теме к теме и отдаляешься от цели -теория")
        case 4:
            print("Друг попросил тебя объяснить ему теорию. Объяснишь?"
                  "(Введи 1, если да и 2, если нет)")
            awns = int(input())
            match awns:
                case 1:
                    (th_1, tsks_1, lk_1,
                     tchr_1, cnd_1) = map(int, input("Введите значения с предыдущего раунда того студента,").split())
                    th_2= th_1+ 100
                    tsks_2 = tsks_1
                    lk_2 = lk_1
                    tchr_2 = tchr_1
                    cnd_2 = cnd_1 + 50
                    print(th_2, tsks_2, lk_2, tchr_2, cnd_2)
                    a = 80
                    e= 80
                    b, c, d = (0,) * 3
                    print("Ты лучше запомнил теорию, друг понял. +теория у обоих и +состояние")
                case 2:
                    (th_1, tsks_1, lk_1,
                     tchr_1, cnd_1) = map(int, input("Введите значения с предыдущего раунда того студента,").split())
                    th_2 = th_1 - 80
                    tsks_2 = tsks_1
                    lk_2 = lk_1
                    tchr_2 = tchr_1
                    cnd_2 = cnd_1
                    print(th_2, tsks_2, lk_2, tchr_2, cnd_2)
                    e = -100
                    b, c, d, a = (0,) * 4
                    print("Вы не помогли друг другу. "
                          "У тебя минус состояние, у друга минус теория")
        case 5:
            print("Посмотреть мотивационный ролик?" "(Введи 1, если да и 2, если нет)")
            awns = int(input())
            match awns:
                case 1:
                    b = 80
                    a, c, d, e = (0,) * 4
                    print("Ты набрался мотивации, задачи стали решаться как по маслу")
                case 2:
                    e = -80
                    c, d, a, b = (0,) * 4
                    print("Не посмотрел и пожалел об этом, состояние уменьшилось")
    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
          student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
          th = th + a
          tsks = tsks + b
          lk = lk + c
          tchr = tchr + d
          cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    print("Закончился второй день, завтра уже экзамен, "
          "хоть выспись сегодня, завтра грандиозный день."
          "Переходим к следующей команде(нажми enter,чтобы продолжить)")
    print(th, tsks, lk, tchr, cnd)


def day_3():
    print(f"{lcl.INTRODUCTION_DAY_3}")
    th, tsks, lk, tchr, cnd = map(int, input().split())
    cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases)
    match m:
        case 1:
            e = 50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_11}")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_12}"
                  "(сигма сигма боой, сигма бой, сигма бой...")
        case 3:
            c = 100
            e = 40
            a, b, d = (0,) * 3
            print(f"{lcl.LUCK_R_9}")
        case 4:
            print(f"{lcl.THEORY_R_8}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -80
            a, b, d, e = (0,) * 4
            print(f"{lcl.LUCK_R_10}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_8}")
        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_7}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{lcl.THEORY_R_9}")
        case 9:
            d = 50
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_9}")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_10}")

    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    cases_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases_1)
    match m:
        case 1:
            e = 50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITIONING_R_13}")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITIONING_R_14}")
        case 3:
            c = 100
            e = 40
            a, b, d = (0,) * 3
            print(f"{lcl.LUCK_R_11}")
        case 4:
            print(f"{lcl.THEORY_R_10}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -80
            a, b, d, e = (0,) * 4
            print(f"{lcl.LUCK_R_10}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_8}ач")
        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_9}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{lcl.THEORY_R_9}")
        case 9:
            d = 50
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_9}")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_11}")

    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    cases_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases_2)
    match m:
        case 1:
            e = 50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_11}")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_12}")
        case 3:
            c = 100
            a, b, d, e = (0,) * 4
            print(f"{lcl.LUCK_R_12}")
        case 4:
            print(f"{lcl.THEORY_R_11}")
            a = 80
            c = 80
            e, b, d = (0,) * 3
        case 5:
            c = -80
            a, b, d, e = (0,) * 4
            print(f"{lcl.LUCK_R_10}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_10}")
        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_7}")
        case 8:
            a = -80
            b = -80
            e, c, d = (0,) * 3
            print(f"{lcl.TASKS_R_11}")
        case 9:
            d = 50
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_9}")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_10}")

    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    cases_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = random.choice(cases_3)
    match m:
        case 1:
            e = 50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_11}")
        case 2:
            e = -50
            a, b, c, d = (0,) * 4
            print(f"{lcl.CONDITION_R_12}")
        case 3:
            c = 100
            e = 40
            a, b, d = (0,) * 3
            print(f"{lcl.LUCK_R_9}")
        case 4:
            print(f"{lcl.THEORY_R_8}")
            a = 80
            e, b, c, d = (0,) * 4
        case 5:
            c = -80
            a, b, d, e = (0,) * 4
            print(f"{lcl.LUCK_R_10}")
        case 6:
            b = 80
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_8}")
        case 7:
            b = -70
            a, e, c, d = (0,) * 4
            print(f"{lcl.TASKS_R_7}")
        case 8:
            a = -80
            e, b, c, d = (0,) * 4
            print(f"{lcl.THEORY_R_9}")
        case 9:
            d = 50
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_9}")
        case 10:
            d = -90
            a, b, c, e = (0,) * 4
            print(f"{lcl.LECTURER_R_10}")

    k = int(input(""))
    match k:
        case 1:
            student_1(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 2:
            student_2(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
        case 3:
            student_3(th, tsks, lk, tchr, cnd, a, b, c, d, e)
            th = th + a
            tsks = tsks + b
            lk = lk + c
            tchr = tchr + d
            cnd = cnd + e
    print(f"{lcl.EXAM_END}")
    print(th, tsks, lk, tchr, cnd)
def win():
    th, tsks, lk, tchr, cnd \
        = map(int, input(f"{lcl.RESULTS_1}").split())
    sum_1 = th + tsks + lk + tchr + cnd
    print(f"{lcl.TOTAL}: {sum_1}")
    th, tsks, lk, tchr, cnd \
        = map(int, input(f"{lcl.RESULTS_2}").split())
    sum_2 = th + tsks + lk + tchr + cnd
    print(f"{lcl.TOTAL}: {sum_2}")
    th, tsks, lk, tchr, cnd \
        = map(int, input(f"{lcl.RESULTS_3}").split())
    sum_3 = th + tsks + lk + tchr + cnd
    print(f"{lcl.TOTAL}: {sum_3}")
    if sum_1 <= 0:
        if sum_2 <= 0:
            if sum_3 <= 0:
                print(f"{lcl.LOSER_123}")
            else:
                print(f"{lcl.LOSER_12}")
                print(f"{lcl.WINNER_3}")
        elif sum_2 > sum_3 and sum_3 > 0:
            print(f"{lcl.LOSER_1}")
            print(f"{lcl.WINNER_2}")
            print(f"{lcl.SILVER_3}")
        elif sum_2 < sum_3 and sum_3 > 0:
            print(f"{lcl.LOSER_1}")
            print(f"{lcl.WINNER_3}")
            print(f"{lcl.SILVER_2}")
        elif sum_2 == sum_3:
            print(f"{lcl.LOSER_1}")
            print(f"{lcl.WINNER_23}")

        elif sum_2 <= sum_3:
            print(f"{lcl.LOSER_12}")
        else:
            print(f"{lcl.WINNER_23}")
            print(f"{lcl.WINNER_3}")

    elif sum_2 <= 0 and sum_3 <= 0:
        print(f"{lcl.LOSER_23}")
        print(f"{lcl.WINNER_1}")
    elif sum_3 <= 0 and sum_1 <= 0:
        print(f"{lcl.LOSER_13}")
        print(f"{lcl.WINNER_2}")
    if sum_1 >= sum_2 and sum_3 >= sum_2:
        print(f"{lcl.WINNER_1}")
        print(f"{lcl.SILVER_3}")
        print(f"{lcl.CUPRUM_2}")
    elif sum_1 >= sum_2 and sum_2 >= sum_3:
        print(f"{lcl.WINNER_1}")
        print(f"{lcl.SILVER_2}")
        print(f"{lcl.CUPRUM_3}")
    elif sum_2 >= sum_1 and sum_1 >= sum_3:
        print(f"{lcl.WINNER_2}")
        print(f"{lcl.SILVER_1}")
        print(f"{lcl.CUPRUM_3}")
    elif sum_2 >= sum_3 and sum_3 >= sum_2:
        print(f"{lcl.WINNER_2}")
        print(f"{lcl.SILVER_3}")
        print(f"{lcl.CUPRUM_1}")
    elif sum_3 >= sum_2 and sum_2 >= sum_1:
        print(f"{lcl.WINNER_3}")
        print(f"{lcl.SILVER_2}")
        print(f"{lcl.CUPRUM_1}")
    elif sum_3 >= sum_1 and sum_1 >= sum_2:
        print(f"{lcl.WINNER_3}")
        print(f"{lcl.SILVER_1}")
        print(f"{lcl.CUPRUM_2}")
    elif sum_1 == sum_2 and sum_1 > sum_3:
        print(f"{lcl.WINNER_12}")
        print(f"{lcl.SILVER_3}")
    elif sum_1 == sum_2 and sum_1 < sum_3:
        print(f"{lcl.WINNER_3}")
        print(f"{lcl.SILVER_1}")
        print(f"{lcl.SILVER_2}")
    elif sum_1 == sum_3 and sum_1 > sum_2:
        print(f"{lcl.WINNER_13}")
        print(f"{lcl.SILVER_2}")
    elif sum_1 == sum_2 and sum_1 < sum_3:
        print(f"{lcl.WINNER_3}")
        print(f"{lcl.SILVER_1}")
        print(f"{lcl.SILVER_2}")
    elif sum_2 == sum_3 and sum_1 < sum_3:
        print(f"{lcl.WINNER_23}")
        print(f"{lcl.SILVER_1}")
    else:
        print(f"{lcl.WINNER_123}")

def main():
    day_1()
    input()
    day_1()
    input()
    day_1()
    input()
    day_2()
    input()
    day_2()
    input()
    day_2()
    input()
    day_3()
    input()
    day_3()
    input()
    day_3()
    input()
    win()


if __name__ == '__main__':
    main()
