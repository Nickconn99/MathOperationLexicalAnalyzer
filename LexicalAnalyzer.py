#NICK CONN
#MATH OPERATION LEXICAL ANALYZER


#TOKENS:
#Integer number = INT_LITERAL
#Float number = FLOAT_LITERAL
# ( LPAREN
# ) RPAREN
# + PLUS
# - MINUS
# * MULTIPLY
# / DIVIDE
# % MODULO
# && AND
# || OR
# < LESS_THAN
# <= LESS_THAN_EQUAL
# > GREATER_THAN
# >= GREATER_THAN_EQUAL
# Any letter a-z A-Z = IDENTIFIER 


import re


#LIST TO STORE EACH LEXEME AND COORESPONDING TOKEN
outputData = []

#TAKES DATA FROM LATest.txt
with open("LATest.txt") as file:
    data = file.read().strip().replace(" ", "")
    print(data)

    charIndex = 0

    while charIndex < len(data):
        charFinal = ""
        token = ""
        if data[charIndex].isnumeric():
            token = "INT_LITERAL"
            charFinal += str(data[charIndex])
            try:
                while data[charIndex+1].isnumeric() or data[charIndex+1] == '.':
                    charIndex += 1
                    charFinal += str(data[charIndex])
                    isFloat = charFinal.find('.')
                    if isFloat > -1:
                        token = "FLOAT_LITERAL"
            except:
                pass
            charIndex += 1
            #print(token, charFinal)
            outputData.append([charFinal, token])
        elif data[charIndex] == '(':
            token = "LPAREN"
            charFinal += str(data[charIndex])
            #print(token, charFinal)
            charIndex += 1
            outputData.append([charFinal, token])
        elif data[charIndex] == ')':
            token = "RPAREN"
            charFinal += str(data[charIndex])
            #print(token, charFinal)
            charIndex += 1
            outputData.append([charFinal, token])
        elif data[charIndex] == '+':
            token = "PLUS"
            charFinal += str(data[charIndex])
            #print(token, charFinal)
            charIndex += 1
            outputData.append([charFinal, token])
        elif data[charIndex] == '-':
            token = "MINUS"
            charFinal += str(data[charIndex])
            #print(token, charFinal)
            charIndex += 1
            outputData.append([charFinal, token])
        elif data[charIndex] == '*':
            token = "MULTIPLY"
            charFinal += str(data[charIndex])
            #print(token, charFinal)
            charIndex += 1
            outputData.append([charFinal, token])
        elif data[charIndex] == '/':
            token = "DIVIDE"
            charFinal += str(data[charIndex])
            #print(token, charFinal)
            charIndex += 1
            outputData.append([charFinal, token])
        elif data[charIndex] == '%':
            token = "MODULO"
            charFinal += str(data[charIndex])
            #print(token, charFinal)
            charIndex += 1
            outputData.append([charFinal, token])
        elif data[charIndex] == "&":
            try:
                if data[charIndex+1] == "&":
                    charIndex+=2
                    charFinal += "&&"
                    token = "AND"
                    outputData.append([charFinal, token])
                else:
                    charIndex+=1
                    charFinal = "&"
                    token = 'INVALID TOKEN'
                    outputData.append([charFinal, token])
            except:
                charIndex+=1
                charFinal = "&"
                token = 'INVALID TOKEN'
                outputData.append([charFinal, token])
        elif data[charIndex] == "|":
            try:
                if data[charIndex+1] == "|":
                    charIndex+=2
                    charFinal += "||"
                    token = "OR"
                    outputData.append([charFinal, token])
                else:
                    charIndex+=1
                    charFinal = "|"
                    token = 'INVALID TOKEN'
                    outputData.append([charFinal, token])
            except:
                charIndex+=1
                charFinal = "|"
                token = 'INVALID TOKEN'
                outputData.append([charFinal, token])
        elif data[charIndex] == '=':
            token = "ASSIGN"
            charFinal += str(data[charIndex])
            try:
                if(data[charIndex+1] == '='):
                    charIndex += 1
                    charFinal += str(data[charIndex])
                    token = "EQUALS"
            except:
                pass
            #print(token, charFinal)
            charIndex += 1
            outputData.append([charFinal, token])
        elif data[charIndex] == '>':
            token = "GREATER_THAN"
            charFinal += str(data[charIndex])
            try:
                if(data[charIndex+1] == '='):
                    charIndex += 1
                    charFinal += str(data[charIndex])
                    token = "GREATER_THAN_EQUAL"
            except:
                pass
            #print(token, charFinal)
            charIndex += 1
            outputData.append([charFinal, token])
        elif data[charIndex] == '<':
            token = "LESS_THAN"
            charFinal += str(data[charIndex])
            try:
                if(data[charIndex+1] == '='):
                    charIndex += 1
                    charFinal += str(data[charIndex])
                    token = "LESS_THAN_EQUAL"
            except:
                pass
            #print(token, charFinal)
            charIndex += 1
            outputData.append([charFinal, token])
        elif data[charIndex].isalpha():
            token = "IDENTIFIER"
            charFinal += str(data[charIndex])
            #print(token, charFinal)
            charIndex += 1
            outputData.append([charFinal, token])
        else:
            token = 'INVALID TOKEN'
            charFinal += str(data[charIndex])
            #print(token, charFinal)
            charIndex += 1
            outputData.append([charFinal, token])

#PRINT EACH LEXEME AND TOKEN VALUE
for item in outputData:
    print("LEXEME =", item[0] + " TOKEN =", item[1])

