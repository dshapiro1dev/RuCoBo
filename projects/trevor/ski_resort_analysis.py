from ski_mountain_details import ski_mountain
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('resorts.csv')
    resort_data = df.to_dict()

    resort_data['summit'] = {}
    resort_data['drop'] = {}

    for row in resort_data['name']:
        print(f"Updating values for {resort_data['name'][row]} at {resort_data['link'][row]}... ", end='')
        my_mountain = ski_mountain(resort_data['link'][row])
        resort_data['summit'][row] = my_mountain.details['summit']
        resort_data['drop'][row] = my_mountain.details['drop']
        print(f"Success!")

    updated_df = pd.DataFrame(data=resort_data)
    file_name = "resort_details.csv"
    updated_df.to_csv(file_name)
    print(f"Ski resort data successfully updated and written to the file {file_name}.")
