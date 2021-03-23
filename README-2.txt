If for whatever reason the submitted code doesn't work, the backup github link is here:
https://github.com/smantri7/MGAFinalProject

To reproduce the data files, one should use GTGraph's Random Graph generator. I have included 2_5.txt and 2_6.txt just to make sure that the code runs appropriately. 

Go inside the ./StoerWagner directory

To Run the file, go to the command line:
Type: g++ graph.cpp -o main -std=c++14
Type(Windows): main.exe filename.txt OR Type (Linux): ./main filename.txt

Example:
main.exe ./data/2_5.txt
./main ./data/2_5.txt

Note: multiple input files can also be passed. E.g. ./main ./data/2_5.txt ./data/2_6.txt

To run the NetworkX and Igraph version, go to the ./Stoerwagner directory. Now do the following in the command line:
Type: py sw.py filename.txt

Note: multiple input files can also be passed. E.g. py sw.py ./data/2_5.txt ./data/2_6.txt
