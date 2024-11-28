import glob
import pandas as pd
import xml.etree.ElementTree as ET # parse the data from an XML file format.
from datetime import datetime

log_file = "log_file.txt"
target_file = "transform_data.csv"

def extract_from_csv(file_to_process):
    df = pd.read_csv(file_to_process)
    return df
def extract_from_json(file_to_process):
    df = pd.read_json(file_to_process, lines=True)
    return df

# must know the headers of the extracted data to write this function
def extract_from_xml(file_to_process):
    df = pd.DataFrame(columns=["name", "height", "weight"])

    tree = ET.parse(file_to_process)
    root = tree.getroot()

    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)

        df = pd.concat([df, pd.DataFrame([{"name": name, "height":height, "weight":weight}])], ignore_index = True)

    return df
def extract():
    extracted_data = pd.DataFrame(columns=["name", "height", "weight"])

    # process all csv files
    for csvfile in glob.glob("*.csv"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True)

    # process all json files
    for jsonfile in glob.glob("*.json"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True)

    # process all xml files
    for xmlfile in glob.glob("*.xml"):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True)
    
    
    return extracted_data

def transform(data):
    # convert inches to meters and round off to two decimals
    # 1 inches is 0.0254 meters
    data['height'] = round(data.height * 0.0254, 3)
    
    # convert pounds to kilograms and round off to two decimals
    # 1 pound is = 0.45359237

    data['weight'] = round(data.weight * 0.45359237, 3)

    return data

def load_data(target_file, tranformed_data):
    tranformed_data.to_csv(target_file)

def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # year month -day-hour-minute-second

    now = datetime.now() # get current timestamp


    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:
        f.write(timestamp+"," + message + "\n")



if __name__ == "__main__":
    log_progress("ETL job started") 
    
    log_progress("Extract phase started") 
    extracted_data = extract() 
    
    log_progress("Extract phase ended") 
    
    log_progress("Transform phase started") 
    transformed_data = transform(extracted_data) 
    print("Transformed data") 
    print(transformed_data) 
    
    log_progress("Transform phase ended") 
    
    log_progress("Load phase started") 
    load_data(target_file,transformed_data) 
    
    log_progress("Load phase ended") 
    
    log_progress("ETL Job ended") 


# result
# Transformed data
#      name  height  weight
# 0    alex   1.671  51.251
# 1    ajay   1.817  61.911
# 2   alice   1.763  69.413
# 3    ravi   1.733  64.564
# 4     joe   1.722  65.453
# 5    alex   1.671  51.251
# 6    ajay   1.817  61.911
# 7   alice   1.763  69.413
# 8    ravi   1.733  64.564
# 9     joe   1.722  65.453
# 10   alex   1.671  51.251
# 11   ajay   1.817  61.911
# 12  alice   1.763  69.413
# 13   ravi   1.733  64.564
# 14    joe   1.722  65.453
# 15   jack   1.745  55.928
# 16    tom   1.773  64.179
# 17  tracy   1.778  61.897
# 18   john   1.725  50.970
# 19   jack   1.745  55.928
# 20    tom   1.773  64.179
# 21  tracy   1.778  61.897
# 22   john   1.725  50.970
# 23   jack   1.745  55.928
# 24    tom   1.773  64.179
# 25  tracy   1.778  61.897
# 26   john   1.725  50.970
# 27  simon   1.725  50.970
# 28  jacob   1.696  54.735
# 29  cindy   1.689  57.810
# 30   ivan   1.718  51.773
# 31  simon   1.725  50.970
# 32  jacob   1.696  54.735
# 33  cindy   1.689  57.810
# 34   ivan   1.718  51.773
# 35  simon   1.725  50.970
# 36  jacob   1.696  54.735
# 37  cindy   1.689  57.810
# 38   ivan   1.718  51.773