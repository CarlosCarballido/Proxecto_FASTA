def parseArgs(args):
    toret = {}
    for arg in args:
        argSplit = arg.split('=')
        name = argSplit[0].replace('--', '')

        if len(argSplit) == 2:
            toret[name] = argSplit[1]
        else:
            toret[name] = True

    return toret
