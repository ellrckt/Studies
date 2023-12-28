#pragma once
#include<iostream>
#include<vector>
#include<string>
#include"Human.h"
#include"Worker.h"



class Security :public Human, Worker
{

public:

	void SetOutsiders(int outsiders);
	int GetNumOfOutsiders();
	

private:

	bool IsAllAlright=true;
	int NumOfOutsiders = 0;




};