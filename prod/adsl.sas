/******************************************************************************
*  We are going to pretend that this script:
*  1. Loads in the original SDTM data
*  2. Transforms that data to create the ADSL dataset
* 
*  For simplcity, we are going to mock the scenario by simply 
*  returning the same dataset as the output.
*****************************************************************************/
%include "/mnt/code/domino.sas";

options dlcreatedir;
libname inputs "/workflow/inputs"; /* All inputs live in this directory */ 
libname outputs "/workflow/outputs"; /* All outputs must go to this directory */ 

data outputs.adae;
    set inputs.ts;
run;

/* (Required) This line signals to Domino Flows that outputs were successfully created */
libname success "/workflow/outputs/_SUCCESS";
