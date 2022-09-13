/* 
First give a try run without input then give input in second run
*/ 
#include <iostream>
#include <math.h>
using namespace std;

class calc { 
	public : 
	
 calc () { 
		cout << "Enter a number , operator and a 2nd number in new lines : \n" ;
    cout << "\n" ; 
    cout << "# = exponent \n"; 
    cout << "_ = Divisibility check \n"; 
    cout << "F = Factors of a Number \n";
    cout << "d = division in decimals \n";    
    cout << "% = square root \n" ; 
    cout << "+ = addition \n" ; 
    cout << "- = subtraction \n" ; 
    cout << "* = multiplication \n" ; 
    cout << "/ = division \n" ;  
    cout << "\n" ; 
    cout << "Your Operation : " << endl; 
    cout << "\n" ;
    }
    
    ~calc () { 
    	cout << "\n"; 
    	cout << "\n";
    	cout << "v2.6" << endl;
    	}
    	
  void expo (int x2 , int x3) { 
  	cout << x2 << " to the power of " << x3 << " = " << pow(x2 , x3) << endl; 
  	}
    
  void add (int x , int y) { 
  	cout << x << " + " << y << " = " << x + y << endl; 
  	} 
  	
  void sub (int p , int q) { 
  	cout << p << " - " << q << " = " << p - q << endl; 
  	} 
  	
  void mult (int t , int u) { 
  	cout << t << " * " << u << " = " << t * u << endl; 
  	} 
  	
  void div (int m , int n) { 
  	cout << m << " / " << n << " = " << m / n << endl; 
  	cout << "Remainder = " << m % n << endl; 
  	}
  	
  void sq2 (int _q) { 
  	cout << "Square Root " << _q << " = " << sqrt(_q) << endl; 
  	} 
  	
  void divd (int _m , int _n) { 
  	cout << _m << " / " << _n << " in decimals = " << (float) _m / (float) _n << endl; 
  	}
  	
  void fact (int w) { 
  	cout << "Factors of " << w << " are" << endl; 
  	for (int i = 1 ; i <= w ; i++) { 
  		if (w % i == 0) { 
  			cout << i << " "; 
  			} 
  		} 
  	}
  	
  void divs (int po , int sq) { 
  	if (po % sq == 0) { 
  		cout << sq << " is divisible by " << po << endl; 
  		} 
  		else { 
  			cout << sq << " is not divisible by " << po << endl; 
  			} 
  		}  
  	};

int main()
{
	int num1 , num2 = 1;
	char op; 
	cin >> num1 >> op >> num2; 
	calc obj; 
	
	if (num1 % 2 == 0) { 
		cout << num1 << " is even" << endl; 
		} 
		else { 
			cout << num1 << " is odd" << endl; 
			} 
			
	if (num2 % 2 == 0) { 
		cout << num2 << " is even" << endl; 
		} 
		else { 
			cout << num2 << " is odd" << endl; 
			} 
			
			cout << "\n"; 
			cout << max(num1 , num2) << " > " << min(num1 , num1) << endl;
			cout << "\n"; 
			
		switch (op) { 
			case '+' : 
			obj.add(num1 , num2); 
			break; 
			
			case '-' : 
			obj.sub(num1 , num2); 
			break; 
			
			case '/' : 
			obj.div(num1 , num2); 
			break;
			
			case '*' : 
			obj.mult(num1 , num2); 
			break; 
			
			case '%' : 
			obj.sq2(num1); 
			break; 
			
			case 'd' : 
			obj.divd(num1 , num2); 
			break; 
			
			case 'F' : 
			obj.fact(num1); 
			break; 
			
			case '_' : 
			obj.divs(num1 , num2); 
			break;
			
			case '#' : 
			obj.expo(num1 , num2); 
			break;  
	}
	return 0;
}
