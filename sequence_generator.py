def generate_sequence(n):
    result = ''
    number = 1
    while len(result) < n:
        result += str(number) * number
        number += 1
    return result[:n]


def main():
    print(('«Генератор числовой последовательности»,'
          ' для выхода введите "exit"'))
    while True:
        data = input('Введите число:\n')
        if data.lower() == 'exit':
            break
        try:
            data = int(data)
        except ValueError:
            print(f'"{data}" не является числом.', end='\n' * 2)
            continue
        if data <= 0:
            print('Введите положительное число.', end='\n' * 2)
            continue
        print(
            'Результат:', generate_sequence(data),
            sep='\n',
            end='\n' * 2
        )


if __name__ == '__main__':
    main()
