#!/bin/bash

#./run.sh <runNumber>

echo 'It takes about 5~10 minuet...'
start=`date +%s.%N`


#cmsenv
#cp /eos/cms/store/group/dpg_hcal/comm_hcal/USC/run$1/USC_$1.root ./temp.root
#cmsRun HCALPFG/HcalTupleMaker/test/pfg_Local_Example.py 
#rm temp.root

#root -b -q $CMSSW_BASE'/src/Pedestal/HCALPFG/HcalPedestalTuning/HcalPedestalTable/HCALPedestalTableMaker.C++("'$CMSSW_BASE'/src/Pedestal/nTuple.root")' #update your path

python PedestalTableMakerHcalNano-pyRoot.py $1
echo "initial table is produced"
python3 interpolation.py nTuple_PedestalTable.txt
echo "missing channel interpolation is done"
cat nTuple_PedestalTable_interploated.txt | grep -e HB -e HE >> nTuple_PedestalTable_interploated_HBHE.txt
cat nTuple_PedestalTable_interploated.txt | grep -e HF -e HO >> nTuple_PedestalTable_interploated_HFHO.txt

mkdir Fig

root -b -q $CMSSW_BASE'/src/Pedestal/HCALPFG/HcalPedestalTuning/HcalPedestalTable/HCALPedestalAnalysis.C++("'$CMSSW_BASE'/src/Pedestal/nTuple_PedestalTable_interploated_HBHE.txt",250,0,50,50,0,50 )' #update your path, [Max, Min, bins] for Mean plot, [Max, Min, bins] for width plot

mv Fig Fig_HBHE
mkdir Fig

root -b -q $CMSSW_BASE'/src/Pedestal/HCALPFG/HcalPedestalTuning/HcalPedestalTable/HCALPedestalAnalysis.C++("'$CMSSW_BASE'/src/Pedestal/nTuple_PedestalTable_interploated_HFHO.txt",30,0,70,15,0,50)' #update your path
mv Fig Fig_HFHO

echo 'plots for saniti check is produced'
root -b -q ProduceWidths.cc

echo 'pedestal width is extracted'
finish=`date +%s.%N`
diff=$( echo "$finish - $start" | bc -l )

echo 'start:' $start
echo 'finish:' $finish
echo 'diff:' $diff
