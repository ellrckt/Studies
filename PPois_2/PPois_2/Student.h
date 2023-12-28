#pragma once

#include<iostream>
#include<string>
#include"Human.h"
#include"Shedule.h"
#include<vector>

using namespace std;

class Student :public Human,Shedule
{

public:

	Student();

	Student(string FavSubject, string University, bool IsStudent, bool IsGoodStudent,int Course);

	void Learning(string Subject);
	void ChooseFavSub(string Subject);
	string GetFavSubject();
	string GetUniversity();
	bool GetIsStudent();
	void SetIsStudent(bool IsStudent);
	void SetIsGoodStudent(bool IsGoodStudent);
	bool GetIsGoodStudent();
	void SetCourse(int course);
	int GetCourse();
	bool PassExam(Student& student);
	vector<int>grades;
private:

	
	string FavSubject;
	string University = "BSUIR";
	bool IsStudent=true;
	bool IsGoodStudent=true;
	int Course=1;


};
