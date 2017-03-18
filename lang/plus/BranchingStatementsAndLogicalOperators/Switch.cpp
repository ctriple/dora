// Switch.cpp -- using the switch statement

#include <iostream>

using namespace std;

void ShowMenu(); // function prototypes
void Report();
void Comfort();

int main(void)
{
    ShowMenu();
    int Choice;
    cin >> Choice;
    while (Choice != 5) {
        switch (Choice) {
            case 1: cout << "\a\n"; break;
            case 2: Report(); break;
            case 3: cout << "The boss was in all day.\n"; break;
            case 4: Comfort(); break;
            default: cout << "That's not a choice.\n";
        }
        ShowMenu();
        cin >> Choice;
    }
    cout << "Bye!\n";

    return 0;
}

void ShowMenu()
{
    cout << "Please enter 1, 2, 3, 4, or 5:\n"
            "1) alarm        2) report\n"
            "3) alibi        4) comfort\n"
            "5) quit\n";
}

void Report()
{
    cout << "It's been an excellent week for business.\n"
            "Sales are up 120%. Expenses are down 35%.\n";
}

void Comfort()
{
    cout << "Your employees think you are the finest CEO\n"
            "in the industry. The board of directors think\n"
            "you are the finest CEO in the industry.\n";
}