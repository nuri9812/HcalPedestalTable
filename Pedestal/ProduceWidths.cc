#include <vector>
#include <exception>
#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <cstdio>
#include <sstream>


void split(std::vector<std::string>& dest, const std::string& str, const char* delim)
{
	char* pTempStr = strdup(str.c_str());
	char* pWord = strtok(pTempStr, delim);
	while (pWord != NULL) {
		dest.push_back(pWord);
		pWord = strtok(NULL, delim);
	}
	free(pTempStr);
}


void ProduceWidths() {

	ifstream filePhase1;
	char fn1[100] = "nTuple_PedestalTable_interploated.txt";
	filePhase1.open(fn1);


	FILE *fto;
	if ((fto = fopen("nTuple_PedestalTable_interploated_Width.txt", "w")) == NULL) {         // Create new file
		printf("\nNo output file open => EXIT\n\n");
		return;
	}
	printf("\n\n output file open \n\n");

	char info[1024];
	//sprintf(info, "# %15s %15s %15s %15s %8s %8s %8s %8s %8s %8s %8s %8s %8s %8s %8s %8s %8s %8s %8s %8s %10s",    "eta", "phi", "dep", "det", "cov_0_0", "cov_0_1", "cov_0_2", "cov_0_3", "cov_1_0", "cov_1_1", "cov_1_2", "cov_1_3", "cov_2_0", "cov_2_1", "cov_2_2", "cov_2_3", "cov_3_0", "cov_3_1", "cov_3_2", "cov_3_3", "DetId");
	//fprintf(fto, "%s\n", info);

	const char *SubDet;
        const char *DetId;
	const char *item;
	int ieta, iphi, depth;
	float cov[4][4] = {0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0};
	char br[] = " ";

	while (filePhase1) {
		char buffer[1024];
		filePhase1.getline(buffer, 1024);
		cout << buffer << endl;
		if( buffer[0] == '#') fprintf(fto,"%s\n", buffer);
                else{
		std::vector <std::string> items;
		split(items, buffer, br);
		cout << items.size() << endl;

		if (items.size() > 0) {
			ieta = atoi(items[0].c_str());
			iphi = atoi(items[1].c_str());
			depth = atoi(items[2].c_str());
			SubDet = items[3].c_str();
			cov[0][0] = pow(atof(items[8].c_str()),2);
			cov[1][1] = pow(atof(items[9].c_str()),2);
			cov[2][2] = pow(atof(items[10].c_str()),2);
			cov[3][3] = pow(atof(items[11].c_str()),2);
                        DetId = items[12].c_str();
                        fprintf(fto, "%17d%16d%16d%16s %8.3f%8.3f%8.3f%8.3f %8.3f%8.3f%8.3f%8.3f %8.3f%8.3f%8.3f%8.3f %8.3f%8.3f%8.3f%8.3f %10s\n", ieta, iphi, depth, SubDet, cov[0][0], cov[0][1], cov[0][2], cov[0][3], cov[1][0], cov[1][1], cov[1][2], cov[1][3], cov[2][0], cov[2][1], cov[2][2], cov[2][3], cov[3][0], cov[3][1], cov[3][2], cov[3][3], DetId);
                        //}
		}//not empty lines
	        }	
	}

	fclose(fto);
}
