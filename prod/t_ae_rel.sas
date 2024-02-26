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

/* This line isn't working right now, using sample data in the meantime

/* proc print data=inputs.adae; */
/* run; */

data dataset;
    input Student_ID $ Gender $ Age Height Weight;
    datalines;
001 M 20 170 65
002 F 21 165 55
003 M 22 180 70
004 F 20 160 50
005 M 23 175 68
;
run;

proc print data=dataset;
run;

ods pdf close;

libname success "/workflow/outputs/_SUCCESS";
