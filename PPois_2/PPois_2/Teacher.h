#pragma once

#include<iostream>
#include<string>
#include"Human.h"
#include"Shedule.h"
#include"Worker.h"
#include"Student.h"
#include<vector>


class Teacher : public Human, Worker
{

public:
	void SetNumOfGroups(int NumOfGroups);

	int GetNumOfGroups();

	void SetIsLector(bool IsLector);

	bool GetIsLector();

	void SetIsPzshnik(bool IsPzshnik);

	bool GetIsPzshnik();

	void SetGrades(Student& student,int grade);

	void EditGrades(Student& student, int IndexOfGrade, int grade);


private:


	int NumOfGroups;
	bool IsLector;
	bool IsPzshnik;



};