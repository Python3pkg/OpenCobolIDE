******************************************************************
* Author: Colin Duquesnoy
* Date: 23/02/2014
* Purpose: Hello world world example mean to test parser with a
* FREE syntax.
* Tectonics: cobc
******************************************************************
IDENTIFICATION DIVISION.
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
PROGRAM-ID. YOUR-PROGRAM-NAME.
ENVIRONMENT DIVISION.
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
CONFIGURATION SECTION.
*-----------------------
INPUT-OUTPUT SECTION.
*-----------------------
DATA DIVISION.
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
FILE SECTION.
*-----------------------
WORKING-STORAGE SECTION.
*-----------------------
PROCEDURE DIVISION.
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
MAIN-PROCEDURE.
**
* The main procedure of the program
**
DISPLAY "Hello world"
STOP RUN.
** add other procedures here
END PROGRAM YOUR-PROGRAM-NAME.
