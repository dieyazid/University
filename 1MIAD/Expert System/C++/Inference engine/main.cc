#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

struct Rule {
    string name;
    bool active;
    vector<string> premisses;
    vector<string> conclusions;
};

int main() {
    vector<Rule> rules;
    ifstream reglestxt("regles.txt");

    if (!reglestxt.is_open()) {
        cout << "There was an error while opening the file" << endl;
        return 1;
    }

    string line;
    int i =0 ;
    while (getline(reglestxt, line)) {
        Rule rule;
        size_t rule_mid = line.find(">");
        size_t rule_end = line.find(".");

        if (rule_mid == string::npos) {
            cout << "Erreur : Structure de la règle incorrecte." << endl;
            continue;
        }

        i+=1;
        rule.name = "R"+to_string(i);
        rule.active = true;

        string premissesStr = line.substr(0, (rule_mid-1));
        string conclusionsStr = line.substr(rule_mid+2,(rule_end-rule_mid)-2);

        size_t start = 0, end = 0;
        for (int i = 0; i < premissesStr.length(); i++) {
            if (premissesStr[i] == ' ') {
                rule.premisses.push_back(premissesStr.substr(start, i - start));
                start = i + 1;
            }
        }
        rule.premisses.push_back(premissesStr.substr(start));

        start = 0, end = 0;
        for (int i = 0; i < conclusionsStr.length(); i++) {
            if (conclusionsStr[i] == ' ') {
                rule.conclusions.push_back(conclusionsStr.substr(start, i - start));
                start = i + 1;
            }
        }
        rule.conclusions.push_back(conclusionsStr.substr(start));

        rules.push_back(rule);
    }
    reglestxt.close();

    cout << "Base des règles : " << endl;
    for (int i = 0; i < rules.size(); i++) {
        cout << rules[i].name << ": ";
        for (int j = 0; j < rules[i].premisses.size(); j++) {
            cout << rules[i].premisses[j] << " ";
        }
        cout << "-> ";
        for (int j = 0; j < rules[i].conclusions.size(); j++) {
            cout << rules[i].conclusions[j] << " ";
        }
        cout << "| Active : " << (rules[i].active ? "True" : "False") << endl;
    }
}
