import webbrowser as wb
import pandas as pd
import time

# url = 'https://adb-4786482868192795.15.azuredatabricks.net/files/tables/a030Y00000Dc4JnQAJ.csv'
# wb.open(url)

# url = 'https://adb-4786482868192795.15.azuredatabricks.net/files/tables/a03P400000FmzdFIAR.csv'
# wb.open(url)

df = pd.read_csv('installations-logs_partition_1.csv')

for row in df.itertuples():
    # print(row.installations)
    url = 'https://adb-4786482868192795.15.azuredatabricks.net/files/tables/avg_bin_time/' + row.installation_id + '.csv'
    wb.open(url)
    time.sleep(0.3)

for row in df.itertuples():
    # print(row.installations)
    url = 'https://adb-4786482868192795.15.azuredatabricks.net/files/tables/dotw/' + row.installation_id + '.csv'
    wb.open(url)
    time.sleep(0.35)