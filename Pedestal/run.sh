#!/bin/bash

#./run.sh <runNumber>

echo "start"
echo "it takes 5~10 minuit"

start=`date +%s.%N`


#cmsenv
#cp /eos/cms/store/group/dpg_hcal/comm_hcal/USC/run$1/USC_$1.root ./temp.root
#cmsRun HCALPFG/HcalTupleMaker/test/pfg_Local_Example.py 
#rm temp.root

#root -b -q $CMSSW_BASE'/src/Pedestal/HCALPFG/HcalPedestalTuning/HcalPedestalTable/HCALPedestalTableMaker.C++("'$CMSSW_BASE'/src/Pedestal/nTuple.root")' #update your path

python PedestalTableMakerHcalNano-pyRoot.py $1
echo "initial table is produced"

python3 interpolation.py PedestalTable.txt
echo "interploation is done"

cat PedestalTable_interploated.txt | grep -e HB -e HE >> PedestalTable_interploated_HBHE.txt
cat PedestalTable_interploated.txt | grep -e HF -e HO >> PedestalTable_interploated_HFHO.txt

mkdir Fig

root -b -q $CMSSW_BASE'/src/Pedestal/HCALPedestalAnalysis.C++("'$CMSSW_BASE'/src/Pedestal/PedestalTable_interploated_HBHE.txt",250,0,50,50,0,50 )' #update your path, [Max, Min, bins] for Mean plot, [Max, Min, bins] for width plot

mv Fig Fig_HBHE
mkdir Fig

root -b -q $CMSSW_BASE'/src/Pedestal/HCALPedestalAnalysis.C++("'$CMSSW_BASE'/src/Pedestal/PedestalTable_interploated_HFHO.txt",30,0,70,15,0,50)' #update your path
mv Fig Fig_HFHO

echo "plots for sanity check is produced"

root -b -q ProduceWidths.cc

echo "Pedestal Width is extracted"

finish=`date +%s.%N`
diff=$( echo "$finish - $start" | bc -l )

echo 'start at' $start
echo 'finish at' $finish
echo 'diff:' $diff
