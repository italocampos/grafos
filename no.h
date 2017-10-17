#ifndef NO_H_
#define NO_H_

class No{
public:
	int dado;
	No *prev, *next;
	
	No(int item) {
		dado = item;
		next = NULL;
		prev = NULL;
	}
	virtual ~No() {	};
};

#endif
