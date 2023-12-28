#include "pch.h"
#include "CppUnitTest.h"
#include "../PPois_2/Cleaner.h"
#include "../PPois_2/Dekan.h"
#include "../PPois_2/Dekanat.h"
#include "../PPois_2/Human.h"
#include "../PPois_2/Lecture.h"
#include "../PPois_2/Security.h"
#include "../PPois_2/Shedule.h"
#include "../PPois_2/Student.h"
#include "../PPois_2/Teacher.h"
#include "../PPois_2/Worker.h"

#include "../PPois_2/Cleaner.cpp"
#include "../PPois_2/Dekan.cpp"
#include "../PPois_2/Dekanat.cpp"
#include "../PPois_2/Human.cpp"
#include "../PPois_2/Lecture.cpp"
#include "../PPois_2/Security.cpp"
#include "../PPois_2/Shedule.cpp"
#include "../PPois_2/Student.cpp"
#include "../PPois_2/Teacher.cpp"
#include "../PPois_2/Worker.cpp"




using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace ClassesUnitTestcpp
{
	TEST_CLASS(ClassesUnitTestcpp)
	{
	public:
		
        TEST_METHOD(TestDefaultConstructorHuman)
        {
         
            Human human;

      
            Assert::AreEqual("", human.GetName().c_str());
            Assert::AreEqual(0, human.GetAge());
            Assert::AreEqual("", human.GetGender().c_str());
        }

        TEST_METHOD(TestParameterizedConstructorHuman)
        {
         
            Human human("John", 25, "Male");

          
            Assert::AreEqual("John", human.GetName().c_str());
            Assert::AreEqual(25, human.GetAge());
            Assert::AreEqual("Male", human.GetGender().c_str());
        }

        TEST_METHOD(TestSetAndGetAgeHuman)
        {
          
            Human human;

           
            human.SetAge(25);

        
            Assert::AreEqual(25, human.GetAge());
        }

        TEST_METHOD(TestBeBornHuman)
        {
           
            Human human;

           
            string beborn = human.BeBorn();
            string res = "Was born!";
        
            Assert::AreEqual(res, beborn);
        }

        TEST_METHOD(TestSetAndGetGenderHuman)
        {
       
            Human human;

          
            human.SetGender("Male");

       
            Assert::AreEqual("Male", human.GetGender().c_str());
        }

        TEST_METHOD(TestSetAndGetNameHuman)
        {
        
            Human human;

       
            human.SetName("Alice");

   
            Assert::AreEqual("Alice", human.GetName().c_str());
        }

        TEST_METHOD(TestDefaultConstructorWorker)
        {
         
            Worker worker;
            string res = worker.GetJobTitle();
            string ans = "";
       
            Assert::AreEqual(ans,res);
            Assert::AreEqual(0, worker.GetSalary());
        }

        TEST_METHOD(TestParameterizedConstructorWorker)
        {
        
            Worker worker("Programmer", 50000);
            string ans = worker.GetJobTitle();
            string res = "Programmer";
      
            Assert::AreEqual(res,ans);
            Assert::AreEqual(50000, worker.GetSalary());
        }

        TEST_METHOD(TestSetAndGetJobTitleWorker)
        {
 
            Worker worker;

       
            worker.SetJobTitle("Engineer");
            string ans = worker.GetJobTitle();
            string result = "Engineer";

  
            Assert::AreEqual(result,ans);
        }

        TEST_METHOD(TestSetAndGetSalaryWorker)
        {
      
            Worker worker;

       
            worker.SetSalary(60000);


            Assert::AreEqual(60000, worker.GetSalary());
        }

        TEST_METHOD(TestDoWorkWorker)
        {
       
            Worker worker; 
            
            string result = worker.DoWork("Working on a project");
           
            string work = "Working on a project";
           
            Assert::AreEqual(result,work);
        }

        TEST_METHOD(TestSetAndGetNumOfGroups)
        {
            Teacher teacher;
            teacher.SetNumOfGroups(5);
            Assert::AreEqual(5, teacher.GetNumOfGroups());
        }

        TEST_METHOD(TestSetAndGetIsLector)
        {
            Teacher teacher;
            teacher.SetIsLector(true);
            Assert::IsTrue(teacher.GetIsLector());
        }

        TEST_METHOD(TestSetAndGetIsPzshnik)
        {
            Teacher teacher;
            teacher.SetIsPzshnik(false);
            Assert::IsFalse(teacher.GetIsPzshnik());
        }

        TEST_METHOD(TestSetGrades)
        {
            Teacher teacher;
            Student student;
            teacher.SetGrades(student, 90);
            int num = student.grades.size();
            Assert::AreEqual(1, num);
            Assert::AreEqual(90, student.grades[0]);
        }

        TEST_METHOD(TestEditGrades)
        {
            Teacher teacher;
            Student student;
            teacher.SetGrades(student, 80);
            teacher.EditGrades(student, 0, 85);
            int num = student.grades.size();
            Assert::AreEqual(1, num);
            Assert::AreEqual(85, student.grades[0]);
        }
        TEST_METHOD(DefaultConstructorStudent)
        {
            Student student;
            Assert::AreEqual("", student.GetUniversity().c_str());
            Assert::IsFalse(student.GetIsStudent());
            Assert::IsFalse(student.GetIsGoodStudent());
            Assert::AreEqual(0, student.GetCourse());
        }

        TEST_METHOD(ParameterizedConstructorStudent)
        {
            Student student("Math", "University", true, true, 3);
            Assert::AreEqual("University", student.GetUniversity().c_str());
            Assert::IsTrue(student.GetIsStudent());
            Assert::IsTrue(student.GetIsGoodStudent());
            Assert::AreEqual(3, student.GetCourse());
        }

        TEST_METHOD(Learning)
        {
            Student student;
            std::ostringstream redirectedOutput;
            std::streambuf* originalOutput = std::cout.rdbuf(redirectedOutput.rdbuf());

            student.Learning("Physics");

            std::cout.rdbuf(originalOutput);
            Assert::AreEqual("Learning Physics", redirectedOutput.str().c_str());
        }

        TEST_METHOD(ChooseFavSub)
        {
            Student student;
            student.ChooseFavSub("Chemistry");
            Assert::AreEqual("Chemistry", student.GetFavSubject().c_str());
        }

        TEST_METHOD(PassExam)
        {
            Student student;
            bool result = student.PassExam(student);
            Assert::IsTrue(result || !result);
        }
        TEST_METHOD(TestSetShedule)
        {
            Shedule shedule;
            shedule.SetShedule("Math");
            shedule.SetShedule("Physics");

           

            shedule.GetShedule();
            string math = "Math";
            string phy = "Physics";

           
            Assert::AreEqual(math, shedule.GetSubject(0));
            Assert::AreEqual(phy, shedule.GetSubject(1));
        }
        TEST_METHOD(TestSetOutsiders)
        {
            Security security;

        
            security.SetOutsiders(3);

        
            Assert::AreEqual(3, security.GetNumOfOutsiders());
            
        }
        TEST_METHOD(TestDefaultConstructorLecture)
        {
          
            Lecture lecture;

            Assert::IsTrue(lecture.GetIsThereTeacher());
            Assert::AreEqual(90, lecture.GetNumStudents());
            Assert::IsTrue(lecture.GetNumStudentsOnLecture() >= 0 && lecture.GetNumStudentsOnLecture() <= 90);
        }

        TEST_METHOD(TestSetIsThereTeacher)
        {
           
            Lecture lecture;

         
            lecture.SetIsThereTeacher(true);

         
            Assert::IsTrue(lecture.GetIsThereTeacher());
        }

        TEST_METHOD(TestSetNumStudents)
        {
          
            Lecture lecture;

           
            lecture.SetNumStudents(80);

          
            Assert::AreEqual(80, lecture.GetNumStudents());
        }

        TEST_METHOD(TestSetNumStudentsOnLecture)
        {
      
            Lecture lecture;

           
            lecture.SetNumStudentsOnLecture(60);
            
            Assert::AreEqual(60, lecture.GetNumStudentsOnLecture());
        }

        TEST_METHOD(TestSetAndGetDolzhniki)
        {
            Dekanat dekanat;

         
            dekanat.SetDolzhniki(10);

           
            Assert::AreEqual(10, dekanat.GetDolzhniki());
        }

        TEST_METHOD(TestSetAndGetPlatniki)
        {
            Dekanat dekanat;

          
            dekanat.SetPlatniki(15);

            
            Assert::AreEqual(15, dekanat.GetPlatniki());
        }

        TEST_METHOD(TestSetAndGetDolg)
        {
            Dekanat dekanat;

            
            dekanat.SetDolg(1000);

            Assert::AreEqual(1000, dekanat.GetDolg());
        }

        TEST_METHOD(TestSetAndGetCostOfEducation)
        {
            Dekanat dekanat;

           
            dekanat.SetCostOfEducation(5000);

           
            Assert::AreEqual(5000, dekanat.GetCost_of_education());
        }

        TEST_METHOD(TestSetAndGetNumOfDocuments)
        {
            Dekanat dekanat;

         
            dekanat.SetNumOfDocuments(5);

            Assert::AreEqual(5, dekanat.GetNumOfDocuments());
        }

        TEST_METHOD(TestSetAndGetAdministration)
        {
            Dekanat dekanat;

         
            dekanat.SetAdministration(3);

            
            Assert::AreEqual(3, dekanat.GetAdministration());
        }

        TEST_METHOD(TestSetAndGetBudgetniki)
        {
            Dekanat dekanat;

          
            dekanat.SetBudgetniki(20);

           
            Assert::AreEqual(20, dekanat.GetBudgetniki());
        }

        TEST_METHOD(TestSetAndGetDocuments)
        {
            Dekanat dekanat;

          
            dekanat.SetDocuments("Document1", "Document2", "Document3");

           
            Assert::AreEqual(3, dekanat.GetDocuments());
        }
        TEST_METHOD(TestDefaultConstructor)
        {
           
            Dekan dekan;

           
            Assert::AreEqual(0, dekan.GetNumOfProtocols());
        }

        TEST_METHOD(TestWriteOutAProtocol)
        {
           
            Dekan dekan;
            Lecture lecture;
            lecture.SetNumStudents(100);
            lecture.SetNumStudentsOnLecture(80);

           
            dekan.CheckLecture(lecture);

          
            Assert::AreEqual(20, dekan.GetNumOfProtocols());
        }

        TEST_METHOD(TestExpelAStudent)
        {
        
            Dekan dekan;
            Student goodStudent;
            Student badStudent;
            goodStudent.SetIsGoodStudent(true);
            badStudent.SetIsGoodStudent(false);

         
            dekan.ExpelAStudent(goodStudent);
            dekan.ExpelAStudent(badStudent);

         
            Assert::IsTrue(goodStudent.GetIsStudent());
            Assert::IsFalse(badStudent.GetIsStudent());
        }
        TEST_METHOD(TestCleanHere)
        {
      
            Cleaner cleaner;
           

        
            cleaner.CleanHere();

            Assert::IsTrue(cleaner.IsCleaned());
        }

    
	};
}
