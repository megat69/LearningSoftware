from random import randrange, shuffle
from time import sleep
import json
from copy import deepcopy
import timeit

# Open the ini file and gets its variables
ini = open("startup.json", "r", encoding="utf-8")
ini_vars = json.load(ini)
ini.close()
# And initializes 'filename' as PyCharm does not like the statement that follows
filename = ""

# Basically creates the variables from the ini file
for element in ini_vars:
    locals()[element] = ini_vars[element]

file = open(filename, "r", encoding="utf-8")
verbs_list = file.readlines()
file.close()

def recreate_string(variable:list, char_in_between:str=""):
    """
    Recreates a string from a list.
    Parameter 'variable' (list) : The list to put together to a string.
    Parameter 'char_in_between' (str) : The char to put between the elements to recompose. Nothing by default.
    """
    temp_str = ""
    for element in variable:
        temp_str += str(element) + char_in_between
    return temp_str

class bcolors:
    global colors_enabled
    if colors_enabled is True:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        ITALICS = '\x1B[3m'
    else:
        HEADER = ''
        OKBLUE = ''
        OKGREEN = ''
        WARNING = ''
        FAIL = ''
        ENDC = ''
        BOLD = ''
        UNDERLINE = ''
        ITALICS = ''

def generate_answers_list(size, columns):
    """
    Generates the list of answers.
    """
    global bcolors
    global verbs_list
    global column_selected
    global i
    if isinstance(verbs_list[i][column_selected], list):
        verbs_list[i][column_selected] = recreate_string(verbs_list[i][column_selected], "; ")[:-2]
    answer = [
        f"{bcolors.WARNING}{columns[k][0].upper() + columns[k][1:]} de " \
        f"'{bcolors.HEADER}{verbs_list[i][column_selected]}{bcolors.ENDC}' : {bcolors.ENDC}" \
        for k in range(size)
    ]
    return answer

mode = -5
while mode < 1 or mode > 8:
    mode = int(input(f"{bcolors.WARNING}Choisis le mode :{bcolors.ENDC}\n"
        f"{bcolors.WARNING}1) Dans l'ordre, une seule colonne à remplir ;{bcolors.ENDC}\n"
        f"{bcolors.WARNING}2) Dans l'ordre, trois colonnes à remplir ;{bcolors.ENDC}\n"
        f"{bcolors.WARNING}3) Ordre aléatoire, trois colonnes à remplir ;{bcolors.ENDC}\n"
        f"{bcolors.WARNING}4) MODE INFINI, TROIS COLONNES, dans l'ordre ;{bcolors.ENDC}\n"
        f"{bcolors.WARNING}5) MODE INFINI, TROIS COLONNES, DANS LE DÉSORDRE ;{bcolors.ENDC}\n"
        f"{bcolors.WARNING}6) Choisis les lignes à travailler, 3 colonnes, dans l'ordre ;{bcolors.ENDC}\n"
        f"{bcolors.WARNING}7) Choisis les lignes à travailler, 3 colonnes, DANS LE DÉSORDRE ;{bcolors.ENDC}\n"
        f"{bcolors.WARNING}8) MODE INFINI, choisis les lignes à travailler, 3 colonnes, DANS LE DÉSORDRE{bcolors.ENDC}\n"))

# Defining what every column corresponds to
column_order = verbs_list[0].split(",")
for i in range(len(column_order)):
    column_order[i] = column_order[i].strip()
# Removing that first line with column names
verbs_list.pop(0)

# INIT
correct_answers = 0
wrong_answers = list()

# Getting verbs format
for i in range(len(verbs_list)):
    verbs_list[i] = verbs_list[i].split(",")
    for k in range(len(verbs_list[i])):
        # Multi answers ?
        if ";" in verbs_list[i][k]:
            verbs_list[i][k] = verbs_list[i][k].split(";")
            for j in range(len(verbs_list[i][k])):
                verbs_list[i][k][j] = verbs_list[i][k][j].strip()
        else:
            verbs_list[i][k] = verbs_list[i][k].strip()

