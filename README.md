# Photodiode calibration project

Goal of the project is to calibrate the photodiodes. For that purpose, a absolutely calibrated PowerMeter is used to obtain the power W-V relationship thanks to the two beams after the beamsplitter. In this way, we know what power we expect to be reaching the PD, so that we can calibrated. The calibration of the PD is done thanks to the Rasberry. Note that in the data columns, we will either have PowerMeter+Keithley or Raspberry(PD)+Keithley.

Each of the used filters will be connected to a W-V relationship, as the effect of the filters is not linear but a convolution, so a different laser power is trasmited  (may we do a FFT of the signal to asses this? ). 


<img width="919" alt="Screenshot 2023-03-07 at 17 59 54" src="https://user-images.githubusercontent.com/126777371/223494247-fd1b9d37-e637-4d06-90f8-156da6a4d00e.png">

Calibration constant to be given as $\mu$ W/m +- E. The uncertainty budget, whose quadratic sum is E, include various sources of uncertainties, as geometrical aspects, power stability aspects, and dependency with the temperature. Then, we can look into the contributions from laser, dark-current, readout noise. 

Possible incoming tests to reach a robust characterization: 
- Dark Current (current in absence of light). Jorge suspects that it is higher that it should be as it is not well polarised (3.3 V for the p-n junction instead of 10-12V), so that some current is still flowing to the small energy gap of the semiconductor. 
- Laser ON. 
- Angle of incidence 
