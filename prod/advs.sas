/******************************************************************************
*  We are going to pretend that this script:
*  1. Loads in the original SDTM tv.sas7bdat data & the processed ADSL data
*  2. Uses that data to create the ADAE dataset
* 
*  For simplcity, we are going to mock the scenario by simply 
*  merging the datasets together
*****************************************************************************/
%include "/mnt/code/domino.sas";

options dlcreatedir;
libname inputs "/workflow/inputs"; /* All inputs live in this directory */ 
libname outputs "/workflow/outputs"; /* All outputs must go to this directory */ 

data outputs.advs;
    merge inputs.vs inputs.adsl;
run;

/* (Required) This line signals to Domino Flows that outputs were successfully created */
libname success "/workflow/outputs/_SUCCESS";

