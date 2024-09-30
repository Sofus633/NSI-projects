def asknumber(min, max, question):
    try:
        inp = int(input(question))
        if inp < min or inp > max:
            print(f'input need to be < {min} and >{max}')
            return asknumber(min, max, question)
        return inp
    except:
        return asknumber(min, max, question)
    
    
def askstr(min, max, question):
    try:
        inp = input(question)
        if len(inp) < min or len(inp) > max:
            print(f'input need to be < {min} and >{max}')
            return asknumber(min, max, question)
        return inp
    except :
        return asknumber(min, max, question)