def navigate(commands, width, height, wrap=False):
    i=0
    pairs={}
    while len(commands)>i:
        if commands[i].isalpha():
            alpha=commands[i]
            number=""
            i+=1
            while i<len(commands) and commands[i].isdigit():
                number+=commands[i]
                i+=1
                pairs[alpha]=int(number)
        else:
            i+=1




navigate("R3U46",4,5)