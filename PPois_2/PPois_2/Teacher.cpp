#include"Teacher.h"

void Teacher::SetNumOfGroups(int NumOfGroups)
{
	this->NumOfGroups = NumOfGroups;
}

int Teacher::GetNumOfGroups()
{
	return this->NumOfGroups;
}

void Teacher::SetIsLector(bool IsLector)
{
	this->IsLector = IsLector;
}

bool Teacher::GetIsLector()
{
	return this->IsLector;
}

void Teacher::SetIsPzshnik(bool IsPzshnik)
{
	this->IsPzshnik = IsPzshnik;
}

bool Teacher::GetIsPzshnik()
{
	return this->IsPzshnik;
}

void Teacher::SetGrades(Student& student,int grade)
{
	student.grades.push_back(grade);
}

void Teacher::EditGrades(Student& student, int IndexOfGrade,int grade)
{
	student.grades[IndexOfGrade] = grade;
}



