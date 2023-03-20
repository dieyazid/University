#include <iostream>
#include <list>
#include <algorithm>
#include <string>

using namespace std;

void print(list<string> uneliste)
{
cout << "{ ";
for (auto mot : uneliste) cout << mot << " ";
cout << "}" << endl;
 }

bool Incluse(list<string> L1, list<string> L2)
{
    list<string>::iterator iter;
    bool In;
    for (iter = L1.begin(); iter != L1.end(); iter++)
    {
        In = false;
        for (auto element : L2)
        {
            if (*iter == element)
            {
                In = true;
                break;
            }
        }
    }
    return In;
}

int main()
 {
 list<string> L1 = { "Logique", "Compilation", "Programmation", "Prolog" };
 list<string> L2 = { "Compilation", "Logique", "Programmation"};
 list<string> MaList={ "Logique", "Compilation", "Programmation", "System" };

cout << "\n\tL1 = "; print(L1);
cout << "\n\tL2 = "; print(L2);
cout << "\n\tMaListe = "; print(MaList);

if (Incluse(L1, MaList))
 cout << "\n\tL1 est incluse dans maListe";
 else
 cout << "\n\tL1 n'est pas incluse dans MaListe";

 cout << endl;

 if (Incluse(L2, MaList))
 cout << "\n\tL2 est incluse dans maListe";
 else
    cout << "\n\tL2 n'est pas incluse dans MaListe";
cout<<endl;

return 0;
}