# Switch for each mode
if mode == 1:
    # Asking for every verb, in the original order
    for i in range(len(verbs_list)):
        # Randomly selecting one verb in the list
        column_selected = randrange(0, len(verbs_list[i]))

        # Creating the phrase to ask for
        for k in range(len(verbs_list[i])):
            if column_selected != k and isinstance(verbs_list[i][k], list):
                verbs_list[i][k] = recreate_string(verbs_list[i][k], "; ")[:-2]
        others = "".join(f"{verbs_list[i][k]} ({column_order[k]}), " for k in range(4) if k != column_selected)

        # Asking the question to the user
        answer_time = timeit.default_timer()
        answer = input(f"{bcolors.OKBLUE}Conjugue le verbe {bcolors.HEADER}{others}{bcolors.OKBLUE}pour le temps '{column_order[column_selected]}'.{bcolors.ENDC}\n")
        answer_time = round(timeit.default_timer() - answer_time)

        # If there are multiple answers
        if isinstance(verbs_list[i][column_selected], list):
            if multi_answers_require_all is True:
                verbs_list[i][column_selected] = recreate_string(verbs_list[i][column_selected], "; ")[:-2]
            else:
                if answer.lower() in verbs_list[i][column_selected]:  # If the answer is in the correct answers
                    # Printing a congrats message
                    print(f"{bcolors.OKGREEN}Bravo, c'est juste !{bcolors.ENDC}")
                    # Incrementing the correct answers counter
                    correct_answers += 1

                else:  # If the answer is wrong
                    # Print a message with the answer
                    print(
                        f"{bcolors.FAIL}Non, c'était '{bcolors.HEADER}{verbs_list[i][column_selected]}{bcolors.FAIL}' !{bcolors.ENDC}")
                    # Adding the wrong answer to the list of total wrong answers
                    wrong_answers.append(f"{verbs_list[i][column_selected]} pour le temps '{column_order[column_selected]}'")
        if multi_answers_require_all is True:
            if answer.lower() == verbs_list[i][column_selected]:  # If the answer is correct
                # Printing a congrats message
                print(f"{bcolors.OKGREEN}Bravo, c'est juste !{bcolors.ENDC}")
                # Incrementing the correct answers counter
                correct_answers += 1

            else:  # If the answer is wrong
                # Print a message with the answer
                print(f"{bcolors.FAIL}Non, c'était '{bcolors.HEADER}{verbs_list[i][column_selected]}{bcolors.FAIL}' !{bcolors.ENDC}")
                # Adding the wrong answer to the list of total wrong answers
                wrong_answers.append(f"{verbs_list[i][column_selected]} pour le temps '{column_order[column_selected]}'")

        if answer_time < 5:
            print(f"{bcolors.OKBLUE}{answer_time}{bcolors.OKBLUE} secondes pour répondre ? Rapide comme l'éclair !{bcolors.ENDC}")
        elif 5 <= answer_time < 10:
            print(f"{bcolors.WARNING}{answer_time}{bcolors.OKBLUE} secondes pour répondre... Pas mal !{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}{answer_time}{bcolors.OKBLUE} secondes pour répondre... C'est trop lent !{bcolors.ENDC}")

        # Sleeping half a second
        sleep(0.5)

    # Printing good answers number
    print(f"{bcolors.OKBLUE}Tu as eu {bcolors.OKGREEN}{correct_answers}{bcolors.OKBLUE} bonnes réponses.{bcolors.ENDC}")

    if len(wrong_answers) == 0:  # If there are no wrong answers
        # Printing a little congrats message
        print(f"{bcolors.OKGREEN}Et aucune mauvaise ! Félicitations !{bcolors.ENDC}")
    else:  # If there are wrong answers
        # Formatting the wrong_answers variable
        wrong_answers = recreate_string(wrong_answers, '\n- ')[:-3]

        # Printing the list of wrong answers
        print(f"{bcolors.FAIL}Tu t'es loupé(e) pour :\n- {wrong_answers}{bcolors.ENDC}")
