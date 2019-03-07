num = int(input('Enter the number from 0 to 999999 you want to translate: '))

NUMBER_TRANSLATIONS = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}


def translate(n):
    d = NUMBER_TRANSLATIONS

    if n in d.keys():
        return d[n]
    else:
        return d[n - n % 10] + '-' + d[n % 10]


def number2words(n):
    tens = n % 100
    hundreds = int(str(n // 100)[-1])
    tens_t = int((n % 100000 - (100 * hundreds + tens)) / 1000)
    hundreds_t = int(str(n // 100000)[-1])

    number_in_words = ''

    if hundreds_t:
        number_in_words = number_in_words + translate(hundreds_t) + ' hundred '
    if tens_t:
        number_in_words = number_in_words + translate(tens_t) + ' thousand '
    if hundreds_t and not tens_t:
        number_in_words = number_in_words + 'thousand '
    if hundreds:
        number_in_words = number_in_words + translate(hundreds) + ' hundred '
    if tens or not number_in_words:
        number_in_words = number_in_words + translate(tens)

    return number_in_words.strip()


print(str(num) + ' is ' + number2words(num))
