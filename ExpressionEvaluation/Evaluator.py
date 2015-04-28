__author__ = 'Jay'


class Evaluator:
    def evaluate_string(self,expression):
        print expression
        expression=str(expression)
        character_list=list(expression)
        operator_list=list()
        operand_list=list()
        i=0
        while i < len(character_list):

            if character_list[i] is ' ':
                i+=1
                continue
            if character_list[i]>='0' and character_list[i]<='9':
                temp_digit=''
                while i<len(character_list) and character_list[i]>='0' and character_list[i]<='9':
                    temp_digit+=character_list[i]
                    i+=1
                i-=1
                operand_list.append(temp_digit)

            elif character_list[i] is '(':
                operator_list.append(character_list[i])
            elif character_list[i] is ')':
                while operator_list[-1]!='(':
                    operand_list.append(self.perform_operation(operator_list.pop(),operand_list.pop(),operand_list.pop()))
                operator_list.pop()
            elif character_list[i] is '+' or character_list[i] is '-' or character_list[i] is '*' or character_list[i] is '/':
                while len(operator_list)>0 and self.check_precedence(character_list[i],operator_list[-1]):
                    operand_list.append(self.perform_operation(operator_list.pop(),operand_list.pop(),operand_list.pop()))
                operator_list.append(character_list[i])
            else:
                raise ValueError
            i+=1

        while len(operator_list)>0 :
            operand_list.append(self.perform_operation(operator_list.pop(),operand_list.pop(),operand_list.pop()))

        return operand_list.pop()



    def check_precedence(self,operator_1,operator_2):
        if operator_1 is '(' or operator_2 is '(':
            return False
        if (operator_1 is '*' or operator_1 is '/') and (operator_2 is '+' or operator_2 is '-'):
            return False
        else:
            return True



    def perform_operation(self,operator,operand_2,operand_1):
        if operator is '+':
            return int(operand_1)+int(operand_2)
        elif operator is '-':
            return int(operand_1)-int(operand_2)
        elif operator is '*':
            return int(operand_1)*int(operand_2)
        elif operator is '/':
            if int(operand_2) is not 0:
                return int(operand_1)/int(operand_2)
            else:
                return 'Divison by 0 not supported.'


