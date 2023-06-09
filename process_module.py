from time_module import get_time, get_date
from database import *
from output_module import output
from input_module import take_input
from internet import check_internet_connection, check_on_wikipedia
import assistent_details


def process(query):
    answer = get_answer_from_memory(query)

    if answer == "get time detail":
        return "Time is " + get_time()
    elif answer == "check internet connection":
        if check_internet_connection():
            return "internet is connected"
        else:
            return "internet is not connected"
    elif answer == "tell date":
        return "Date is " + get_date()

    elif answer == "on speak":
        return turn_on_speech()

    elif answer == "off speak":
        return turn_off_speech()



    elif answer == 'change name':
        output("okay! what do you want to call me")
        temp = take_input()
        if temp == assistent_details.name:
            return "Can't change. I think you are happy with ny old name"

        else:
            update_name(temp)
            assistent_details.name = temp
            return "Now you can call me " + temp


    else:

        output("Don't know this one should i search on internet ")
        ans = take_input()
        if "yes" in ans:
            answer = check_on_wikipedia(query)
            if answer != "":
                return answer
        else:
            output("can you please tell me what its means")
            ans = take_input()
            if "it means" in ans:
                ans = ans.replace("it means", "")
                ans = ans.strip()
                value = get_answer_from_memory(ans)
                if value == "":
                    return "Can't help with this one"
                else:
                    insert_question_and_answer(query, value)
                    return "Thanks i will remember for the next time"
            else:
                return "can't help with this one"
