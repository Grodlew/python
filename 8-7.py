class Complex:
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex((self.real * other.real - self.imag * other.imag),
                       (self.imag * other.real + self.real * other.imag))

    def __str__(self):
        sign = '+' if self.imag > 0 else ''
        return f'{self.real}{sign}{self.imag}j'


z_1 = Complex(1, -2)
z_2 = Complex(3, 5)
print(z_1 + z_2)
print(z_1 * z_2)
