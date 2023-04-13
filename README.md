# HcalPedestalTable
First, move pedestal to $CMSSWBASE/src


To produce a pedestal Mean/Width, interpolate missing channels, and Figures
you should update your path line in "run.sh". and then
```
run.sh <path to HcalNano>
```



To produce a pedestal Mean/Width from HcalNano,
```
python3 PedestalTableMakerHcalNano-pyRoot.py <path to HcalNano>
```

To find missing channels and interpolate them,
```
python3 interpolation.py <path to PedestalTable>
```

To make figures for a sanity check,
```
mkdir Fig
root -b -q 'HCALPedestalAnalysis.C++("<path to PedestalTable>", <bins1>,<min1>,<max1>,<bins2>,<min2>,<max2>)'
```
bins1, min1, max1 is number of bins, min, max for pedestal mean.
bins2, min2, max2 is number of bins, min, max for pedestal width.

To extract pedestal width from pedestal table,
```
root -b -q ProduceWidth.cc
```

