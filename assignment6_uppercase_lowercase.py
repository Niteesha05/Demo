def up_low(s):
    u=sum(1 for i in s if i.isupper())
    l=sum(1 for i in s if i.islower())
    print("no.of upper case characters: %s" %u)
    print("no.of lower case characters: %s" %l)
up_low("Hello Mr.Rogers,how are you this fine Tuesday?")
