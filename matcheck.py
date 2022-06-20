import matcensor
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel
mats = matcensor.MatProtect()
tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)

def status(message):
    matfiltr = mats.checkCensor(obj=message)
    if matfiltr['status']:
        return 'Сообщение содержит ненормативную лексику: ' + ', '.join(matfiltr['badwords'])
    filter2 = mats.checkCensor(obj=message.replace('ё', 'е'))
    if filter2['status']:
        return 'Сообщение содержит ненормативную лексику: ' + ', '.join(filter2['badwords'])
    res = {
        'speech': 'Сообщение формальное',
        'neutral': 'Сообщение нейтральное',
        'positive': 'Сообщение позитивное',
        'negative': 'Сообщение негативное',
        'skip': 'Не удалось определить характер сообщения'
        }
    return res[list(model.predict([message])[0].keys())[0]]

message = input('Введите строку: ')
print(status(message))


