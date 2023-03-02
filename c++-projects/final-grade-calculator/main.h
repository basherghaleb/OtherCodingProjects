#pragma once
#include <map>
#include <string>
#include <set>


int GetPointTotalForStudent(std::map<std::string, std::string> studentInfo, std::string assignementCategory);
int GetTopNHomeworkTotalForStudent(std::map<std::string, std::string> studentInfo, int topNHomework);
int GetNumberOfMissingLabsForStudent(std::map<std::string, std::string> studentInfo);
int GetPointTotalForStudent(std::map<std::string, std::string> studentInfo);
std::map<std::string, std::map<std::string, std::string>> GetIDToInfoFromCSV(std::string filename);
std::map<std::string, double> GetIDToGrade(std::map<std::string, std::map<std::string, std::string>> idToStudentInfoMap);
std::set<std::string> GetStudentsEligibleForHonorsCredit(std::map<std::string, std::map<std::string, std::string>> idToStudentInfoMap, int thresh);
