
def __init__() :
    msg = 'KYZJZJDPGIZDRIPBVP'
    caesar(msg)

def caesar(msg) :
    ex = ''
    msg = msg.upper()

    for u in range(1,26) :
        for k in msg :
            for i in range(65,91) :
                if k==chr(i) :
                    if (i+u) > 90 :
                        ex += chr(i+u-26)
                    else :
                        ex += chr(i+u)
        print('[{0}] : {1}'.format(u,ex))
        ex = ''

__init__()
print('Decrypted in line 9!')