class Binary:
    
    def __init__(self, number=None,reverse_code=None,complement_code=None):
        if number:
            self.number = number
            self.binary = self.decimal_to_binary()
            self.direct_code = self.binary_to_direct()
            self.reverse_code = self.binary_to_reverse()
            self.complement_code = self.binary_to_complement()
        if reverse_code:
            self.reverse_code = reverse_code
            self.direct_code = self.reverse_to_direct()
            self.number = self.direct_to_decimal()
            self.binary = self.decimal_to_binary()
            self.complement_code = self.binary_to_complement()
        if complement_code:
            self.complement_code = complement_code
            self.reverse_code = self.complement_to_reverse()
            self.direct_code = self.reverse_to_direct()
            self.number = self.direct_to_decimal()
            self.binary = self.decimal_to_binary()
            
    def __str__(self):
        return f"Number: {self.number}\nDirect Code:  {self.direct_code}\nReverse Code: {self.reverse_code}\nComplement Code:  {self.complement_code}"
    
    def decimal_to_binary(self):
        if self.number == 0:
            return '0'

        binary_result = ''
        temp_number = abs(self.number)
        while temp_number > 0:
            remainder = temp_number % 2
            binary_result = str(remainder) + binary_result
            temp_number //= 2
        return binary_result.zfill(8)  
    
    def binary_to_direct(self):
        
        if self.number >= 0:
            return self.binary
        else:
            direct_code = self.binary
            direct_code = direct_code.replace('0','1',1)
            return direct_code
    
    def binary_to_reverse(self):
        reverse_code = ''
        if self.number>=0:
            reverse_code = self.binary
            return reverse_code
        else:
            reverse_code = ''.join('0' if char == '1' else '1' for char in self.direct_code[1:])
            return '1'+reverse_code

    def binary_to_complement(self):
        
        complement_code = ''
        carry = 1  
        if self.number >=0:
            complement_code = self.binary
            return complement_code
        else:
            for bit in reversed(self.reverse_code):  
                if bit == '0' and carry == 1:
                    complement_code = '1' + complement_code
                    carry = 0
                elif bit == '1' and carry == 1:
                    complement_code = '0' + complement_code
                else:
                    complement_code = bit + complement_code
            return complement_code.zfill(8)  
    
    def reverse_to_direct(self):
        if self.reverse_code[0]=='0':
            self.direct_code= self.reverse_code
        else:
            self.direct_code= '1'+''.join('1' if bit == '0' else '0' for bit in self.reverse_code)[1:]
        return self.direct_code
    
    def direct_to_decimal(self):
        if self.direct_code[0]=='1':
            binary = '0'+ self.direct_code[1:]
            number = -int(binary,2)
        else:
            binary = self.direct_code
            number = int(binary,2)
        self.number = number
        return self.number

    def check(self,result):
        while 2 in result:
            carry = 1
            for i,num in enumerate(result):
                if 2 in result:
                    if num ==2 and carry == 1:
                        if i == len(result)-1:
                            result[i]==0
                            result[0]+=1
                        else:
                            result[i]=0
                            result[i+1]+=1
                    if num ==0 and carry ==1:
                        result[i]=1
                        carry = 0
            return result
    
        
    def __add__(self, other):
        if isinstance(other, Binary):
            carry = 0
            result = []
            self_reverse = list(map(int,self.reverse_code[::-1]))
            other_reverse = list(map(int,other.reverse_code[::-1]))
            
            for i,(a, b) in enumerate(zip(self_reverse, other_reverse)):
                digit_sum = a + b 
                if a+b ==2 and carry ==0:
                    if i ==len(self_reverse)-1:
                        result.append(0)
                        carry =0
                        result[0]+=1
                    else:
                        result.append(0)
                        carry = 1
                elif a+b ==2 and carry ==1:
                    if i == len(self_reverse)-1:
                        result.append(1)
                        result[0]+=1
                    else:        
                        result.append(1)
                elif a +b ==1 and carry ==1:
                    if i ==len(self_reverse)-1:
                        result.append(0)
                        carry =0
                        result[0]+=1
                    else:
                        result.append(0)
                elif a+b ==1 and carry ==0:
                    result.append(1)
                elif a+b ==0 and carry ==1:
                    result.append(1)
                    carry =0
                elif a+b ==0 and carry ==0:
                    result.append(0)
                    
            if 2 in result:# if 2 in result: !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                result =self.check(result)
                result = ''.join(map(str,result[::-1]))
            else:result = ''.join(map(str,result[::-1]))
        return Binary(reverse_code=result) 
    
    def __mul__(self, other):
        if isinstance(other, Binary):
            result = 0
            for i in range (8):
                first_bit = int(self.binary[7-i])
                for j in range(8):
                    second_bit = int(other.binary[7-j])
                    result += first_bit *second_bit*(2**(i+j))
            if self.number>0 and  other.number <0 or self.number <0 and other.number >0:
                result = -result
            else:
                pass
            return Binary(result)
        else:
            raise TypeError("Unsupported operand type for *")
    
    def __truediv__(self, other ):
        if isinstance(other,Binary):
            quotient = ''
            precision = 5
            remainder = ''
            temp_dividend = ''
            dividend = self.direct_code[1:]
            divisor = other.direct_code[1:]
            for digit in dividend:
                temp_dividend += digit
                if int(temp_dividend, 2) >= int(divisor, 2):
                    quotient += '1'
                    temp_dividend = bin(int(temp_dividend, 2) - int(divisor, 2))[2:]
                else:
                    quotient += '0'     
            quotient += '.'     
            for _ in range(precision):
                temp_dividend += '0'
                if int(temp_dividend, 2) >= int(divisor, 2):
                    quotient += '1'
                    temp_dividend = bin(int(temp_dividend, 2) - int(divisor, 2))[2:]
                else:
                    quotient += '0'
            if self.number * other.number >=0:
                sign = '0'
            else: sign = '1'
            quotient =quotient.zfill(13)
            quotient = sign + quotient            
        else:
            raise TypeError("Unsupported operand type for / ")
        return quotient     

    
