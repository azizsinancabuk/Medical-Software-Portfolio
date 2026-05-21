// Forensic Case Management System
// Developer: Aziz Sinan Cabuk

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class ForensicCase {
public:
    int caseID;
    string victimName;
    string caseType; // e.g., Toxicology, DNA Matching, Accident
    string status;   // e.g., Under Investigation, Completed

    ForensicCase(int id, string name, string type, string stat) {
        caseID = id;
        victimName = name;
        caseType = type;
        status = stat;
    }

    void displayCase() {
        cout << "Case ID: " << caseID
            << " | Victim: " << victimName
            << " | Investigation Type: " << caseType
            << " | Status: " << status << endl;
    }
};

int main() {
    vector<ForensicCase> database;

    // Entering sample forensic cases into the system
    database.push_back(ForensicCase(101, "Anonymous X", "Toxicology Report", "Under Investigation"));
    database.push_back(ForensicCase(102, "John Doe", "DNA Profiling", "Completed"));
    database.push_back(ForensicCase(103, "Ayse Yilmaz", "Digital Forensics", "Under Investigation"));

    cout << "=== FORENSIC CASE MANAGEMENT SYSTEM ===" << endl;
    for (int i = 0; i < database.size(); i++) {
        database[i].displayCase();
    }
    cout << "=======================================" << endl;

    return 0;
}