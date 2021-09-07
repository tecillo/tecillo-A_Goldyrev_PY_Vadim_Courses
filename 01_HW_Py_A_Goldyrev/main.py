st = "My string"
i = 1
flo = 1.5
b = bytes(4)
l = ["ok", "google", 56, 79]
tu = ("I", "am", "hungry", 77)
se = {"hello", 777, 953, 777}
fse = frozenset("666")
dic = {"name" : "Killabeez"}

print(
    "st - ", st, type(st), "\n", "i - ", i, type(i), "\n", "flo - ", flo, type(flo), "\n", "b - ", b, type(b),
    "\n", "l - ", l, type(l), "\n", "tu - ", tu, type(tu),"\n", "se - ", se, type(se), "\n", "fse - ", fse, type(fse)
)

unoStr = "Andrey"
dosStr = "Goldyrev"
tres = unoStr + ' ' + dosStr
print(tres)

unoIn = 41
dosIn = 12
tresIn = unoIn + dosIn
quatroIn = unoIn * dosIn
cincoIn = unoIn / dosIn
seisIn = unoIn // dosIn
sieteIn = unoIn % dosIn
print(tresIn, " ", quatroIn, " ", cincoIn, " ", seisIn, " ", sieteIn)

