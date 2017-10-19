#ifndef LISTA_H_
#define LISTA_H_

#include "no.h"
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

class Lista {
private:
	No *first = NULL, *last = NULL;
	
	void startList(int item) {
		first = new No(item);
		first->next = NULL;
		first->prev = NULL;
		last = first;
	}
	
	void killList() {
		delete first;
		first = NULL;
		last = first;
	}
	
public:
	Lista(){	}
	
	virtual ~Lista() { }
	
	void printNodes() {
		cout<<"\n";
		No *node = first;
		while(node != NULL) {
			cout<<"[ ";
			if(node->prev == NULL)
				cout<<"NULL <- ";
			else
				printf("%d <- ", node->prev);
			cout<<node->dado;
			if(node->next == NULL)
				cout<<" -> NULL";
			else
				printf(" -> %d", node->next);
			printf(" ] Endereco: %d\n", node);
			node = node->next;
		}
	}
	
	bool isEmpty() {
		if(first == NULL)
			return true;
		else
			return false;
	}
	
	No * getFirstNode() {
		return this->first;
	}
	
	No * getLastNode() {
		return this->last;
	}
	
	int length() {
		No *p = first;
		int tam = 0;
		while(p != NULL) {
			p = p->next;
			tam++;
		}
		return tam;
	}
	
	// Retorna a posição da primeira ocorrência de um determinado item. Retorna -1 caso ele não exista
	int positionItem(int item) {
		int pos, tam = length();
		No *p = first;
		for(pos=0; pos<tam; pos++) {
			if(item == p->dado)
				break;
			p = p->next;
		}
		if(pos != tam)
			return pos;
		else
			return -1;
	}
	
	// Ajusta um item na posicao i
	void setItem(int item, int posicao) {
		if(posicao >= 0 && posicao < length()) {
			No *p = first;
			for(int i=0; i<posicao; i++)
				p = p->next;
			p->dado = item;
		}
		else
			cout<<"Out of range.\n";
	}
	
	// Retorna um item i da lista. Retorna -1 caso seja uma posição inválida
	int getItem(int posicao) {
		if(posicao >= 0 && posicao < length()) {
			No *p = first;
			for(int i=0; i<posicao; i++)
				p = p->next;
			return p->dado;
		}
		else
			return -1;
	}
	
	void addBegin(int item) {
		if(isEmpty())
			startList(item);
		else {
			No *p = new No(item);
			p->next = first;
			first->prev = p;
			first = p;
			p->prev = NULL;
		}
	}
	
	void addEnd(int item) {
		if(isEmpty())
			startList(item);
		else {
			No *p = new No(item);
			p->prev = last;
			last->next = p;
			last = p;
			p->next = NULL;
		}
	}
	
	void addPosition(int posicao, int item) {
		No *p, *p1, *p2;
		if(isEmpty() && posicao == 0) {
			startList(item);
		}
		else {
			if(posicao == 0)
					addBegin(item);
			else {
				if(posicao > 0 && posicao < length()) {
					p = first;
					for(int i=0; i!=posicao; i++)
						p = p->next;
					p1 = p->prev;
					p2 = new No(item);
					p2->next = p;
					p2->prev = p1;
					p1->next = p2;
					p->prev = p2;
				}
				else
					cout<<"Out of range.\n";
			}
		}
	}
	
	void removeFirst() {
		if(first != NULL) {
			if(length() == 1)
				killList();
			else {
				No *p = first->next;
				delete first;
				first = p;
				first->prev = NULL;
			}
		}
		else
			cout<<"Empty list.\n";
	}
	
	void removeLast() {
		if(first != NULL) {
			if(length() == 1)
				killList();
			else {
				No *p = last->prev;
				delete last;
				last = p;
				last->next = NULL;
			}
		}
		else
			cout<<"Empty list.\n";
	}
	
	// Remove todas as ocorrências de um item
	void removeAllItems(int item) {
		No *p = first, *ant, *prox;
		while(p != NULL) {
			if(p->dado == item) {
				ant = p->prev;
				prox = p->next;
				delete p;
				if(ant != NULL)
					ant->next = prox;
				if(prox != NULL)
					prox->prev = ant;
				if(ant == NULL) {
					if(prox == NULL) {
						first = NULL;
						last = NULL;
						break;
					}
					else
						first = prox;
				}
			}
			p = p->next;
		}
	}
	
	void removePosition(int posicao) {
		No *p, *ant, *prox;
		int tam = length();
		if(posicao >=0 && posicao < tam && !isEmpty()) {
			if(posicao == 0)
				removeFirst();
			else
				if(posicao == tam-1)
					removeLast();
				else {
					p = first;
					for(int i=0; i!=posicao; i++)
						p = p->next;
					ant = p->prev;
					prox = p->next;
					ant->next = prox;
					prox->prev = ant;
					delete p;
				}
		}
		else
			cout<<"Coul not remove this item.\n";
	}

	void append(Lista lista) {
		this->last->next = lista.getFirstNode();
		lista.getFirstNode()->prev = this->getLastNode();
		this->last = lista.getLastNode();
	}
	
	void reverse() {
		No *p = first, *aux;
		int tam = length();
		for(int i=0; i<tam; i++) {
			aux = p->next;
			p->next = p->prev;
			p->prev = aux;
			p = aux;
		}
		aux = first;
		first = last;
		last = aux;
	}
	
	void print() {
		cout<<"[";
		if(!isEmpty()) {
			No *p = first;
			while(p != NULL) {
				cout<<p->dado<<",";
				p = p->next;
			}
			printf("%c", 8);
		}
		cout<<"]";
	}
};

#endif
