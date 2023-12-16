#pragma once
#include <iostream>
#include<vector>


using namespace std;

class Set {

private:


	vector<string> elements;


public:

	Set(string str);

	Set();

	void processSet(const std::string& set_example, int& i);

	std::string extractSet(const std::string& set_example, int& i);

	void StrToSet(const std::string& set_example);

	//void StrToSet(string set_example);

	bool IsEmpty();

	string add(string str);

	string add(char str);

	string del(int pos);

	int power();
	
	bool contains(string str);
	
	bool contains(char ch);

	void Print();

	bool operator[](const string& element) const;

	Set operator+(const Set& other) const;

	Set& operator+=(const Set& other);

	Set operator*(const Set& other) const;

	Set& operator*=(const Set& other);

	Set operator-(const Set& other) const;

	Set& operator-=(const Set& other);

	vector<Set> powerSet();

};