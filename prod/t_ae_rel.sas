/******************************************************************************
*  This script mocks the scenario for generating a final t_ae_rel PDF report
*
* For simplicity, we will simply print the input data onto a PDF file 
*****************************************************************************/
%include "/mnt/code/domino.sas";

options dlcreatedir;
libname inputs "/workflow/inputs";
libname outputs "/workflow/outputs";

ods pdf file=outputs.report;

proc print data=inputs.adae(obs=5);
run;

ods pdf close;

libname success "/workflow/outputs/_SUCCESS";
