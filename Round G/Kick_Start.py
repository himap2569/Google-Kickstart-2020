"""PROBLEM:
Ksenia is very fond of reading so she kicks off each day by reading a fragment from her favourite book before starting with the rest of her morning routine. 
A fragment is simply a substring of the text. Ksenia is somewhat superstitious and believes that her day will be lucky if the fragment she reads starts with the 
string KICK, then goes on with 0 or more characters, and eventually ends with the string START, even if the overall fragment makes little sense.

Given the text of the book, count the number of different lucky fragments that Ksenia can read before the book gets old and she needs to buy another one. Two 
fragments are considered to be different if they start or end at different positions in the text, even if the fragments read the same. Also note that different
lucky fragments may overlap.

Input
The first line of the input gives the number of test cases T. T lines follow, each containing a single string S consisting of upper case English letters only.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of different lucky fragments in 
the text of this test case.

Limits
Memory limit: 1 GB.
1 ≤ T ≤ 100.
S consists of upper-case English letters only.

Test Set 1
Time limit: 20 seconds.
1 ≤ |S| ≤ 1000.

Test Set 2
Time limit: 40 seconds.
1 ≤ |S| ≤ 105.

Sample

Input
 	
Output
 
3
AKICKSTARTPROBLEMNAMEDKICKSTART
STARTUNLUCKYKICK
KICKXKICKXSTARTXKICKXSTART

  
Case #1: 3
Case #2: 0
Case #3: 5

  
There are three lucky fragments in the first test case, namely, KICKSTARTPROBLEMNAMEDKICKSTART and two occurrences of KICKSTART. The text in the second test case has 
no lucky fragments at all.

SOLUTION:"""
def cnt(s,n):
    c1=0
    c2=0
    for i in range(n):
        if(s[i:i+4]=="KICK"):
            c1+=1
        if(s[i:i+5]=="START"):
            c2=c2+c1
    return c2
t=int(input())
for p in range(t):
    s=input()
    n=len(s)
    print("Case #{}: {}".format(p+1,cnt(s,n)))
