%include "/mnt/code/domino.sas";
data sdtm; 
  set "/workflow/inputs/data_path"; 
run;

* proc export data=sdtm 
*     outfile="/workflow/outputs/adae" 
*     dbms=sas7bdat replace;
* run;

