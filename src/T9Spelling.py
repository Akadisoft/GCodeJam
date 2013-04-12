T9 = {}
T9['A'] = '2'
T9['B'] = '22'
T9['C'] = '222'

T9['D'] = '3'
T9['E'] = '33'
T9['F'] = '333'

T9['G'] = '4'
T9['H'] = '44'
T9['I'] = '444'

T9['J'] = '5'
T9['K'] = '55'
T9['L'] = '555'

T9['M'] = '6'
T9['N'] = '66'
T9['O'] = '666'

T9['P'] = '7'
T9['Q'] = '77'
T9['R'] = '777'
T9['S'] = '7777'

T9['T'] = '8'
T9['U'] = '88'
T9['V'] = '888'

T9['W'] = '9'
T9['X'] = '99'
T9['Y'] = '999'
T9['Z'] = '9999'


def test(tc,message):
    t9_codes = ""
    last_code = " "
    for ch in message:
        code = ''
        if ch == ' ':
            code = "0"      
        else:
            code = T9[ch.upper()]
            
        if last_code[0] == code[0]:
            code = " " + code
        t9_codes = t9_codes + code
        last_code = code
    print ("Case #" + str(tc)+": "+ t9_codes.strip())
           
           
if __name__ == '__main__' :
    # number of test cases
    N = input()
    tc = 1
    while tc <= N:
        line = raw_input()
        if not line.strip() == '':
            test(tc,line)
        tc = tc + 1
    
