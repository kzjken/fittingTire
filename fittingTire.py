import glob
import os
import csv
import itertools

def initCSV(lstPar):
    lstTitle = ['TestNo.'], ['Long Vel (m/s)'], ['Rotation (rad/s)'], ['Slip Angle (rad)'], ['IA (rad)'], ['RI loaded'], ['Re effective rolling radius'], ['Gauge Pressure (Pa)'], ['Long Force (N)'], ['Lat Force (N)'], ['Vertical Force (N)'], ['Overturning Torque (Nm)'], ['Aligning Torque (Nm)'], ['Slip Ratio'], ['turn slip (1/m)'], ['Roll Resist Torque (Nm)'], [' '], ['Slip Angle (deg)'], ['Camber (deg)'], ['Gauge Pressure (kPa)'], ['Slip Ratio (%)'], 
    lstPar = []
    for title in lstTitle:
        # lstCol = []
        lstPar.append(title)
    return lstPar

def buildCSV(txtPath, lstPar):
    # print(txtPath)
    lstPar[0].append(os.path.basename(txtPath)[-7:-4])
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
                lstPar[4].append(str(float(slipAngle) * 3.14159 / 180))
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

# ask for src folder
srcPath = ""
try:
    srcPath = input("Source path = ")
except ValueError:
    print("error input!")

# srcPath = r'.\src'
lstTireFolder = glob.glob(srcPath + '\\*')

print('===================================================================================================================')
for folder in lstTireFolder:
    print(folder)
print(str(len(lstTireFolder)) + ' tire folders found.')

for tireFolder in lstTireFolder:
    print('===================================================================================================================')
    print('processing ' + tireFolder)
    suffix = os.path.basename(tireFolder)[3:]
    saveFolder = os.path.abspath(os.path.join(tireFolder, '../..')) + '\\rst\\' + suffix + '\\'
    print('saveFolder = ' + saveFolder)
    if not os.path.exists(saveFolder):
        os.makedirs(saveFolder)

    lstSubfolder = glob.glob(tireFolder + '\\*')
    # print(lstSubfolder)

    # glob all txt files in subfolder
    for idx, subfolder in enumerate(lstSubfolder):
        print('-------------------------------------------------------------------------------------------------------------------')
        print("Processing " + subfolder)
        lstTxt = glob.glob(subfolder + '\\**\\*.txt', recursive = True)    
        lstAvg = []
        lstMin = []
        lstMax = []

        subfolderPrefix = subfolder[-1]
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

        lstCsvMin = []
        lstCsvMin = initCSV(lstCsvMin)
        for txtMin in lstMin:
            lstCsvMin = buildCSV(txtMin, lstCsvMin)       
        saveCSV(saveFolder + subfolderPrefix + '_Min_' + suffix + '.csv', lstCsvMin)

        lstCsvMax = []
        lstCsvMax = initCSV(lstCsvMax)
        for txtMax in lstMax:
            lstCsvMax = buildCSV(txtMax, lstCsvMax)       
        saveCSV(saveFolder + subfolderPrefix + '_Max_' + suffix + '.csv', lstCsvMax)

print('===================================================================================================================')
print(str(len(lstTireFolder)) + ' tire folders processed.')
