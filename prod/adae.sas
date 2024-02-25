%include "/mnt/code/domino.sas";

* data sdtm; 
*   set "/workflow/inputs/data_path"; 
* run;

data sdtm; 
  set "/mnt/code/data/vs.sas7bdat"; 
run;

libname output "/workflow/outputs/adae_data";
data output.adae;
  set sdtm;
run;


