%include "/mnt/code/domino.sas";

* data sdtm; 
*   set "/workflow/inputs/data_path"; 
* run;

data sdtm; 
  set "/mnt/code/data/vs.sas7bdat"; 
run;

proc export data=sdtm 
    outfile="/workflow/outputs/adae_data"
    dbms=csv replace;
run;

