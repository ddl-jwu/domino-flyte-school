/******************************************************************************
*  This script mocks the scenario for generating a final t_ae_rel PDF report
*
* For simplicity, we will simply print the input data onto a PDF file 
*****************************************************************************/
%include "/mnt/code/domino.sas";
options dlcreatedir;
libname inputs "/workflow/inputs"; /* All inputs live in this directory */ 
libname outputs "/workflow/outputs"; /* All outputs must go to this directory */ 
libname report "/workflow/outputs/report";

ods pdf file=report;
title "T_AE_REL Report";

/* proc report data=inputs.adae;  */
/*     title "T_AE_REL Report" tsparmcs=100; */
/* run;  */
/*  */
ods pdf close;

/* (Required) This line signals to Domino Flows that outputs were successfully created */
libname success "/workflow/outputs/_SUCCESS";

