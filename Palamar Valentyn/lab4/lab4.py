def перелік_переваг():
    return ["Більш структурований код", "Покращена зрозумілість коду", "Спрощення перевикористання коду",
            "Можливість спільної роботи та інтеграції коду"]


def скласти_речення(перевага):
    return "%s - перевага функцій!" % перевага

def назвати_переваги_функцій():
    перелік_переваги = перелік_переваг()
    for перевага in перелік_переваги:
        print(скласти_речення(перевага))

назвати_переваги_функцій()
