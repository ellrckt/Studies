#pragma once

#include<iostream>
#include<string>
#include"Human.h"

using namespace std;


class Worker: public Human
{
public:
	Worker();

	Worker(string JobTitle, int Salary);

	void SetJobTitle(string JobTitle);

	string GetJobTitle();

	void SetSalary(int Salary);

	int GetSalary();

	string DoWork(string doingsmth);


private:


	string JobTitle;
	int Salary;
	


};