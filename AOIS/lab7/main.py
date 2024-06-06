class Matrix:
    def __init__(self):
        self.table = [
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ];
    
    def __str__(self):
        str = ''
        for i in self.table:
            str+=f"{i}\n"
        return '16x16 Matrix: \n'+str   
    
    def get_adress(self,num_of_word):
        word = ''
        sec_ind = 16 - num_of_word
        for offset in range(0, 16 - num_of_word):
            i = num_of_word + offset
            j = offset
            if i < 16 and j < 16:
                word += str(self.table[i][j])
        for offset in range(0, num_of_word):
            i = offset
            j = sec_ind + offset
            if i < 16 and j < 16:
                word += str(self.table[i][j])
        print(f'Word №{num_of_word}',word)
        return word
    
    def find_matching_columns_anywhere(self, key):
        key_length = len(key)
        matching_columns = []   
        for col in range(len(self.table[0])):
            for start_row in range(len(self.table) - key_length + 1):
                match = True
                for k in range(key_length):
                    if self.table[start_row + k][col] != int(key[k]):
                        match = False
                        break
                if match:
                    matching_columns.append((col, start_row))
                    break 
        print(matching_columns)
        return matching_columns

    def summ_of_fields(self,matching_columns):
        for i in matching_columns:
            for j in i:
                self.get_word()
        
    def get_word(self,num_of_word):
        sec_ind = 16 - num_of_word
        word = ''
        for i in range(num_of_word,16):
            j = num_of_word
            word+=str(self.table[i][j])
        for i in range(0,num_of_word):
            j = num_of_word
            word+=str(self.table[i][j])
        return word

    def find_combination(self, combination):
        words_with_combination = []
        for num_of_word in range(16):
            word = ''.join(str(self.table[i][num_of_word]) for i in range(16))
            if combination in word:
                words_with_combination.append(num_of_word)
        print(words_with_combination)
        return words_with_combination

        
    def summ(self,combo):
        
        matching_columns = self.find_combination(combo)
        for i in matching_columns:
            updated = ''
            str1 = self.get_word(i)
            V = str1[0:3]  
            A = str1[3:7] 
            B = str1[7:11]  
            S = str1[11:16] 
            print(f'S = {S},B = {B}, A = {A}')
            a_int = int(A,2)
            b_int = int(B,2)
            s_int = a_int+b_int
            s_bin = bin(s_int)[2:].zfill(5)
            if len(s_bin) > 5:
                s_bin = s_bin[-5:]
            updated = str1[:-5] + s_bin
            print(str1)
            print(updated)
        
    def bitwise_and(self,first_num,second_num,word_num_to_insert):
        
        str1 = self.get_word(first_num)
        str2 = self.get_word(second_num)
        if len(str1) != len(str2):
            raise ValueError("Строки должны быть одинаковой длины")
        result = ''
        for ch1, ch2 in zip(str1, str2):
            result += '1' if ch1 == '1' and ch2 == '1' else '0'
        print(result)
        self.insert_word(word_num_to_insert,result)
        return result
    
    def find_closest_above(self, row_index, column_index, search_str):

        matrix = self.table
        if len(search_str) > len(matrix):
            raise ValueError("Строка поиска длиннее количества строк в матрице")

        search_length = len(search_str)

        for i in range(row_index - 1, -1, -1):
            match = True
            for k in range(search_length):
                if i - k < 0 or matrix[i - k][column_index] != int(search_str[search_length - 1 - k]):
                    match = False
                    break
            if match:
                print(f'Совпадение найдено в строке{row_index} столбце {column_index} начиная с {column_index} до {i-search_length}')
                
                return i - search_length + 1  

    def find_closest_below(self, row_index, column_index, search_str):

        matrix = self.table
        if len(search_str) > len(matrix):
            raise ValueError("Строка поиска длиннее количества строк в матрице")

        search_length = len(search_str)

        for i in range(row_index, len(matrix)):
            match = True
            for k in range(search_length):
                if i + k >= len(matrix) or matrix[i + k][column_index] != int(search_str[k]):
                    match = False
                    break
            if match:
                print(f'Совпадение найдено в строке {row_index} столбце {column_index} начиная с {i} до {i+len(search_str)-1}')
                return i 
        return None  
    
    def insert_word(self,num_of_word,word):
        k = 0
        sec_ind = 16-num_of_word
        for i in range(num_of_word,16):
            j = num_of_word
            self.table[i][j]=int(word[k])
            k+=1
        for i in range(0,num_of_word):
            j = num_of_word
            self.table[i][j]=int(word[k])
            k+=1

    def bitwise_not(self,word,num_to_insert):
        
        binary_str = self.get_word(word)
        result = ''
        for ch in binary_str:
            result += '1' if ch == '0' else '0'
        print(result)
        self.insert_word(num_to_insert,result)
        return result
        
    def bitwise_nand(self,first_num, second_num,num_to_insert):
        
        str1 = self.get_word(first_num)
        str2 = self.get_word(second_num)
        if len(str1) != len(str2):
            raise ValueError("Строки должны быть одинаковой длины")
        result = ''
        for ch1, ch2 in zip(str1, str2):
            result += '0' if ch1 == '1' and ch2 == '1' else '1'
        print(result)
        self.insert_word(num_to_insert,result)
        return result
        
    def repeat_1_argyment(self,first_word,second_word,num_of_word):
        first_word = self.get_word(first_word)
        second_word = self.get_word(second_word)
        second_word = first_word
        print("Второе слово после преобразования: ",second_word)
        self.insert_word(num_of_word,second_word)
a = Matrix()
print(a)
a.insert_word(3,'0000000000000000')
print(a)
print(a.get_adress(3))
word2 = a.get_word(2)
print(word2)
print(a)
print('Отрицание')
print(a.get_word(0))
a.bitwise_not(0,4)
print('повтор первого аргумента')
print(a.get_word(3))
print(a.get_word(2))
a.repeat_1_argyment(3,2,3)
print('коньюкция')
print(a.get_word(2))
print(a.get_word(3))
a.bitwise_and(2,3,0)
print('Отрицание Шеффера')
print(a.get_word(15))
print(a.get_word(14))
a.bitwise_nand(15,14,0)
a.find_closest_above(15,6,'010')
a.find_closest_below(0,5,'1010')
a.summ('111')

