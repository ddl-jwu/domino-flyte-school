%include "/mnt/code/domino.sas";

options dlcreatedir;
libname inputs "/workflow/inputs";
libname outputs "/workflow/outputs";
* libname sdtm "/mnt/code/data";
libname adae "/workflow/outputs/adae_data";

* data sdtm; 
*   set "/workflow/inputs/data_path"; 
* run;

* data sdtm; 
*   set "/mnt/code/data/vs.sas7bdat"; 
* run;

/* data input_string;  */
/*     infile "/workflow/inputs/sdtm_data_dir"; */
/*     input;  */
/* run; */
/*  */
/* proc print data=input_string; */
/* run; */

data outputs.adae;
    set inputs.vs;
run;

libname success "/workflow/outputs/_SUCCESS";
