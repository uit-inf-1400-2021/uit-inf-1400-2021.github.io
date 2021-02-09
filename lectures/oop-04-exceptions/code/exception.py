import glob

def les_fil(filnavn):
    if len(glob.glob(filnavn)) < 1:
        raise ValueError("Ingen filer som passer funnet", with_traceback=True)
    else:
        print("Fant filer")

def les_masse_filer():
    les_fil("*.py")
    les_fil("*f*")
    les_fil("hallo")

try:
    les_masse_filer()
except ValueError as exc:
    print(exc)
except NameError:
    print("Har du glemt å importere noe?")

