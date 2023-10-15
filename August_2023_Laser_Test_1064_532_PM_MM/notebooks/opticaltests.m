function opticaltests(filename,id)
T=readtable(filename);

%check table size
if height(T)~=100 || width(T)~=10
    T
    disp('WARNING:The size of the table is not standard, check the file')
else
    disp('Table ok')
end

T.Properties.VariableNames{1} = 'date'; %string day/month/year
T.Properties.VariableNames{2} = 'time'; %HH:MM:SS
T.Properties.VariableNames{3} = 'LCurrent'; %mA
T.Properties.VariableNames{4} = 'meanPM'; %W
T.Properties.VariableNames{5} = 'stdPM'; %W
T.Properties.VariableNames{6} = 'meanRefPD'; %V
T.Properties.VariableNames{7} = 'stdRefPD'; %V
T.Properties.VariableNames{8} = 'Temp'; %Celsius
T.Properties.VariableNames{9} = 'RH'; %persentage
T.Properties.VariableNames{10} = 'smaples';


figure(id), errorbar(T.LCurrent,T.meanPM,T.stdPM, '.','MarkerSize',10,'LineWidth',1),
ylabel('Mean Optical Power (W)');
xlabel('Amplitude (mA)');hold on;

figure(id+1), errorbar(T.LCurrent,T.meanRefPD,T.stdRefPD, '.','MarkerSize',10,'LineWidth',1),
ylabel('Mean ref PD (V)');
xlabel('Amplitude (mA)'); hold on;

figure(id+2), errorbar(T.meanRefPD,T.meanPM,T.stdPM, '.','MarkerSize',10,'LineWidth',1),
ylabel('Mean Optical Power (W)');
xlabel('Mean ref PD (V)'); hold on;


% for i=1:10
% filename=['Laser_532_Step_50_Temp_20_PM_MM_G_',int2str(i),'.txt']
% opticaltests(filename,1)
% end

