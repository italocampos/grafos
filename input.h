#include <iostream>
#include <stdlib.h>
#include "tabela.h"
#include "lista.h"

using namespace std;

void readFromUser(Tabela &tabela) {
	Tabela *t = &tabela;
	cout<<"LISTA DE ADJACENCIA ==============\n";
	cout<<"Digite -1 para encerrar a leitura.\n\n";
	t->newLine();
	int valor = 0;
	while(valor != -1) {
		int i = 0;
		cout<<"Linha #"<<i<<":";
		cin>>valor;
		t->pushItem(i, valor);
		i++;
	}
}
