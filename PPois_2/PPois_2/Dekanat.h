#pragma once
#include<iostream>
#include<vector>
#include<string>


using namespace std;

class Dekanat {



public:
	void SetDolzhniki(int num);
	void SetPlatniki(int num);
	void SetDolg(int num);
	void SetCostOfEducation(int num);
	void SetNumOfDocuments(int num);
	void SetDocuments(string doc1, string doc2, string doc3);
	void SetAdministration(int num);
	void SetBudgetniki(int num);
	
	int GetAdministration();
	int GetNumOfDocuments();
	int GetDolzhniki();
	int GetPlatniki();
	int GetBudgetniki();
	int GetDolg();
	int GetCost_of_education();
	int GetDocuments();




private:

	int administration=0;
	vector<string> documents;
	int NumOfDocuments=0;
	int dolzhniki;
	int platniki;
	int budgetniki;
	int dolg;
	int cost_of_education;


};