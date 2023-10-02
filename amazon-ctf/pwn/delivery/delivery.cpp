#include <iostream>
#include <fstream>

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

using namespace std;

int main(){

	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);

	char buffer[32];

	cout << "[*]Welcome to your favorite delivery service" << endl;
	cout << "[*]Please drop your package to the closest location" << endl;
	cout << "[*]Address:" << &buffer << endl;
	cout << "[*]Package:";

	if(read(0,buffer,64) < 5){
		cout << "[*]We don't take this...Goodbye" << endl;
		return -1;
	}
	return 0;

}
