%include "/mnt/code/domino.sas";

options dlcreatedir;
libname inputs "/workflow/inputs";
libname outputs "/workflow/outputs";

proc print data=inputs.advs(obs=5);
run;

libname success "/workflow/outputs/_SUCCESS";
