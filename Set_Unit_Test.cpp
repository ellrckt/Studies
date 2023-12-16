#include "pch.h"
#include "CppUnitTest.h"
#include "./../PPois_1/Set.h";
#include "./../PPois_1/Set.cpp";




#include <vector>
#include <string> 
#include <algorithm>
using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace SetUnitTest
{
	TEST_CLASS(SetUnitTest)
	{
	public:
		
		
		TEST_METHOD(AddElement)
		{
			Set testSet;
			int num = 1;
			string str = "apple";
			testSet.add(str);

			
			Assert::AreEqual(num, testSet.power());  
			Assert::IsTrue(testSet.contains(str));

			
		}
		
		TEST_METHOD(AddChar)
		{
		
			Set testSet;

			int num = 1;
			char ch = 'a';
			testSet.add(ch);

			
			Assert::AreEqual(num, testSet.power());
			Assert::IsTrue(testSet.contains(ch));

			
		}
		TEST_METHOD(IsEmpty)
		{
			Set set;
			Assert::IsTrue(set.IsEmpty());
		}

		TEST_METHOD(IsEmpty2)
		{
			Set set;
			set.add("A");
			Assert::IsFalse(set.IsEmpty());
		}

		TEST_METHOD(IsEmpty3)
		{
			Set set;
			set.add("A");
			set.del(1);
			Assert::IsTrue(set.IsEmpty());
		}

		TEST_METHOD(IsEmpty4)
		{
			Set set;
			set.add("A");
			set.add("B");
			Assert::IsFalse(set.IsEmpty());
		}
		TEST_METHOD(ТестExtractSet)
		{
			Set set;
			int i = 0;
			std::string input = "{1, 2, 3}";
			std::string expected = "{1";
			Assert::AreEqual(expected, set.extractSet(input, i));
		}

		TEST_METHOD(ТестProcessSet)
		{
			int num = 1;
			Set set;
			int i = 0;
			std::string input = "{{1, 2, 3}, {4, 5, 6}}";
			set.processSet(input, i);
			Assert::AreEqual(num, set.power());
		}
		TEST_METHOD(Constructor1)
		{
			
			std::string str1 = "a";
			std::string str2 = "b";
			std::string str3 = "c";
			

		
			Set set;
			set.add(str1);
			set.add(str2);
			set.add(str3);

		
			Assert::IsFalse(set.IsEmpty());
			Assert::AreEqual(3, set.power());
		}

		TEST_METHOD(DefaultConstructor)
		{
			
			Set set;

		
			Assert::IsTrue(set.IsEmpty());
			Assert::AreEqual(0, set.power());
		}
		TEST_METHOD(DelElement)
		{
		
			Set set;
			set.add("A");
			set.add("B");
			set.add("C");

		
			std::string deletedElement = set.del(2);

		
			Assert::AreEqual("B", deletedElement.c_str());
			Assert::AreEqual(2, set.power()); 
			Assert::IsFalse(set.contains("B"));
		}
		TEST_METHOD(Power1)
		{
			Set set;
			set.add("A");
			set.add("B");
			set.add("C");

			int count = set.power();

			Assert::AreEqual(3, count);
		}

		TEST_METHOD(Power2)
		{
			Set set;

			int count = set.power();

			Assert::AreEqual(0, count);
		}
		TEST_METHOD(Contains1)
		{
			Set set;
			set.add("A");
			set.add("B");
			set.add("C");

			bool result = set.contains("B");

			Assert::IsTrue(result);
		}

		TEST_METHOD(Contains2)
		{
			Set set;
			set.add("A");
			set.add("B");
			set.add("C");

			bool result = set.contains("D");

			Assert::IsFalse(result);
		}

		TEST_METHOD(Contains3)
		{
			Set set;

			bool result = set.contains("A");

			Assert::IsFalse(result);
		}
		TEST_METHOD(Containschar1)
		{
			Set set;
			set.add("A");
			set.add("B");
			set.add("C");

			bool result = set.contains('B');

			Assert::IsTrue(result);
		}

		TEST_METHOD(Containschar2)
		{
			Set set;
			set.add("A");
			set.add("B");
			set.add("C");

			bool result = set.contains('D');

			Assert::IsFalse(result);
		}

		TEST_METHOD(Containschar3)
		{
			Set set;

			bool result = set.contains('A');

			Assert::IsFalse(result);
		}
		TEST_METHOD(OperatorBracket1)
		{
			Set set;
			set.add("A");
			set.add("B");
			set.add("C");

			bool result = set["B"];

			Assert::IsTrue(result);
		}

		TEST_METHOD(OperatorBracket2)
		{
			Set set;
			set.add("A");
			set.add("B");
			set.add("C");

			bool result = set["D"];

			Assert::IsFalse(result);
		}

		TEST_METHOD(OperatorBracket3)
		{
			Set set;

			bool result = set["A"];

			Assert::IsFalse(result);
		}
		 TEST_METHOD(OperatorBracket4)
        {
            Set set;
            set.add("A");
            set.add("B");
            set.add("C");

            bool result = set["B"];

            Assert::IsTrue(result);
        }

        TEST_METHOD(OperatorBracket5)
        {
            Set set;
            set.add("A");
            set.add("B");
            set.add("C");

            bool result = set["D"];

            Assert::IsFalse(result);
        }

        TEST_METHOD(OperatorBracket6)
        {
            Set set;

            bool result = set["A"];

            Assert::IsFalse(result);
        }
		TEST_METHOD(OperatorPlus1)
		{
			Set set1;
			set1.add("A");
			set1.add("B");
			set1.add("C");

			Set set2;
			set2.add("B");
			set2.add("C");
			set2.add("D");

			Set result = set1 + set2;

	
			Assert::AreEqual(4, result.power());
			Assert::IsTrue(result["A"]);
			Assert::IsTrue(result["B"]);
			Assert::IsTrue(result["C"]);
			Assert::IsTrue(result["D"]);
		}

		TEST_METHOD(OperatorPlus2)
		{
			Set set1;
			set1.add("A");
			set1.add("B");

			Set set2; 

		
			Set result = set1 + set2;

	
			Assert::AreEqual(2, result.power());
			Assert::IsTrue(result["A"]);
			Assert::IsTrue(result["B"]);
		}
		TEST_METHOD(OperatorPlusEqual1)
		{
			Set set1;
			set1.add("A");
			set1.add("B");

			Set set2;
			set2.add("B");
			set2.add("C");

		
			set1 += set2;

		
			Assert::AreEqual(3, set1.power());
			Assert::IsTrue(set1["A"]);
			Assert::IsTrue(set1["B"]);
			Assert::IsTrue(set1["C"]);
		}

		TEST_METHOD(OperatorPlusEqual2)
		{
			Set set1;
			set1.add("A");
			set1.add("B");

			Set set2; 

		
			set1 += set2;

		
			Assert::AreEqual(2, set1.power());
			Assert::IsTrue(set1["A"]);
			Assert::IsTrue(set1["B"]);
		}
		TEST_METHOD(OperatorMultiply1)
		{
			Set set1;
			set1.add("A");
			set1.add("B");
			set1.add("C");

			Set set2;
			set2.add("B");
			set2.add("C");
			set2.add("D");

			Set result = set1 * set2;

			Assert::AreEqual(2, result.power());
			Assert::IsTrue(result["B"]);
			Assert::IsTrue(result["C"]);
		}

		TEST_METHOD(OperatorMultiply2)
		{
			Set set1;
			set1.add("A");
			set1.add("B");

			Set set2;
			set2.add("C");
			set2.add("D");

			Set result = set1 * set2;

			Assert::AreEqual(0, result.power());
		}
		TEST_METHOD(OperatorMultiplyEqual1)
		{
			Set set1;
			set1.add("A");
			set1.add("B");
			set1.add("C");

			Set set2;
			set2.add("B");
			set2.add("C");
			set2.add("D");

			set1 *= set2;

			Assert::AreEqual(2, set1.power());
			Assert::IsTrue(set1["B"]);
			Assert::IsTrue(set1["C"]);
		}

		TEST_METHOD(OperatorMultiplyEqual2)
		{
			Set set1;
			set1.add("A");
			set1.add("B");

			Set set2;
			set2.add("C");
			set2.add("D");

			set1 *= set2;

			Assert::AreEqual(0, set1.power());
		}
		TEST_METHOD(OperatorMinus1)
		{
			Set set1;
			set1.add("A");
			set1.add("B");
			set1.add("C");

			Set set2;
			set2.add("B");
			set2.add("C");
			set2.add("D");

			Set result = set1 - set2;

			Assert::AreEqual(1, result.power());
			Assert::IsTrue(result["A"]);
		}

		TEST_METHOD(OperatorMinus2)
		{
			Set set1;
			set1.add("A");
			set1.add("B");

			Set set2;
			set2.add("C");
			set2.add("D");

			Set result = set1 - set2;

			Assert::AreEqual(2, result.power());
			Assert::IsTrue(result["A"]);
			Assert::IsTrue(result["B"]);
		}
		TEST_METHOD(OperatorMinusEqual1)
		{
			Set set1;
			set1.add("A");
			set1.add("B");
			set1.add("C");

			Set set2;
			set2.add("B");
			set2.add("C");
			set2.add("D");

			set1 -= set2;

			Assert::AreEqual(1, set1.power());
			Assert::IsTrue(set1["A"]);
		}

		TEST_METHOD(OperatorMinusEqual2)
		{
			Set set1;
			set1.add("A");
			set1.add("B");

			Set set2;
			set2.add("C");
			set2.add("D");

			set1 -= set2;

			Assert::AreEqual(2, set1.power());
			Assert::IsTrue(set1["A"]);
			Assert::IsTrue(set1["B"]);
		}
	};
}
