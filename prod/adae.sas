%include "/mnt/code/domino.sas";
libname data "/mnt/code/data";

* data sdtm; 
*   set "/workflow/inputs/data_path"; 
* run;

* data sdtm; 
*   set "/mnt/code/data/vs.sas7bdat"; 
* run;

data sdtm;
    set data.vs;
run;

proc export data=sdtm 
    outfile="/workflow/outputs/adae_data"
    dbms=csv replace;
run;

