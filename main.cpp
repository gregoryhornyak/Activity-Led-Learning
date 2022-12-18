// main.cpp
// Rewritten by Leo Head
// The main class of the game

// Include defaults
#include <iostream>
#include <windows.h>
#include "generators/worldGen.h"

// main function
int main()
{
    /*
    system("mode con COLS=700");
    ShowWindow(GetConsoleWindow(),SW_MAXIMIZE);
    SendMessage(GetConsoleWindow(),WM_SYSKEYDOWN,VK_RETURN,0x20000000);
    */
    //help();
    // Generate world/island
    Island island(0,"",300,700,25,20,2);
    island.help();
    island.Printer(18,10); /// if no UI or Printing component exists
    //a1.details_Island();
};