elif mode in (2, 3, 6, 7):
    # Mode 2 and 3 are identical, except the fact mode 3 or 7 shuffles the verbs order
    if mode == 6 or mode == 7:
        print(f"{bcolors.WARNING}Quelles lignes tu veux travailler ?{bcolors.ENDC}")
        min_line = int(input(f"{bcolors.WARNING}Ligne minimum : {bcolors.ENDC}")) - 1
        max_line = int(input(f"{bcolors.WARNING}Ligne maximum : {bcolors.ENDC}"))
        # Removing all the lines before 'min_line' and after 'max_line'
        verbs_list = verbs_list[min_line:max_line]

    if mode == 3 or mode == 7:  # So if it is mode 3 or 7
        # Shuffling the verbs order
        shuffle(verbs_list)

    # Asking for every single verb in the list
    for i in range(len(verbs_list)):
        # Randomly choosing a column
        column_selected = randrange(0, len(verbs_list[i]))

        # Creating all the answers, and formatting them
        answer = generate_answers_list(len(verbs_list[i]), column_order)

        # Removing the selected column, no need to ask
        answer.pop(column_selected)

        answer_time = []
        # Asking every question
        for k in range(len(answer)):
            answer_time.append(timeit.default_timer())
            answer[k] = input(answer[k])
            answer_time[k] = round(timeit.default_timer() - answer_time[k])

        # Adding the formatted answer back to the list as a model
        temp = deepcopy(verbs_list[i][column_selected])
        if isinstance(temp, list):
            temp = recreate_string(temp, "; ")[:-2]
        answer.insert(column_selected, column_order[column_selected][0].upper()+column_order[column_selected][1:] + " : "
                      + bcolors.HEADER + temp + bcolors.ENDC)
        del temp

        # Deciding whether or not the answers are correct
        for k in range(len(answer)):
            if k == column_selected:  # No need need to check that answer, just going next loop
                continue

            # If there are multiple answers
            do_not_the_other_statement = False
            if isinstance(verbs_list[i][k], list):
                if multi_answers_require_all is True:
                    verbs_list[i][column_selected] = recreate_string(verbs_list[i][column_selected], "; ")[:-2]
                else:
                    do_not_the_other_statement = True
                    if answer[k].lower() in verbs_list[i][k]:  # If it is correct
                        answer[k] = f"{column_order[k][0].upper()+column_order[k][1:]} : {bcolors.HEADER}{answer[k]}{bcolors.OKGREEN} -> Juste !{bcolors.ENDC}"
                    else:  # Otherwise
                        answer[k] = f"{column_order[k][0].upper()+column_order[k][1:]} : {bcolors.HEADER}{answer[k]}{bcolors.FAIL} -> Faux ! Réponse : '{bcolors.HEADER}{recreate_string(verbs_list[i][k], '; ')[:-2]}{bcolors.FAIL}'{bcolors.ENDC}"
            if do_not_the_other_statement is False:
                if answer[k].lower() == verbs_list[i][k]:  # If it is correct
                    answer[k] = f"{column_order[k][0].upper()+column_order[k][1:]} : {bcolors.HEADER}{answer[k]}{bcolors.OKGREEN} -> Juste !{bcolors.ENDC}"
                else:  # Otherwise
                    if isinstance(verbs_list[i][k], list):
                        verbs_list[i][k] = recreate_string(verbs_list[i][k], "; ")[:-2]
                    answer[k] = f"{column_order[k][0].upper()+column_order[k][1:]} : {bcolors.HEADER}{answer[k]}{bcolors.FAIL} -> Faux ! Réponse : '{bcolors.HEADER}{verbs_list[i][k]}{bcolors.FAIL}'{bcolors.ENDC}"

        # Prints the formatted correction
        print(recreate_string(answer, "\n"))

        answer_time.sort()
        answer_time = answer_time[len(answer_time)-1]
        if answer_time < 5:
            print(f"{bcolors.OKGREEN}{answer_time}{bcolors.OKBLUE} secondes max pour répondre ? Rapide comme l'éclair !{bcolors.ENDC}")
        elif 5 <= answer_time < 10:
            print(f"{bcolors.WARNING}{answer_time}{bcolors.OKBLUE} secondes max pour répondre... Pas mal !{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}{answer_time}{bcolors.OKBLUE} secondes max pour répondre... C'est trop lent !{bcolors.ENDC}")

        # Just sleeping half a second
        sleep(0.5)
