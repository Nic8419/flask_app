def validation_names(stra):
    s = {}
    names = stra.split(',')
    for i in range(len(names)):
        if len(names[i]) < 10 and (names[i]).isalpha():
            s['error'] = False
        else:
            s['error'] = True
            break
    if not s['error']:
        if len(stra) == 0:
            s['data'] = "Это никому не нравится"
        if len(names) == 1:
            s['data'] = "{} лайкнул это.".format(names[0])
        if len(names) == 2:
            s['data'] = "{} и {} лайкнули это.".format(names[0], names[1])
        if len(names) == 3:
            s['data'] = "{}, {} и {} лайкнули это.".format(names[0], names[1], names[2])
        if len(names) > 3:
            s['data'] = "{}, {} и ещё {} человека лайкнули это".format(names[0], names[1], len(names) - 2)
        s['error_message'] = None
    else:
        s['data'] = None
        s['error_message'] = 'Ошибка в имени'
    return s
