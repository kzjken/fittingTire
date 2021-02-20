import glob
import os
import csv
import itertools

def getProcNo(msg):    
    answer = input(msg) 
    try:
        return int(answer)
    except ValueError:
        print("Please input a number.")
        getProcNo(msg)    

def askYN(msg):
    answer = None
    while answer not in ("y", "n", "yes", "no"): 
        answer = input(msg) 
        if answer == "yes" or answer == "y" or answer == "Y"  or answer == "enter": 
            return True
        elif answer == "no" or answer == "n" or answer == "N": 
            return False
        else: 
            print("Please enter yes(y) or no(n)") 

def initCSV(lstPar):
    lstTitle = ['TestNo.'], ['Long Vel (m/s)'], ['Rotation (rad/s)'], ['Slip Angle (rad)'], ['IA (rad)'], ['RI loaded'], ['Re effective rolling radius'], ['Gauge Pressure (Pa)'], ['Long Force (N)'], ['Lat Force (N)'], ['Vertical Force (N)'], ['Overturning Torque (Nm)'], ['Aligning Torque (Nm)'], ['Slip Ratio'], ['turn slip (1/m)'], ['Roll Resist Torque (Nm)'], [' '], ['Slip Angle (deg)'], ['Camber (deg)'], ['Gauge Pressure (kPa)'], ['Slip Ratio (%)'], 
    lstPar = []
    for title in lstTitle:
        # lstCol = []
        lstPar.append(title)
    return lstPar

def buildCSV(txtPath, lstPar):
    # print(txtPath)
    lstPar[0].append(os.path.basename(txtPath)[14:-4])
    with open(txtPath, 'r') as txtFile:
        lineCount = 0
        for line in txtFile: 
            if lineCount == 9:
                lstPar[1].append(line.split('=',)[1].split('\n',)[0])
                # print(str(lineCount) + '. ' + line.split('=',)[0] + '=' + line.split('=',)[1].split('\n',)[0])
            if lineCount == 11:
                lstPar[2].append(line.split('=',)[1].split('\n',)[0])
                # print(str(lineCount) + '. ' + line.split('=',)[0] + '=' + line.split('=',)[1].split('\n',)[0])
            if lineCount == 37:
                lstPar[8].append(line.split('=',)[1].split('\n',)[0])
                # print(str(lineCount) + '. ' + line.split('=',)[0] + '=' + line.split('=',)[1].split('\n',)[0])
            if lineCount == 38:
                lstPar[9].append(line.split('=',)[1].split('\n',)[0])
                # print(str(lineCount) + '. ' + line.split('=',)[0] + '=' + line.split('=',)[1].split('\n',)[0])
            if lineCount == 36:
                lstPar[10].append(line.split('=',)[1].split('\n',)[0])
                # print(str(lineCount) + '. ' + line.split('=',)[0] + '=' + line.split('=',)[1].split('\n',)[0])
            if lineCount == 40:
                lstPar[11].append(line.split('=',)[1].split('\n',)[0])
                # print(str(lineCount) + '. ' + line.split('=',)[0] + '=' + line.split('=',)[1].split('\n',)[0])       
            if lineCount == 39:
                lstPar[12].append(line.split('=',)[1].split('\n',)[0])
                # print(str(lineCount) + '. ' + line.split('=',)[0] + '=' + line.split('=',)[1].split('\n',)[0])                           
            if lineCount == 41:
                lstPar[15].append(line.split('=',)[1].split('\n',)[0])
                # print(str(lineCount) + '. ' + line.split('=',)[0] + '=' + line.split('=',)[1].split('\n',)[0])              
            if lineCount == 17:
                slipAngle = line.split('=',)[1].split('\n',)[0]
                lstPar[17].append(slipAngle)
                lstPar[3].append(str(float(slipAngle) * 3.14159 / 180))
                # print(str(lineCount) + '. ' + line.split('=',)[0] + '=' + line.split('=',)[1].split('\n',)[0])              
            if lineCount == 19:
                slipRatio = line.split('=',)[1].split('\n',)[0]
                lstPar[18].append(slipRatio)
                lstPar[4].append(str(float(slipRatio) * 3.14159 / 180))
                # print(str(lineCount) + '. ' + line.split('=',)[0] + '=' + line.split('=',)[1].split('\n',)[0])              
            if lineCount == 20:
                gaugePressure = line.split('=',)[1].split('\n',)[0]
                lstPar[19].append(gaugePressure)
                lstPar[7].append(str(float(gaugePressure) * 1000))
                # print(str(lineCount) + '. ' + line.split('=',)[0] + '=' + line.split('=',)[1].split('\n',)[0])              
            if lineCount == 18:
                SlipRatioPer = line.split('=',)[1].split('\n',)[0]
                lstPar[20].append(SlipRatioPer)
                lstPar[13].append(str(float(SlipRatioPer) / 100))
                # print(str(lineCount) + '. ' + line.split('=',)[0] + '=' + line.split('=',)[1].split('\n',)[0])
            lineCount += 1
    
    return lstPar

