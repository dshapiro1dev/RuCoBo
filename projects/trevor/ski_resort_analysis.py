from ski_mountain_details import ski_mountain
import pandas as pd

if __name__ == "__main__":
    file_name = "resort_details.csv"
    df = pd.read_csv(file_name)
    resort_data = df.to_dict()

    for row in resort_data['name']:
        print(f"Updating values for {resort_data['name'][row]} at {resort_data['link'][row]}... ", end='')
        my_mountain = ski_mountain(resort_data['link'][row])
        resort_data['summit'][row] = my_mountain.details['summit']
        resort_data['drop'][row] = my_mountain.details['drop']
        resort_data['beginner runs'][row] = my_mountain.details['beginner runs']
        resort_data['intermediate runs'][row] = my_mountain.details['intermediate runs']
        resort_data['advanced runs'][row] = my_mountain.details['advanced runs']
        resort_data['expert runs'][row] = my_mountain.details['expert runs']
        resort_data['state'][row] = my_mountain.details['state']
        updated_df = pd.DataFrame(data=resort_data)
        updated_df.to_csv(file_name, index=False)
        print(f"Success!")

    print(f"Ski resort data successfully updated and written to the file {file_name}.")
