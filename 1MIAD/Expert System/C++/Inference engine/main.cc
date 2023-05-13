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
struct Fact{
    string name;
};

bool Chainage_avant_profonder(vector<Rule>& rules, string goal,vector<Fact>&facts);

int main() {
    vector<Rule> rules;
    // print all txt files in the current directory and wait for user file name
    cout << "======================================"<<  endl;
    system("ls");
    cout << "======================================"<<  endl;
    string fileName;cout << "Enter the name of the file you want to open: ";
    cin >> fileName;cin.ignore();
    ifstream reglestxt(fileName);

    if (!reglestxt.is_open()) {
        cout << "There was an error while opening the file" << endl;
        return 1;
    }

    string line;
    int i = 0;
    while (getline(reglestxt, line)) {
        Rule rule;
        size_t rule_mid = line.find(">");
        size_t rule_end = line.find(".");

        if (rule_mid == string::npos) {
            cout << "Erreur : Structure de la règle incorrecte." << endl;
            continue;
        }

        i += 1;
        rule.name = "R" + to_string(i);
        rule.active = true;

        string premissesStr = line.substr(0, (rule_mid - 1));
        string conclusionsStr = line.substr(rule_mid + 2, (rule_end - rule_mid) - 2);

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

    vector<Fact> facts;
    int nbFacts;
    cout << "Combien du faits ya t'il? "<< endl;
    cin >> nbFacts;
    cin.ignore();
    Fact fact;
    for (int i = 0; i < nbFacts; i++) {
        cout << "Entrez le nom du fait : ";
        getline(cin, fact.name);
        facts.push_back(fact);
    }
    string goal;
    cout << "Entrez le but à atteindre : ";
    getline(cin, goal);

    if (Chainage_avant_profonder(rules, goal,facts)) {
        cout << "Le but a été atteint." << endl;
    } else {
        cout << "Le but n'a pas pu être atteint." << endl;
    }
}
bool Chainage_avant_profonder(vector<Rule>& rules, string goal, vector<Fact>&facts){
    bool goalReached = false;
    bool allRulesInactive = false;
    int c=0;
    
    // Tant que le but n'est pas atteint et qu'il y a des règles actives à traiter
    while (!goalReached && !allRulesInactive) {
        cout << "================= Cycle " << c+1<< endl;
        bool ruleFired = false;
        allRulesInactive = true;
        // Parcourir toutes les règles
        for (int i = 0; i < rules.size(); i++) {
            // Si la règle est active
            if (rules[i].active) {
                bool allPremissesTrue = true;
                // Parcourir toutes les prémisses de la règle
                for (int j = 0; j < rules[i].premisses.size(); j++) {
                    bool premissTrue = false;
                    // Parcourir tous les faits
                    for (int k = 0; k < facts.size(); k++) {
                        // Si la prémisses est présente dans la base de faits
                        if (rules[i].premisses[j] == facts[k].name) {
                            premissTrue = true;
                            break;
                        }
                    }
                    if (!premissTrue) {
                        allPremissesTrue = false;
                        break;
                    }
                }
                // Si toutes les prémisses sont vraies, on ajoute les conclusions à la base de faits et on désactive la règle
                if (allPremissesTrue) {
                    // PRINT LA REGLE A APPLIQUE
                    cout << "Règle appliquée : " << rules[i].name << endl;
                    ruleFired = true;
                    for (int j = 0; j < rules[i].conclusions.size(); j++) {
                        bool factExists = false;
                        for (int k = 0; k < facts.size(); k++) {
                            if (rules[i].conclusions[j] == facts[k].name) {
                                factExists = true;
                                break;
                            }
                        }
                        if (!factExists) {
                            Fact newFact;
                            newFact.name = rules[i].conclusions[j];
                            facts.push_back(newFact);
                            // print full updated fact vector
                            cout << "Base de faits : {";
                            for (int i = 0; i < facts.size(); i++) {
                                cout << facts[i].name <<",";
                            }
                            cout << "}" << endl;
                        }
                    }
                    rules[i].active = false;
                    allRulesInactive = false;
                    break;
                }
            }
        }
        if (!ruleFired) {
            allRulesInactive = true;
        }
        // Vérifier si le but a été atteint
        for (int i = 0; i < facts.size(); i++) {
            if (facts[i].name == goal) {
                goalReached = true;
                break;
            }
        }
        c++ ;
    }
    return goalReached;
}