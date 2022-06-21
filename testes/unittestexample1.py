from unittest import TestCase, main

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x,y):
    return x * y

class Testes(TestCase):
    def test_soma(self):
        self.assertEqual(soma(5, 5), 10)
        self.assertLess(soma(5, 5), 11)

    # def test_soma_errada(self):
    #     self.assertEqual(soma(5, 5), 13)

    def test_sub(self):
        self.assertEqual(sub(5,5), 0)


if __name__ == '__main__':
    main()