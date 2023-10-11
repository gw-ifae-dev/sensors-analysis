Variable that one could explore in this folder so far 
- Obtain the V-W relationship from test A
- Influence of RC filters when calibrating the PD (?)
- Influence of the gain when calibrating the PD (outer vs. external ring?)
- Angle of incidence measurements

---------------------------------------------------

The format of the files should follow: 

$TESTTYPE_$GCONFIGURATION_$SUBTESTTYPE_$TESTNUMBER_$FILENUMBER.txt 

The $subtype only applies if there is more of one type of similar tests.

The G configuration keyword denotes the gain of the amplifier.
- G=2 is the default configuration for all boards.
- G=4 is set for the boards located on the outer ring. 

Test in this folder are:

TEST A: Valid data are power meter (W) and keithley voltage (V). There were captured 8 files. They would be combined each other to improve statistics.
Naming: Monitor_Responsivity_1_0.txt to Monitor_Responsivity_1_7.txt

TEST B1: Valid data are keithley voltage (V) and raspberry (V). There were captured 9 files using G=2 configuration. 
Naming: PD_Responsivity_G2_1_1_0.txt to PD_Responsivity_G2_1_1_8.txt 

TEST B2: Same as B1 but include some RC filters.
Naming: PD_Responsivity_G2_2_1_0.txt to PD_Responsivity_G2_2_1_8.txt 

TEST C: Valid data are keithley voltage (V) and raspberry (V). There were captured 10 files using G=4 configuration (outer ring).
Naming: PD_Responsivity_G4_1_1_0.txt to PD_Responsivity_G4_1_1_9.txt (subtype index added so that RC may be tried)

TEST D: Valid data are keithley voltage (V) and raspberry (V). Angle of Incident test using G=2 configuration. 
It also include UTC time and temperatures.
Naming: PD_AoI_G2_1_0.txt 
 
 

