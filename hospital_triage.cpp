// Hospital Patient Triage and Record System
// Developer: Aziz Sinan Cabuk

#include <iostream>
#include <queue>
#include <string>

using namespace std;

struct Patient {
    string name;
    int urgencyFactor; // 1: Mild, 2: Moderate, 3: Critical

    // Operator overloading to prioritize the most urgent patient in the queue
    bool operator<(const Patient& other) const {
        return urgencyFactor < other.urgencyFactor;
    }
};

int main() {
    priority_queue<Patient> hospitalQueue;

    // Patients entering the emergency room
    hospitalQueue.push({ "Mehmet Demir", 1 });  // Green Zone
    hospitalQueue.push({ "Stoyan Ivanov", 3 }); // Red Zone (Critical)
    hospitalQueue.push({ "Elena Petrova", 2 }); // Yellow Zone

    cout << "=== HOSPITAL EMERGENCY TRIAGE REORDER ===" << endl;
    cout << "(Patients to be seen by the doctor in order of priority)" << endl;
    cout << "------------------------------------------------------" << endl;

    while (!hospitalQueue.empty()) {
        Patient current = hospitalQueue.top();
        string status = (current.urgencyFactor == 3) ? "CRITICAL" : (current.urgencyFactor == 2 ? "MODERATE" : "STABLE");

        cout << "Patient Name: " << current.name << " -> Status: " << status << endl;
        hospitalQueue.pop();
    }

    return 0;
}