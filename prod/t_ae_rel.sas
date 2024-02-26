/******************************************************************************
*  This script mocks the scenario for generating a final t_ae_rel PDF report
*
* For simplicity, we will simply print the input data onto a PDF file 
*****************************************************************************/
%include "/mnt/code/domino.sas";

options dlcreatedir;
libname inputs "/workflow/inputs";
libname outputs "/workflow/outputs";

%let pdf_filename = report.pdf;
ods pdf file=outputs.&pdf_filename;

proc print data=inputs.adae(obs=5);
  title 'Final t_ae_rel report';
run;

ods pdf close;

libname success "/workflow/outputs/_SUCCESS";
