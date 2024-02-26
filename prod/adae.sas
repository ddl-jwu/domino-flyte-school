%include "/mnt/code/domino.sas";

options dlcreatedir;
libname inputs "/workflow/inputs";
libname outputs "/workflow/outputs";

/* data input_string;  */
/*     infile "/workflow/inputs/sdtm_data_dir"; */
/*     input;  */
/* run; */
/*  */
/* proc print data=input_string; */
/* run; */

proc print data=inputs.vs(obs=5);
run;

data outputs.adae;
    set inputs.vs;
run;

libname success "/workflow/outputs/_SUCCESS";
