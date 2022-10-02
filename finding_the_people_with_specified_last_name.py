names = ("james jones", "kelvin grants", "james tyler", "job jones", "jones mark", "peter stone", "palu jones",
         "jones henry", "alex jones", "ezekiel pedro", "elizabeth pedro", "gideon job", "dave tyler", "david dicky")
print([name for name in names if name.split()[-1] == "jones"])