def saveCSV(savePath, lstPar):
    with open(savePath, 'w', newline='') as file:      
        writer = csv.writer(file)
        writer.writerows(list(itertools.zip_longest(*lstPar, fillvalue='')))     

##################################################################################################################################################
# get src path
##################################################################################################################################################
srcPath = input("Source path = ")
if not os.path.isdir(srcPath):
    print(srcPath + ' is not a valid path, please re-input.')
    srcPath = input("Source path = ")
# srcPath = r'.\src'

print('===================================================================================================================')
lstTireFolder = glob.glob(srcPath + '\\*\\')
for idx, folder in enumerate(lstTireFolder):
    print(str(idx + 1) + '. ' + folder)
print(str(len(lstTireFolder)) + ' tire folder(s) found.\n')

##################################################################################################################################################
# process
##################################################################################################################################################
# processFlag = askYN("Process the tire folder(s): yes or no ? (y/n)")
selectedFolderIdx = getProcNo("Please select a folder with index number (0 for all): ")

procAllFlag = False
if selectedFolderIdx == 0:
    procAllFlag = True
selectedFolderIdx -= 1

for idx, tireFolder in enumerate(lstTireFolder):
    if idx == selectedFolderIdx or procAllFlag:
        print('===================================================================================================================')
        print('processing ' + tireFolder)
        suffix = os.path.basename(tireFolder[:-1])[3:]
        # print('suffix =' + suffix)
        saveFolder = os.path.abspath(os.path.join(tireFolder, '../..')) + '\\FittingTireRST\\' + suffix + '\\'
        print('saveFolder = ' + saveFolder)
        if not os.path.exists(saveFolder):
            os.makedirs(saveFolder)

        lstSubfolder = glob.glob(tireFolder + '\\*\\')
        # print(lstSubfolder)

        # glob all txt files in subfolder
        for idx, subfolder in enumerate(lstSubfolder):
            print('-------------------------------------------------------------------------------------------------------------------')
            print("Processing " + subfolder)
            lstTxt = glob.glob(subfolder + '\\**\\*.txt', recursive = True)    
            lstAvg = []
            lstMin = []
            lstMax = []

            subfolderPrefix = subfolder[-2]
            # print(subfolderPrefix)

            for txt in lstTxt:
                # print(os.path.basename(txt))   
                if 'Average' in os.path.basename(txt):
                    lstAvg.append(txt)
                if 'Minimum' in os.path.basename(txt):
                    lstMin.append(txt)
                if 'Maximum' in os.path.basename(txt):
                    lstMax.append(txt)

            lstCsvAvg = []
            lstCsvAvg = initCSV(lstCsvAvg)
            for txtAvg in lstAvg:
                lstCsvAvg = buildCSV(txtAvg, lstCsvAvg)       
            saveCSV(saveFolder + subfolderPrefix + '_Avg_' + suffix + '.csv', lstCsvAvg)
            print(saveFolder + subfolderPrefix + '_Avg_' + suffix + '.csv created.')

            lstCsvMin = []
            lstCsvMin = initCSV(lstCsvMin)
            for txtMin in lstMin:
                lstCsvMin = buildCSV(txtMin, lstCsvMin)       
            saveCSV(saveFolder + subfolderPrefix + '_Min_' + suffix + '.csv', lstCsvMin)
            print(saveFolder + subfolderPrefix + '_Min_' + suffix + '.csv created.')

            lstCsvMax = []
            lstCsvMax = initCSV(lstCsvMax)
            for txtMax in lstMax:
                lstCsvMax = buildCSV(txtMax, lstCsvMax)       
            saveCSV(saveFolder + subfolderPrefix + '_Max_' + suffix + '.csv', lstCsvMax)
            print(saveFolder + subfolderPrefix + '_Max_' + suffix + '.csv created.')
print('===================================================================================================================')
# print(str(len(lstTireFolder)) + ' tire folders processed.')

quitHold = input("Press any key to quit.") 


