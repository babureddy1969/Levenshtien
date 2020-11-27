# Levenshtien
Levenshtein Algorithm to detect closely related strings

Software Required 
1. Python 3.x
2. pip install python-levenshtein

-- Run by typing the following command at the windows command prompt
python test.py

There are about 277K strings. I am comparing strings with almost same size. e.g. if a string to be compared is 5 chars length, it will be compared with all the strings with 4, 5 and 6 length strings to get a distance of 1. Multi threading is done to process the strings faster.

Following are the timings for each string length in a 10 thread processing on a 8 GB windows 10 machine

1. 16 2030 03.442968
2. 15 2481 04.927917
3. 14 17445 53.952722
4. 13 61082 35.051812
5. 12 60562 10.093825
6. 11 19299 04:16.237551
7. 10 14586 02:15.018157
8. 9 20130 04:27.504321
9. 8 26818 07:36.326677
10. 7 24803 06:30.689928
11. 6 15771 02:24.223509
12. 5 9694 52.274948
13. 4 1756 01.687475
14. 3 542 0.136329
15. 2 90 0.006121
