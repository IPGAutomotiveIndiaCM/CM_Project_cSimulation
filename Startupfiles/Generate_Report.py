import os
import cmerg
import pandas as pd
#loading .erg file folder 
folder_path = '/opt/SimResults/$timestamp'
erg_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.erg')]
results = []

# Loop through each .erg file and process the data
for file_name in erg_files:
    # Construct the file paths
    old_file_path = os.path.join(folder_path, file_name)
    new_file_path = os.path.join(folder_path, file_name)  # Assuming the file is not renamed

    # Rename the file (same name for now, modify if needed)
    os.rename(old_file_path, new_file_path)
    print(f'Renamed: {file_name} -> {file_name}')

    # Convert .erg file to a pandas DataFrame
    df_result = cmerg.ERG(new_file_path).to_pd()
    print(df_result.columns)

    # Extract data from the DataFrame
    time = df_result["Time_s"].to_numpy()
    velocity = df_result["Car.v_m/s"].to_numpy()
    sensor = df_result["Sensor.Collision.Vhcl.Fr1.Count_"].to_numpy()
    distance = df_result["Car.Distance_m"].to_numpy()
    i = 0
    I = 0
    hit_status = "Test_Case_Passed"
    t1=0
    #Extract overall simualtion time 
    for j in range(len(time)):
        pass
    print(time[j])
    t1=time[j]   
    #Extract time when test_case Failed
    for j in range(len(time)):
        if sensor[j] == 1:
            print(time[j])
            t1=time[j]
            # print("hit")
            hit_status = "Test_Case_Failed"
            break
    # Add a dictionary with file information to the 'results' list
    results.append({
        'File Name': file_name,
        'Hit Status': hit_status,
        'Time': t1, 
    })

    print(f"File: {file_name}, Hit Status: {hit_status}")
    print("*********")

# Convert the results into a pandas DataFrame
df_results = pd.DataFrame(results)

# Define the HTML content (including the results)
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simulation Report</title>
    <style>
        body {{
            text-align: center;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        table {{
            width: 100%;
            margin-top: 20px;
            border-collapse: collapse;
        }}
        table, th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>IPG CarMaker Simulation Report</h1>
        <p>This report summarizes the results of the collision detection during the simulation.</p>

        <table>
            <thead>
                <tr>
                    <th>TestRun_Name</th>
                    <th>Test_Case</th>
                    <th>Time (s)</th>
                </tr>
            </thead>
            <tbody>
"""
# Iterate over each row in the DataFrame 'df_results'
for _, row in df_results.iterrows():
    # Set the hit_class based on the 'Hit Status' column of the current row
    hit_class = 'Test_Case_Passed' if row['Hit Status'] == 'Test_Case_Passed' else 'Test_Case_Failed'
    # Append an HTML table row for the current row's data
    html_content += f"""
                <tr>
                    <td>{row['File Name']}</td>
                    <td class="{hit_class}">{row['Hit Status']}</td>
                    <td>{row['Time']}</td>
                </tr>
"""
html_content += """
            </tbody>
        </table>
    </div>
</body>
</html>
"""
with open("simulation_report.html", "w") as file:
    file.write(html_content)

print("HTML file created successfully with detailed simulation results!")

