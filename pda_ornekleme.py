class PDA:
    def _init_(self):
        self.stack = []

    def is_operator(self, c):
        return c in ['+', '-', '*', '/']

    def is_digit(self, c):
        return c.isdigit()

    def is_balanced_and_valid(self, expression):
        self.stack = []
        self.stack.append('#')  # yığıtın başlangıç sembolü
        state = 'q0'  # state değişkeninin başlangıç değeri
        n = len(expression)


        for i, char in enumerate(expression):
            if state == 'q0':
                if char.isdigit():
                    state = 'q1'
                elif char == '(':
                    self.stack.append(char)
                    state = 'q0'
                else:
                    return False

            elif state == 'q1':
                if char in '+-*/':
                    state = 'q2'
                elif char == ')':
                    if self.stack and self.stack[-1] == '(':
                        self.stack.pop()
                        state = 'q1'
                    else:
                        return False
                else:
                    return False

            elif state == 'q2':
                if char.isdigit():
                    # 0'a bölme kontrolü
                    if expression[i-1] == '/' and char == '0':
                        return False
                    state = 'q1'
                elif char == '(':
                    self.stack.append(char)
                    state = 'q0'
                else:
                    return False

        return state == 'q1' and self.stack == ['#']

def check_expression(expression):
    pda = PDA()
    return pda.is_balanced_and_valid(expression)

def main():
    expression = input("Lütfen kontrol etmek istediğiniz matematiksel ifadeyi girin: ")
    result = check_expression(expression)
    if result:
        print("Girilen ifade geçerli ve dengelidir.")
    else:
        print("Girilen ifade geçersiz veya dengesizdir.")

if __name__ == "__main__":
    main()