class FloatingPoint:
    exponent = 0
    def __init__(self, number=None):
        if number is not None:
            self.number = number
            self.mantissa =''
            self.exponent = 0
            if abs(self.number)<1:
                self.integer_part = '00000000'
            else:
                self.integer_part = self.decimal_to_binary(number)
            self.number = number
            self.fractional_part = self.get_fractional_part(number)
            self.float = self.float_to_binary_representation(number) 
            self.scientific_notation = self.shift_point_to_range()
            self.result = self.get_bin_result()
            self.bin_expo = self.decimal_to_binary(self.exponent)
            self.res_len = len(self.result)
            self.full_mantissa = '1'+self.mantissa
            
        else:
            self.binary_representation = None
            self.number = None
            
    def __str__(self):
        return f"Value: {self.number}\nBinary Representation:\n {self.result}"
            
    # def __add__(self, other):
    #     if isinstance(other, FloatingPoint):
    #         result_binary = self.binary_addition(self.binary_representation, other.binary_representation)
    #         result_value = self.binary_to_float(result_binary)
    #         return FloatingPoint(result_value)
        
    def decimal_to_binary(self,number):
        if  number == 0:
            return '0'
        
        binary_result = ''
        temp_number = int(number)
        
        while temp_number > 0:
            if temp_number < 2:
                remainder = str(int(temp_number))
                binary_result = remainder+ binary_result
                return binary_result.zfill(8)
            else:
                remainder = temp_number % 2
                binary_result = str(remainder) + binary_result
                temp_number //= 2
        return binary_result.zfill(8)
        
    
    def get_fractional_part(self,number, precision=5):
        number = abs(number)
        fl_part = round(number - int(number), precision)

        result = ''
        counter = 0
        while fl_part != 0 and counter < 23:

            fl_part=round(fl_part,5)
            fl_part *= 2
            result += str(int(fl_part))
            fl_part -= int(fl_part)
            counter+=1

        return result

    def float_to_binary_representation(self,number,percisoin = 5):

        if number<0:
            sign = '1'
        else:
            sign = '0'
        number = abs(number)
        fractional_part = self.fractional_part.ljust(23, '0')
        exponent = self.decimal_to_binary(int(number))
        result =exponent+ '.'  +fractional_part
        return result
    def print(self):
        print(f"Result:  {self.result} \nfractional part:  {self.fractional_part} \nresult length:  {len(self.float)} \n integer part: {self.integer_part} \n scientific notation {self.scientific_notation} " )

    def shift_point_to_range(self):
        number = self.float
        dot_index = number.find('.')
        is_less = False
        if dot_index == -1:
            dot_index = len(number)
            number += '.'
        if float(number) >2:
            while not is_less:
                number = list(number)
                number[dot_index],number[dot_index-1] = number[dot_index-1],number[dot_index]
                dot_index-=1
                self.exponent +=1
                number = ''.join(number)
                
                if float(number)>1 and float(number)<2:
                    is_less = True
                    self.exponent+=127
                    index = 0
                    while number[index]!='1':
                        index+=1
                        
                    self.mantissa = number[index+2::]
                    mantissa = self.mantissa
                    while len(mantissa)!=23:
                        if len(mantissa)>23:
                            mantissa = mantissa[:-1]
                        if len(mantissa)<23:
                            mantissa = mantissa + '0'
                    self.mantissa = mantissa
                    return number
        elif float(number) <1 :
            while not is_less:
                number= list(number)
                number[dot_index],number[dot_index+1] = number[dot_index+1],number[dot_index]
                dot_index+=1
                self.exponent -=1
                number = ''.join(number)
                if float(number)>=1:
                    number = number[1::]
                    is_less = True
                    self.exponent+=127
                    index = 0
                    while number[index]!='1':
                        index+=1
                        
                    self.mantissa = number[index+2::]
                    while len(self.mantissa)!=23:
                        if len(self.mantissa)>23:
                            self.mantissa = self.mantissa[:-1]
                        if len(self.mantissa)<23:
                            self.mantissa = self.mantissa + '0'
                    return number
        else:
            index = 0
            while number[index]!='1':
                index+=1
                
            self.mantissa = number[index+2::]

            while len(self.mantissa)!=23:
                if len(self.mantissa)>23:
                    self.mantissa = self.mantissa[:-1]
                if len(self.mantissa)<23:
                    self.mantissa = self.mantissa + '0'
            self.exponent+=127
            return number
        
    def get_bin_result(self):
        expo = self.decimal_to_binary(self.exponent)
        if self.number>=0:
            sign_bit = '0'
        else:
            sign_bit = '1'
        result = sign_bit+expo+self.mantissa
        return result
    
    def shift_in_adding_floats(self,number,new_exp):
        
        dot_index = len(number)-23    # -23
        number = list(number)
        number.insert(dot_index,'.')
        number = ''.join(number)
        is_less = False
        if dot_index == -1:
            dot_index = len(number)
            number += '.'
        if float(number) >2:
            while not is_less:
                number = list(number)
                number[dot_index],number[dot_index-1] = number[dot_index-1],number[dot_index]
                dot_index-=1
                new_exp +=1
                number = ''.join(number)
                
                if float(number)>1 and float(number)<2:
                    is_less = True
                    #self.exponent+=127
                    index = 0
                    while number[index]!='1':
                        index+=1
                        
                    number = number[index+2::]
                    
                    while len(number)!=23:
                        if len(number)>23:
                            number = number[:-1]
                        elif len(number)<23:
                            number = number + '0'
                    new_exp = self.decimal_to_binary(new_exp)
                    number = new_exp+number
                    return number
        if float(number) <1:
            while not is_less:
                number= list(number)
                number[dot_index],number[dot_index+1] = number[dot_index+1],number[dot_index]
                dot_index+=1
                new_exp -=1
                number = ''.join(number)
                if float(number)>1 and float(number)<2:
                    number = number[1::]
                    is_less = True
                    #self.exponent+=127
                    index = 0
                    while number[index]!='1':
                        index+=1
                        return index
                    number = number[index+2::]
                    while len(number)!=23:
                        if len(number)>23:
                            number = number[:-1]
                        elif len(number)<23:
                            number = number + '0'
                    new_exp = self.decimal_to_binary(new_exp)
                    number = new_exp+number
                    return number
        else:
            index = 0
            while number[index]!='1':
                index+=1
                return index
            number = number[index+2::]
            while len(number)!=23:
                if len(number)>23:
                    number = number[:-1]
                elif len(number)<23:
                    number = number + '0'
            new_exp = self.decimal_to_binary(new_exp)
            number = new_exp+number
            return number

    def check(self,result):
        while 2 in result:
            carry = 1
            for i,num in enumerate(result):
                if 2 in result:
                    if num ==2 and carry == 1:
                        if i == len(result)-1:
                            result[i]=0
                            result.append(1)
                        else:
                            result[i]=0 
                            result[i+1]+=1
                    if num ==0 and carry ==1:
                        result[i]=1
                        carry = 0
        return result

    def __add__(self, other):
        if isinstance(other, FloatingPoint):
            if self.number+other.number >=0:
                sign_bit = '0'
            else:
                sign_bit='1'
            new_exp = max(other.exponent,self.exponent)
            bits_before_point = 1
            
            self_mantissa=''
            other_mantissa = ''
            exp_shift = abs(other.exponent-self.exponent)
            if other.exponent<self.exponent:
                other_mantissa = other.full_mantissa
                other_mantissa = other_mantissa.zfill(24+exp_shift)[:-(exp_shift)]
                #other_mantissa = other_mantissa[:-exp_shift]
                self_mantissa = self.full_mantissa
            elif other.exponent>self.exponent:
                self_mantissa = self.full_mantissa
                self_mantissa = self_mantissa.zfill(24+exp_shift)[:-(exp_shift)]   #self_mantissa = self_mantissa.zfill(24+exp_shift)[:-exp_shift]
                other_mantissa = other.full_mantissa
                print(len(self_mantissa),len(other_mantissa))
            else:
                self_mantissa = self.full_mantissa
                other_mantissa = other.full_mantissa
            carry = 0
            result = []
            self_reverse = list(map(int,self_mantissa[::-1]))
            other_reverse = list(map(int,other_mantissa[::-1]))
            
            for i,(a, b) in enumerate(zip(self_reverse, other_reverse)):
                digit_sum = a + b 
                if a+b ==2 and carry ==0:
                    if i ==len(self_reverse)-1:
                        result.append(0)
                        carry =0
                        result.append(1)
                    else:
                        result.append(0)
                        carry = 1
                elif a+b ==2 and carry ==1:
                    if i == len(self_reverse)-1:
                        result.append(1)
                        result.append(1)
                    else:        
                        result.append(1)
                elif a +b ==1 and carry ==1:
                    if i ==len(self_reverse)-1:
                        result.append(0)
                        carry =1  #0
                        result.append(1)
                    else:
                        result.append(0)
                elif a+b ==1 and carry ==0:
                    result.append(1)
                elif a+b ==0 and carry ==1:
                    result.append(1)
                    carry =0
                elif a+b ==0 and carry ==0:
                    result.append(0)
                    
            if 2 in result:
                result =self.check(result)
                result = ''.join(map(str,result[::-1]))
            else:result = ''.join(map(str,result[::-1]))
                
                
        result = self.shift_in_adding_floats(result,new_exp)
        
        
        result = sign_bit  + result
        return result 
    


fl1 = FloatingPoint(17.5)
fl2 = FloatingPoint(10.5)
print(fl1.result)
print(fl2.result)
c = fl1 + fl2
print(c)



