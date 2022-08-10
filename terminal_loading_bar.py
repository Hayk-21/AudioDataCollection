

def loadbar(interation, total, prefix='', suffix='', decimals=1, length=100, fill='>', fig='-'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (interation/float(total)))
    filledLength = int(length * interation // total)
    bar = fill * filledLength + fig * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if interation == total:
        print()
