/* first give a try run without input . 
then give input in 2nd run */
#include <iostream> 
#include <math.h>  
using namespace std; 

void printIns () { 	
cout << "Enter a number , operator and a 2nd number in new lines : \n" ;
cout << "\n" ; 
cout << "_ = Divisibility check \n"; 
cout << "F = Factors of a Number \n";
cout << "d = division in decimals \n";    
cout << "% = square root \n" ; 
cout << "^ = square \n" ;
cout << "+ = addition \n" ; 
cout << "- = subtraction \n" ; 
cout << "* = multiplication \n" ; 
cout << "/ = division \n" ;  
cout << "\n" ; 
cout << "Your Operation : " << endl; 
cout << "\n" ; 
} 

int main() {
	
printIns (); 
	 		 
int num1 , num2 = 1;      
char op;  
cin >> num1 >> op >> num2;  
int num3 = num1 % num2;  
auto num4 = sqrt (num1); 
int num5 = num1 % 2; 
int num6 = num2 % 2; 

switch (num5) { 
	
  case 1 : 
  cout << num1 << " is odd" << endl; 
  break; 
  
  case 0 : 
  cout << num1 << " is even" << endl; 
  break; 
} 

switch (num6) { 
	
	case 0 : 
	cout << num2 << " is even" << endl; 
	break; 
	
	case 1 : 
	cout << num2 << " is odd" << endl;
	break;  
} 

cout << "\n"; 

switch (op) { 
	
	case 'd' : 
	cout << num1 << " / " << num2 << " in decimals = " << float(num1) / float(num2) << endl; 
	break;
	
	case '_' : 
	if (num1 % num2 == 0) { 
		cout << num1 << " is divisible by " << num2 << endl;  
		} 
	else { 
		cout << num1 << " is not divisible by " << num2 << endl;
		} 
	break; 
	
	case 'F' : 
	cout << "Factors of " << num1 << " are" << endl; 
	for (int i = 1 ; i <= num1 ; i++) { 
		if (num1 % i == 0) { 
			cout << i << " "; 
			} 
		} 
	break;  
	
	case '%' : 
	cout << "square root " << num1 << " = " << num4 << endl; 
	break; 
	
	case '^' :  
	cout << "Square " << num1 << " = " << (num1 * num1) << endl;
	break;  
	
	case '+' : 
  cout << num1 << " + " << num2 << " = " << (num1 + num2) << endl; 
  break; 

  case '-' : 
  cout << num1 << " - " << num2 << " = " << (num1 - num2) << endl; 
  break; 

  case '*' : 
  cout << num1 << " * " << num2 << " = " << (num1 * num2) << endl; 
  break; 

  case '/' : 
  cout << num1 << " / " << num2 << " = " << (num1 / num2) << endl; 
    if (num3 == 0) { 
    cout << "No Remainder" << endl; 
    } 
   else { 
  	cout << "Remainder " << num3 << endl; 
  	 }
  break;
  
  default : 
  cout << "please give correct input" << endl; 
  break; 
   
 }
cout << "\n"; 
cout << "\n"; 
cout << "v2.4 \n"; 

 return 0; 
} 