elif mode in (4, 5, 8):
    # Mode 5 has nearly no difference with mode 4, the only one is
    # mode 5 shuffles the list of verbs, and the 8 chooses the lines to practise on.

    # Initializes some variables
    running = True
    loop_times = 0
    i = -1

    if mode == 8:
        print(f"{bcolors.WARNING}Quelles lignes tu veux travailler ?{bcolors.ENDC}")
        min_line = int(input(f"{bcolors.WARNING}Ligne minimum : {bcolors.ENDC}")) - 1
        max_line = int(input(f"{bcolors.WARNING}Ligne maximum : {bcolors.ENDC}"))
        # Removing all the lines before 'min_line' and after 'max_line'
        verbs_list = verbs_list[min_line:max_line]

    # Creates a loop
    while running:
        if mode == 5:  # So if it is mode 5
            # We shuffle the list of verbs
            shuffle(verbs_list)

        # Selects a random column and some impossible to understand stuff, but it works ¯\_(ツ)_/¯
        i += 1
        if i > len(verbs_list)-1:
            i = 0

        column_selected = randrange(0, 3)
        answer = generate_answers_list(len(verbs_list[i]), column_order)
        answer.pop(column_selected)

        answer_time = list()
        # Asking the answers
        for k in range(len(answer)):
            answer_time.append(timeit.default_timer())
            answer[k] = input(answer[k])
            answer_time[k] = round(timeit.default_timer() - answer_time[k])

        # Adding the formatted answer back to the list as a model
        temp = deepcopy(verbs_list[i][column_selected])
        if isinstance(temp, list):
            temp = recreate_string(temp, "; ")[:-2]
        answer.insert(column_selected,
                      column_order[column_selected][0].upper() + column_order[column_selected][1:] + " : "
                      + bcolors.HEADER + temp + bcolors.ENDC)
        del temp

        # Correcting
        for k in range(len(answer)):
            if k == column_selected:  # No need need to check that answer, just going next loop
                continue

            # If there are multiple answers
            do_not_the_other_statement = False
            if isinstance(verbs_list[i][k], list):
                if multi_answers_require_all is True:
                    verbs_list[i][column_selected] = recreate_string(verbs_list[i][column_selected], "; ")[:-2]
                else:
                    do_not_the_other_statement = True
                    if answer[k].lower() in verbs_list[i][k]:  # If it is correct
                        answer[k] = f"{column_order[k][0].upper() + column_order[k][1:]} : {bcolors.HEADER}{answer[k]}{bcolors.OKGREEN} -> Juste !{bcolors.ENDC}"
                    else:  # Otherwise
                        answer[k] = f"{column_order[k][0].upper() + column_order[k][1:]} : {bcolors.HEADER}{answer[k]}{bcolors.FAIL} -> Faux ! Réponse : '{bcolors.HEADER}{recreate_string(verbs_list[i][k], '; ')[:-2]}{bcolors.FAIL}'{bcolors.ENDC}"
            if do_not_the_other_statement is False:
                if answer[k].lower() == verbs_list[i][k]:  # If it is correct
                    answer[k] = f"{column_order[k][0].upper() + column_order[k][1:]} : {bcolors.HEADER}{answer[k]}{bcolors.OKGREEN} -> Juste !{bcolors.ENDC}"
                else:  # Otherwise
                    if isinstance(verbs_list[i][k], list):
                        verbs_list[i][k] = recreate_string(verbs_list[i][k], "; ")[:-2]
                    answer[k] = f"{column_order[k][0].upper() + column_order[k][1:]} : {bcolors.HEADER}{answer[k]}{bcolors.FAIL} -> Faux ! Réponse : '{bcolors.HEADER}{verbs_list[i][k]}{bcolors.FAIL}'{bcolors.ENDC}"

        # Prints the formatted correction
        print(recreate_string(answer, "\n"))

        # Adds a loop time
        loop_times += 1

        # Every 5 loop iterations, we ask the user if he wants to quit
        if loop_times % 5 == 0:
            confirm = input(f"{bcolors.OKBLUE}On s'arrête ou on continue ? ('quitter' ou 'stop' pour quitter, sinon ça continue !) : {bcolors.ENDC}")
            if confirm.lower() == "quitter" or confirm.lower() == "stop":
                running = False
            del confirm

        answer_time.sort()
        answer_time = answer_time[len(answer_time) - 1]
        if answer_time < 5:
            print(f"{bcolors.OKGREEN}{answer_time}{bcolors.OKBLUE} secondes max pour répondre ? Rapide comme l'éclair !{bcolors.ENDC}")
        elif 5 <= answer_time < 10:
            print(f"{bcolors.WARNING}{answer_time}{bcolors.OKBLUE} secondes max pour répondre... Pas mal !{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}{answer_time}{bcolors.OKBLUE} secondes max pour répondre... C'est trop lent !{bcolors.ENDC}")

        # Sleeping half a second
        sleep(0.5)

    # Prints a greetings text
    print("Encore bravo !")
