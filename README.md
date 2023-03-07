# GitHub Codespaces ♥️ Jupyter Notebooks

Goal of the project is to calibrate the photodiodes. For that purpose, a absolutely calibrated PowerMeter is used to obtain the power W-V relationship thanks to the two beams after the beamsplitter. In this way, we know what power we expect to be reaching the PD, so that we can calibrated. The calibration of the PD is done thanks to the Rasberry. Note that in the data columns, we will either have PowerMeter+Keithley or Raspberry(PD)+Keithley.

Each of the used filters will be connected to a W-V relationship, as the effect of the filters is not linear but a convolution, so a different laser power is trasmited  (may we do a FFT of the signal to asses this? ). 


