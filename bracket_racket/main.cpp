
/*

solution to:
http://www.reddit.com/r/dailyprogrammer/comments/11par4/10182012_challenge_104_intermediate_bracket_racket/

 */

#include <stack>
#include <map>
#include <cstdlib>
#include <iostream>
#include <sstream>

using namespace std;

// predicate indicating that character is an open bracket
inline bool popen_bracket( char c )
{
  return c == '(' || c == '[' || c == '{' || c == '<';
}

// predicate indicating that character is a close bracket
inline bool pclose_bracket( char c )
{
  return c == ')' || c == ']' || c == '}' || c == '>';
}


bool brack(string& input)
{
  // stack to store brackets
  stack<char> sc;

  // map to store correspondence between open and close brackets
  map<char,char> mc;

  // initialize map with pairs of open and close brackets
  mc['('] = ')';
  mc['{'] = '}';
  mc['['] = ']';
  mc['<'] = '>';

  cout << "string: " << input << endl;

  for(int i = 0; i < input.length(); i++ ) {
    char current = input[i];

    // push incoming bracket types onto the stack
    if( popen_bracket(current) ) {
      sc.push(current);
      continue;  // go to the next character in 'input'
    }

    // process closing brackets
    if( pclose_bracket(current) ) {
      if( sc.empty() ) {  // an empty stack is an error
	cout << "Error: bracket " << input[i] << " is missing a match" << endl << endl;
	return false;
      }
      
      // check to see if the bracket has match
      char top = sc.top();
      sc.pop();  // remove the element
      if( mc[top] != current ) {
	cout << "Error: bracket mismatch \"" << top << "\" and \"" << current << "\"" << endl << endl;
	return false;
      }
    }
  }

  if( !sc.empty() ) {
    cout << "Error: bracket \"" << sc.top() << "\" is missing a match" << endl << endl;
    return false;
  }
  else {
    cout << "All brackets match" << endl << endl;
  }

  return true;
}

int main(void) {
  string input = "";
  getline( cin, input );

  if( brack(input) )
    return EXIT_SUCCESS;
  else
    return EXIT_FAILURE;
}

