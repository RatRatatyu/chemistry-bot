#function for checking user answer
def answer_checker(answer, question_num):
    match question_num:
        case 0:
            if answer in ["водород", "h"]:
                return "Правильно"
            else:
                return "Неправильно"
        case 1:
            if answer in ["гелий", "he"]:
                return "Правильно"
            else:
                return "Неправильно"
        case 2:
            if answer in ["литий", "li"]:
                return "Правильно"
            else:
                return "Неправильно"
        case 3:
            if answer in ["бериллий", "be"]:
                return "Правильно"
            else:
                return "Неправильно"
        case 4:
            if answer in ["углерод", "c"]:
                return "Правильно"
            else:
                return "Неправильно"
        case 5:
            if answer in ["кислород", "o"]:
                return "Правильно"
            else:
                return "Неправильно"
        case 6:
            if answer in ["фтор", "f"]:
                return "Правильно"
            else:
                return "Неправильно"
        case 7:
            if answer in ["натрий", "na"]:
                return "Правильно"
            else:
                return "Неправильно"
        case 8:
            if answer in ["магний", "mg"]:
                return "Правильно"
            else:
                return "Неправильно"
        case 9:
            if answer in ["хлор", "cl"]:
                return "Правильно"
            else:
                return "Неправильно"
