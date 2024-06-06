from tabulate import tabulate
import re

class Sdnf:
    def __init__(self,formula):
        self.formula = formula
        self.listed_formula = self.format_strings(self.formula)
        self.minimaized_sdnf = self.find_inter(self.listed_formula)
        self.letters = sorted(list(set([char.lower() for char in re.findall(r'[a-zA-Z]', formula)])))
        self.calc_method = ''
        self.carno = self.convert_letters_to_numbers(self.format_strings(self.formula))
        self.zero_array = self.create_zero_array(self.carno)
    def print(self):
        print("Минимизированная СДНФ: ",self.minimaized_sdnf)
        
    def format_strings(self,formula):
        exp = formula.split("|")
        expression = [[char for char in row if char != '&'] for row in exp]
        formatted_list = []
        for string in expression:
            new_string = ""
            for i, char in enumerate(string):
                if i > 0 and string[i-1] == "!":
                    new_string += char.upper()
                elif char != "!":
                    new_string += char
            formatted_list.append(new_string)
            result = [[*element] for element in [''.join(list(item[1:-1])) for item in formatted_list]]
        return result
    # def convert_to_array(self,expression):
    #     terms = expression.strip("()").split(")|(")
    #     def convert_term(term):
    #         return [0 if char.isupper() else 1 for char in term]
    #     return [convert_term(term) for term in terms]
    def get_unique(self,result):
        unique_result = []
        for item in result:
            if isinstance(item, list) and len(item) == 1:
                if item not in unique_result:
                    unique_result.append(item)
            else:
                unique_item = tuple(sorted(item))
                if unique_item not in unique_result:
                    unique_result.append(unique_item)
        sorted_list = sorted(unique_result, key=lambda x: (str(x),) if isinstance(x, (list, tuple)) else (x,))
        return sorted_list
    
    def sort(self, input_list):
        result = []
        for item in input_list:
            if isinstance(item, str):
                result.append([item])
            else:
                sorted_item = sorted(item, key=lambda x: x.lower())
                result.append(sorted_item)

            result2 = []
            for item in result:
                if isinstance(item, str):
                    result2.append([item])
                else:
                    result2.append(list(item))

        return result2
    
    def print_table_c(self,):

        for i,elem in enumerate(self.carno):
            if elem==[0,0,0]:
                self.zero_array[0][0]=1
            if elem == [0,1,0]:
                self.zero_array[0][3]=1
            if elem ==[0,1,1]:
                self.zero_array[0][2]=1
            if elem ==[0,0,1]:
                self.zero_array[0][1]=1                    
            if elem ==[1,0,0]:
                self.zero_array[1][0]=1
            if elem ==[1,1,0]:
                self.zero_array[1][3]=1   
            if elem ==[1,1,1]:
                self.zero_array[1][2]=1
            if elem ==[1,0,1]:
                self.zero_array[1][1]=1      
        print(self.zero_array)
    
    def find_inter(self,input_data):
        result = []
        intersection_count = 0
        t_result = []
        unused_elements = input_data.copy()

        for i, element1 in enumerate(input_data):
            for j, element2 in enumerate(input_data):
                if i != j:
                    count = 0
                    otr_count = 0
                    t_result = []
                    for ind in range(len(element1)):
                        if len(element1) > ind and len(element2) > ind:
                            if element2[ind] == element1[ind]:
                                t_result.append(element1[ind])
                                count += 1

                            elif element2[ind] != element1[ind] and (element2[ind].upper() == element1[ind] or element2[ind].lower() == element1[ind]):
                                otr_count += 1
                    if count == len(element2) - 1 and otr_count == 1:
                        result.append(t_result)
                        intersection_count+=1
                        if element1 in unused_elements:
                            unused_elements.remove(element1)
                        if element2 in unused_elements:
                            unused_elements.remove(element2)
                        t_result = []

        if len(unused_elements) > 0:
            for elem in unused_elements:
                result.append(elem)
            result = self.replace_tuples_with_lists(result)    
        unique = self.get_unique(result)
        sorted = self.sort(unique)
        result = sorted            
        result = self.replace_tuples_with_lists(result)
        if intersection_count > 0:

            return self.find_inter(result)
        else:
            return result
        
    def replace_tuples_with_lists(self,input_list):
        result = []
        for item in input_list:
            if isinstance(item, tuple):
                result.append(list(item))
            elif isinstance(item, list):
                result.append(self.replace_tuples_with_lists(item))
            else:
                result.append(item)
        return result

    def calc_table_method(self):
        input_vars = self.minimaized_sdnf
        output_vars = self.listed_formula
        input_combinations = []
        for combination in input_vars:
            input_combinations.append(combination)

        truth_table = []
        for input_combo in input_combinations:
            row = []
            for output_combo in output_vars:
                row.append(int(all(elem in output_combo for elem in input_combo)))
            truth_table.append(row)
        headers = ["A, B, C"] + [", ".join(output_combo) for output_combo in output_vars]
        table = []
        for i, input_combo in enumerate(input_combinations):
            table.append([", ".join(input_combo)] + truth_table[i])
        print("Таблично-рассчетный метод:")
        print(tabulate(table, headers, tablefmt="grid"))

        single_one_inputs = []

        transposed_table = list(zip(*truth_table))

        for i, row in enumerate(truth_table):
            for j, value in enumerate(row):
                if value == 1 and transposed_table[j].count(1) == 1:
                    single_one_inputs.append(input_combinations[i])
                    break 

        ans = []
        for combo in single_one_inputs:
            ans.append(", ".join(combo))
        print(ans)
        self.calc_method = ans

    def convert_letters_to_numbers(self,nested_list):
        def convert_element(element):
            return 0 if element.isupper() else 1
        return [[convert_element(char) for char in sublist] for sublist in nested_list]

    def create_zero_array(self,input_list):
        num_rows = 2
        num_cols = 4
        zero_array = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        return zero_array

    def print_table(self):
        array = self.zero_array
        num_rows = len(array)
        num_cols = len(array[0])
        headers = ["a/bc", "00", "01", "11", "10"]
        print(f"| {' | '.join(headers)} |")
        print("+-------+----+----+----+----+")
        for i in range(num_rows):
            row_label = str(i)
            row_values = " | ".join(map(str, array[i]))
            print(f"|   {row_label}   | {row_values} |")









# a= Sdnf('(!a!b!c)|(!a!bc)|(!ab!c)|(a!b!c)|(a!bc)')  
# a.calc_table_method()
# a.print_table_c()
# a.print_table()
# print('Рассчетный метод: \n',a.minimaized_sdnf)



