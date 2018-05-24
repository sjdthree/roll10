# roll10

Readme file for roll10.py

Description:
roll10 is a python solution to the "I have 2 6-sided dice and I want to achieve a 1-10 result, but even distribution (or even chance) that I get a 1-10 with every roll."  Simple one page solution that uses a lookup table (dictionary) to ensure there is an even chance of getting a 1 as there is a 10 with every two rolls.

made for python 3.5

Modules:
matplotlib needed for testing and displaying histograms

% pip install matplotlib

python3 roll10.py

results of tests:
Run 1,000,000 rolls, show distribution of results:
 
 (Two runs to show repeatability)
 
![Roll 10 Output](https://github.com/sjdthree/roll10/blob/master/roll10ouput.png)


![Roll 10 Output](https://github.com/sjdthree/roll10/blob/master/roll10ouputb.png)


Even distribution of results from 1-10 for 1M rolls.
