function mergeficheros(list_ficheros)

fidlist=fopen(list_ficheros); %the list of files must contain the entire filepath
tline=fgetl(fidlist);
nfil=0;
while tline ~= -1
nfil=nfil+1;
file{nfil}=tline;
tline=fgetl(fidlist);
end

T=table();

for i=1:nfil
    Ti=readtable(file{i});

%check table size
if height(Ti)~=100 || width(Ti)~=10
    Ti
    disp('WARNING:The size of the table is not standard, check the file')
else
    disp('Table ok')
end

Ti.Properties.VariableNames{1} = 'date'; %string day/month/year
Ti.Properties.VariableNames{2} = 'time'; %HH:MM:SS
Ti.Properties.VariableNames{3} = 'LCurrent'; %mA
Ti.Properties.VariableNames{4} = 'meanPM'; %W
Ti.Properties.VariableNames{5} = 'stdPM'; %W
Ti.Properties.VariableNames{6} = 'meanRefPD'; %V
Ti.Properties.VariableNames{7} = 'stdRefPD'; %V
Ti.Properties.VariableNames{8} = 'Temp'; %Celsius
Ti.Properties.VariableNames{9} = 'RH'; %percentage
Ti.Properties.VariableNames{10} = 'samples';
    
T=[T;Ti];

end


K=unique(T.LCurrent);
Tk=table();
Tav=table();
for i=1:length(K)
mask=T.LCurrent==K(i);
sum(mask)

%T(mask,:)

Tk.LCurrent=mean(T(mask,:).LCurrent);
Tk.avPM=mean(T(mask,:).meanPM);
Tk.stdPM=std(T(mask,:).meanPM);
Tk.avRPD=mean(T(mask,:).meanRefPD);
Tk.stdRPD=std(T(mask,:).meanRefPD);

Tk.Temp=mean(T(mask,:).Temp);
Tk.RH=mean(T(mask,:).RH);


Tav=[Tav;Tk];

end



save T