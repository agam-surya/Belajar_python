# celcius
def celc(celcius):
    fahrenheit = (9/5)*celcius+32
    kelvin = celcius + 273
    reamur = 4/5*celcius

    print("suhu", celcius, "celcius = ", fahrenheit,
          'fahrenheit,', kelvin, 'kelvin,', reamur, 'reamur')

# reamur


def ream(reamur):
    fahrenheit = (9/4)*reamur+32
    kelvin = (5/4)*reamur + 273
    celcius = 5/4*reamur

    print("suhu", reamur, "reamur = ", fahrenheit,
          'fahrenheit,', kelvin, 'kelvin,', celcius, 'celcius')

# fahrenheit


def fah(fahrenheit):
    celcius = (5/9)*(fahrenheit-32)
    kelvin = celcius + 273
    reamur = 4/9*(fahrenheit-32)

    print("suhu", fahrenheit, "fahrenheit = ", celcius,
          'celcius,', kelvin, 'kelvin,', reamur, 'reamur')

# kelvin


def kel(kelvin):
    celcius = kelvin-273
    fahrenheit = 9/5*celcius + 32
    reamur = 4/5*(celcius)

    print("suhu", kelvin, "kelvin = ", celcius, 'celcius,',
          fahrenheit, 'fahrenheit,', reamur, 'reamur')


celc(float(input("input suhu celcius :")))
fah(float(input("input suhu fahrenheit :")))
ream(float(input("input suhu reamur :")))
kel(float(input("input suhu kelvin :")))
