import itertools
import re
class TruthTable:
    def __init__(self, expression):
        self.rstack = []
        self.expression = expression
        self.variable_names = sorted(set([char for char in expression if char.isalpha()]))
        self.expression = expression
    def evaluate(self, values):
        variables = dict(zip(self.variable_names, values))
        variables = {key: bool(value) for key, value in variables.items()}
        opz = self.create_opz(self.expression)
        for i in opz:
            if i in ['a', 'b', 'c', 'd', 'e']:
                self.rstack.append(i)
            elif i == '!':
                rstring = str(i + self.rstack.pop())
                substituted_operation = self.substitute_variables(rstring, variables)
                result = self.calc(substituted_operation)
                self.rstack.append(result)
            elif i in ["&", "!", "|", "=", "~", ">"]:
                rstring = str(self.rstack[-2])+str(i) + str(self.rstack[-1])
                self.rstack.pop()
                self.rstack.pop()
                substituted_operation = self.substitute_variables(rstring, variables)
                result = self.calc(substituted_operation)
                self.rstack.append(result)
        return int(self.rstack.pop())

    def __iter__(self):
        for values in itertools.product([0, 1], repeat=len(self.variable_names)):
            yield values + (self.evaluate(values),)

    def __str__(self):
        header = ' '.join(self.variable_names) + ' F'
        table_str = header + '\n'
        for row in self:
            values_str = ' '.join(str(value) for value in row[:-1])
            table_str += '{} {}\n'.format(values_str, row[-1])
        return table_str

    def sknf(self):
        sknf_terms = []
        for row in self:
            if row[-1] == 0:
                term = []
                for i, value in enumerate(row[:-1]):
                    if value == 0:
                        term.append(self.variable_names[i])
                    else:
                        term.append('(¬' + self.variable_names[i]+ ')')
                sknf_terms.append('(' + ' ∨ '.join(term) + ')')
        return ' ∧ '.join(sknf_terms)

    def sdnf(self):
        sdnf_terms = []
        for row in self:
            if row[-1] == 1:
                term = []
                for i, value in enumerate(row[:-1]):
                    if value == 1:
                        term.append(self.variable_names[i])
                    else:
                        term.append('(¬' + self.variable_names[i] + ')')
                sdnf_terms.append('(' + ' ∧ '.join(term) + ')')
        return ' ∨ '.join(sdnf_terms)
    
    def num_sknf(self):
        result = []
        for row in self:
            if row[-1] == 0:
                num = ''.join(str(element) for element in row[:-1])
                num = int(num, 2) 
                result.append(num)
        return result

    def num_sdnf(self):
        result = []
        for row in self:
            if row[-1] == 1:
                num = ''.join(str(element) for element in row[:-1])
                num = int(num, 2) 
                result.append(num)
        return result
    
    def ind_view(self):
        
        result=[]
        for row in self:
            result.append(str(row[-1]))
            
        result_int = int(''.join(result),2)
        print("Int result: ",result_int)
        return ''.join(result)

    def create_opz(self,expression):
        stack = []
        output = []
        for token in expression:
            if token in ['a','b','c','d','e']:
                output.append(token)
            elif token in ["&", "!", "|", "=","~",">"]:
                while stack and stack[-1] in ["!"]: 
                    output.append(stack.pop())
                stack.append(token)
            elif token == "(":
                stack.append(token)
            elif token == ")":
                while stack and stack[-1] != "(":
                    output.append(stack.pop())
                stack.pop()

        while stack:
            output.append(stack.pop())
        return output

    def calc(self,expression):
        patterns = {
            'True|True': True,
            'False|True': True,
            'True|False': True,
            'False|False': False,

            'True=True': True,
            'True=False': False,
            'False=True': False,
            'False=False': True,

            'True>True': True,
            'True>False': False,
            'False>True': True,
            'False>False': True,

            'True&True': True,
            'True&False': False,
            'False&True': False,
            'False&False': False,

            '!False': True,
            '!True': False
        }

        if expression in patterns:
            return patterns[expression]
        else:
            return None

    def substitute_variables(self,operation, variables):
        variable_pattern = r"\w+"

        def replace_variable(match):
            variable = match.group()
            if variable in variables:
                return str(variables[variable])
            return variable

        substituted_operation = re.sub(variable_pattern, replace_variable, operation)

        return substituted_operation

expression = '(!a)>(b|c)'

table = TruthTable(expression)
print("Таблица истинности:")
print(table)
print(table.sknf())
print(table.sdnf())
print(table.num_sdnf())
print(table.num_sknf())
print(table.ind_view())
