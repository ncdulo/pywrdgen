# password strength determination

The password strength is determined following a simple structure of rules.
Rules were originally found through a StackOverflow answer, which points to
a website providing password strength checking. The algorithm used in pywrdgen
is based on the rules described on 'The Password Meter'.

# rules
- Flat: Rates that add/remove in non-changing increments.
- Incr: Rates that add/remove in adjusting increments.
- Cond: Rates that add/remove depending on additional factors.
- Comp: Rates that are too complex to summarize. See source code for details.
- n: Refers to the total number of occurrences.
- len: Refers to the total password length.
- Additional bonus scores are given for increased character variety.
- Final score is a cumulative result of all bonuses minus deductions.
- Final score is capped with a minimum of 0 and a maximum of 100.
- Score and Complexity ratings are not conditional on meeting minimum requirements.
```
Additions (better passwords)
-----------------------------
- Number of Characters              Flat       +(n*4)   
- Uppercase Letters                 Cond/Incr  +((len-n)*2)     
- Lowercase Letters                 Cond/Incr  +((len-n)*2)     
- Numbers                           Cond       +(n*4)   
- Symbols                           Flat       +(n*6)
- Middle Numbers or Symbols         Flat       +(n*2)   
- Shannon Entropy                   Complex    *EntropyScore

Deductions (worse passwords)
----------------------------- 
- Letters Only                      Flat       -n   
- Numbers Only                      Flat       -(n*16)  
- Repeat Chars (Case Insensitive)   Complex    -    
- Consecutive Uppercase Letters     Flat       -(n*2)   
- Consecutive Lowercase Letters     Flat       -(n*2)   
- Consecutive Numbers               Flat       -(n*2)   
- Sequential Letters (3+)           Flat       -(n*3)   
- Sequential Numbers (3+)           Flat       -(n*3)   
- Sequential Symbols (3+)           Flat       -(n*3)
- Repeated words                    Complex    -       
- Only 1st char is uppercase        Flat       -n
- Last (non symbol) char is number  Flat       -n
- Only last char is symbol          Flat       -n
```

# references
- https://stackoverflow.com/questions/75057/what-is-the-best-way-to-check-the-strength-of-a-password
- https://stackoverflow.com/questions/15450192/fastest-way-to-compute-entropy-in-python
- http://www.passwordmeter.com/
