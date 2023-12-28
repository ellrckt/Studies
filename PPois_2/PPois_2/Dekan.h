#pragma once

#include<iostream>
#include<string>
#include"Human.h"
#include"Worker.h"
#include"Lecture.h"
#include"Student.h"

using namespace std;

class Dekan: public Human,Worker
{
public:

	
	Dekan();
	void CheckLecture(Lecture& lecture);
	void WriteOutAProtocol(Lecture& lecture);
	int WriteNumOFProtocols(int protocols);
	void ExpelAStudent(Student& student);
	int GetNumOfProtocols();

	

private:

	int NumOfProtocols;

	
	

};