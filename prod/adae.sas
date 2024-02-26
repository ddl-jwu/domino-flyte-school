%include "/mnt/code/domino.sas";

options dlcreatedir;
libname inputs "/workflow/inputs";
libname outputs "/workflow/outputs";

data outputs.adae;
    set inputs.vs;
run;

libname success "/workflow/outputs/_SUCCESS";
