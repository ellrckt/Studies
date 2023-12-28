#pragma once
#include<iostream>
#include<vector>
#include<string>
#include"Human.h"



using namespace std;

class Cleaner :public Human
{


public:
	bool IsCleaned();
	void CleanHere();

private:
	vector<string> instruments = { "rag","mop" };
	bool cleaned = false;



};

