#include "Dekanat.h"

void Dekanat::SetDolzhniki(int num)
{
	this->dolzhniki = num;
}

void Dekanat::SetPlatniki(int num)
{
	this->platniki=num;
}

void Dekanat::SetDolg(int num)
{
	this->dolg=num;
}

void Dekanat::SetCostOfEducation(int num)
{
	this->cost_of_education=num;
}

void Dekanat::SetNumOfDocuments(int num)
{
	this->NumOfDocuments=num;
}

void Dekanat::SetDocuments(string doc1, string doc2, string doc3)
{

	this->documents.push_back(doc1);
	this->documents.push_back(doc2);
	this->documents.push_back(doc3);

}

void Dekanat::SetAdministration(int num)
{
	this->administration = num;
}

void Dekanat::SetBudgetniki(int num)
{
	this->budgetniki = num;
}

int Dekanat::GetAdministration()
{
	return this->administration;
}



int Dekanat::GetNumOfDocuments()
{
	return this->NumOfDocuments;
}

int Dekanat::GetDolzhniki()
{
	return this->dolzhniki;
}

int Dekanat::GetPlatniki()
{
	return this->platniki;
}

int Dekanat::GetBudgetniki()
{
	return this->budgetniki;
}

int Dekanat::GetDolg()
{
	return this->dolg;
}

int Dekanat::GetCost_of_education()
{
	return this->cost_of_education;
}

int Dekanat::GetDocuments()
{
	return this->documents.size();
}
