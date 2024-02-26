%include "/mnt/code/domino.sas";

options dlcreatedir;
libname inputs "/workflow/inputs";
libname outputs "/workflow/outputs";

%let pdf_filename = report.pdf;
ods pdf file=outputs.&pdf_filename;

proc print data=inputs.adae;
  title 'Final t_ae_rel report';
run;

ods pdf close;

libname success "/workflow/outputs/_SUCCESS";
