import time

def loadbar(interation, total, prefix='', suffix='', decimals=1, length=100, fill='>'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (interation/float(total)))
    filledLength = int(length * interation // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if interation == total:
        print()
#
# items = list(range(0, 50))
# l = len(items)
# loadbar(0, l, prefix='Progress:', suffix='Complete', length=l)
# for i, item in enumerate(items):
#     time.sleep(0.1)
#     loadbar(i+1, l, prefix='Progress:', suffix='Complete', length=l)
