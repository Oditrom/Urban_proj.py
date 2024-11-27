def send_email(message, recipient, sender = "university.help@gmail.com"):
    if '@' not in sender or '@' not in recipient:
        print("Невозможно отправить письмо с адреса ",sender, "на адрес" ,recipient)
        return
    if recipient.endswith('.com') == False and recipient.endswith('.net') == False and recipient.endswith('.ru') == False:
        print("Невозможно отправить письмо с адреса ",sender, "на адрес" ,recipient)
        return
    if sender.endswith('.com') == False and sender.endswith('.net') == False and sender.endswith('.ru') == False:
        print("Невозможно отправить письмо с адреса ",sender, "на адрес" ,recipient)
        return
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender != 'university.help@gmail.com':
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + sender + " на адрес " + recipient, ".")
        return
    else:
        print("Письмо успешно отправлено с адреса " + sender + " на адрес " + recipient + '.')
