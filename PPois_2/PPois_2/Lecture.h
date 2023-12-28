#pragma once

#include<iostream>
#include<string>


using namespace std;

class Lecture
{
public:

	Lecture();

	void SetIsThereTeacher(bool IsThereTeacher);

	bool GetIsThereTeacher();

	void SetNumStudents(int NumStudents);

	int GetNumStudents();

	
	void SetNumStudentsOnLecture(int NumStudentsOnLecture);


	int GetNumStudentsOnLecture();

	


private:
	
	int NumStudents=90;
	int NumStudentsOnLecture;
	bool IsThereTeacher;

	

};
