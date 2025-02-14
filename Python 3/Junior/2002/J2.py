def american_to_canadian(w):
    return w[:-2] + "our" if len(w) > 4 and w.endswith("or") and w[-3] not in "aeiouy" else w
while (w := input()) != "quit!":
    print(american_to_canadian(w))