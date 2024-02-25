%include "/mnt/code/domino.sas";

options dlcreatedir;
libname sdtm "/mnt/code/data";
libname adae "/workflow/outputs/adae_data";

* data sdtm; 
*   set "/workflow/inputs/data_path"; 
* run;

* data sdtm; 
*   set "/mnt/code/data/vs.sas7bdat"; 
* run;

data adae.adae;
    set sdtm.vs;
run;

libname success "/workflow/outputs/_SUCCESS";
