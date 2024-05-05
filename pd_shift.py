import pandas

data_file = r'c:\data_folder\programming\data\train_5000.csv'

data = pandas.read_csv(data_file)

print(data)

d = {'x': [1, 2, 3, 4, 5],
     'y': [2, None, 10, None, 17]}

test_df = pandas.DataFrame(d)
interpolated_test_df = test_df.interpolate()
print(test_df)

chunks = pandas.read_csv(data_file, chunksize=1000)
for chunk in chunks:
     print(chunk)