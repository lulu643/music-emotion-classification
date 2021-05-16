import pandas as pd


def remove_characters(file):
    df = pd.read_csv(file)
    new_df = df[df.loc[:,'binary_label'].isin(['1', '-1'])]
    print(new_df.head())
    new_df.to_csv(file, encoding='utf-8')


def count_rows(file):
    df = pd.read_csv(file)
    print(file, df.shape)


def with_url(file):
    df = pd.read_csv(file)
    # print(df.iloc[[105], [17]])
    new_df = df[df.loc[:, 'preview_url'].notna()]
    new_df.to_csv(file[: -4]+'_with_audio.csv', encoding='utf-8', index=False)


def concatenate_files(file_lst):
    # combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in file_lst])
    # export to csv
    combined_csv.to_csv("all_data_ori.csv", index=False, encoding='utf-8')


def combine_happy_energetic(file):
    df = pd.read_csv(file)
    df.iloc[:, -1].replace(4, 3, inplace=True)
    df.to_csv(file, encoding='utf-8', index=False)


def add_new_sad_sons(infile, outfile):
    with open(infile,'r') as f1:
        with open(outfile, 'w') as f2:
            for line in f1:
                s1 = line.replace('https://open.spotify.com/track/', '')
                ind = s1.find('?si=')
                s = s1[:ind]
                f2.write(s+'\n')


if __name__ == '__main__':
    file_list = ['reserve/sad.csv', 'reserve/calm.csv',
                 'reserve/energetic.csv', 'reserve/happy.csv']
    combine_happy_energetic('reserve/happy.csv')
    concatenate_files(file_list)
