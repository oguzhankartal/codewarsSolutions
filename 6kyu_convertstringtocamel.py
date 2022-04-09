import re
def to_camel_case(text):
    l = [w for w in re.split('[-_]', text)]
    x = []
    for c, w in enumerate(l):
        if c != 0:
            x.append(w.capitalize())
        else:
            x.append(w)
    return "".join(w for w in x)
