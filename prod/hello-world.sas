/****************
This program reads in a set of grades for six students, and prints out their student numbers and genders
******************/

*********;
** Setup environment including libraries for this reporting effort;
%include "/mnt/code/domino.sas";
*********;

OPTIONS NODATE LS=78;
DATA grade;
    Input subject gender $
        exam1 exam2 hwgrade $;
    DATELINES;
    10 M 80 84 A
     7 . 85 89 A
     4 F 90 .  B
    20 M 82 85 B
    25 F 94 94 A
    14 F 88 84 C
    ;
    RUN;

PROC PRINT data=grade;
    var subject gender; * print student ID and gender;
run;