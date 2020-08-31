'''
lebowski.py
@author Matt Paterson, hello@hireMattPaterson.com
'''

def scaled_data_split(dataframe, target):
    '''
    returns six dataframes and series, X_train, X_train_sc, 
            X_val, X_val_sc, y_train, y_val in that order
            for use in scaled classification models and NN
    df is a pandas dataframe
    target is a string literal, should exactly match the column header from
            the dataframe that will be the predicted class of the model
    Employs the train_test_split function and the StandardScalar() as well
    '''
    import pandas as pd
    from sklearn.preprocessing       import StandardScaler
    from sklearn.model_selection     import train_test_split
    
    X = dataframe.drop(columns='koi_disposition')
    y = dataframe['koi_disposition']

    X_train, X_val, y_train, y_val = train_test_split(X, y,
                                                      test_size = .2, 
                                                      random_state = 42, 
                                                      stratify=y)

    sc = StandardScaler()
    X_train_sc = sc.fit_transform(X_train)
    X_val_sc = sc.transform(X_val)
    
    return X_train, X_train_sc, X_val, X_val_sc, y_train, y_val

def waste(dataframe):
    '''
    unsure about what to do with this function, may delete
    '''
    return 0


def graph_words(word_color):
    '''
    establishes the word color for a graph to more easily transfer to ppt slides
    '''
    import matplotlib.pyplot as plt
    return plt.rcParams.update({'text.color' : word_color,
                     'axes.labelcolor' : word_color, 'xtick.color' : word_color,
                    'ytick.color' : word_color})

def count_chars(string):
    '''
    returns the total number of characters including spaces in a string literal
    string, a string
    '''
    count=0
    for s in string:
        count+=1
    return count

def word_count(string):
    '''
    returns the number of words or tokens in a string literal, splitting on spaces,
        regardless of word lenth.  This function will include space-separated
        punctuation as a word, such as " : " where the colon would be counted
    string, a string
    '''
    str_list = string.split()
    return len(str_list)


def create_lexicon(subreddit, db_length=1_000, size=500, post_type='submission'):
    '''
    returns a dataframe of the information found at the pushshift api for reddit
    subreddit, a string representing the name of the subreddit to scrape
    db_length, an int indicating how many rows in total to scrape
    size, an int, the size parameter in the api with a max of 500 rows
         note: This param is currently returning only 100 rows?
    post_type, a string, either 'submission' or 'comment' denoting nominal results

    errors: throws an exception if there is trouble connecting to the webpage
    errors: supresses an error if there are not enough posts to complete the function,
            in that case will store all available info and return a printed warning
    '''
    import requests
    import pandas as pd

    # instantiate an empty list to hold results
    result_list = []

    # establish the url to search
    url = 'https://api.pushshift.io/reddit/search/' + post_type

    # establish a set of parameters for use in the api
    params = {
    'subreddit' : subreddit,
    'size': 500
    }

    try:
        #print('Entering the Try statement, before while loop')
        while (len(result_list) < db_length):
            #print('TEST PRINT 1, enter the while loop')
            # get the posts from the subreddit
            url_relevant =  requests.get(url, params)
            # print the url status_code to make sure it's working
            if url_relevant.status_code>=200 & url_relevant.status_code<300:
                print('connection nominal')
            else:
                print('a connection error occurred, could not reach the api')
                return 0
            response = url_relevant.json()['data']

            # assign the posts to a list of dictionaries
            for row in response:
                result_list.append(row)
            print(f"Added in {len(response)} new rows")
            print(f"List contains {len(result_list)} rows")

            #Modify params to make sure we only read in posts we don't already have
            params['before'] = response[len(response)-1]['created_utc']
            #print('params dict now looks like this:', params)

        print(f'Succeffully created a list of {len(result_list)} total rows from r/{subreddit}')
    except:
        print("An error occurred, possibly there are not enough posts to scrape, \n\
        but maybe something completely different")

    # turn the list in to a dataframe
    print('Creating dataframe')
    df = pd.DataFrame(result_list)

    # print out the dataframe shape
    print('Printing dataframe shape:')
    print(df.shape)


    return df


def make_soup(url):
    '''
    returns a beautiful soup object
    url a string, the url where you will find the html

    prints a 200 code if all went well, a different code if the
           desired webpage had issues

    this function uses lxml as the html parser
    this function taken from Riley Dallas Class presentation snippets
    '''
    import requests
    from bs4 import BeautifulSoup

    url = url
    res = requests.get(url)
    print(res.status_code)
    return  BeautifulSoup(res.content, 'lxml')

def make_food(url, restaurants):
    '''
    this function created for lab 9 specifically, saving in case it can be useful
    returns a list of dictionaries of the food
    url: a string, the original url
    restaurants: a list of dictionaries containing the link to the restaurant's website

    PRINTOUT: Function will print out a 200 code if the href url is reached
              successfully, or an error code otherwise
    '''
    from bs4 import BeautifulSoup

    food = []
    for rest in restaurants:
        soup = make_soup(url + rest['href'])
        for i in range(1, len(soup.find_all('tr'))):
            food.append({
                'calories': soup.find_all('tr')[i].text.strip().split('\n')[2].lower(),
                'carbs': soup.find_all('tr')[i].text.strip().split('\n')[4].lower(),
                'category': soup.find_all('tr')[i].text.strip().split('\n')[1].lower(),
                'fat': soup.find_all('tr')[i].text.strip().split('\n')[3].lower(),
                'name': soup.find_all('tr')[i].text.strip().split('\n')[0].lower(),
                'restaurant': rest['name']
            })
    return food



def show_details(dataframe):
    print('Accessing quick look at {dataframe}')
    print('{dataframe}.head(2)\n>>>', dataframe.head(2))
    print('\n\n{dataframe}.isna().sum()\n>>>', dataframe.isna().sum())
    print('\n\n{dataframe}.info()\n>>>', dataframe.info())
    print('\n{dataframe}.shape', dataframe.shape)
    return None



def heatmap_this(df, features, title):
    # Heatmap style borrowed from Ryley Dallas
    '''
    returns 1 if no errors
        prints a heatmap of the correlations between all fields in a dataframe
    df, a pandas dataframe
    title, a string literal that will title the graph
    '''
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    word_color = 'black'
    plt.rcParams.update({'text.color' : word_color,
                     'axes.labelcolor' : word_color, 'xtick.color' : word_color,
                    'ytick.color' : word_color})


    plt.figure(figsize=(21, 12))
    sns.heatmap(df[features].corr(),
                annot=True,
               cmap='coolwarm',
               vmin=-1,
               vmax=1);
    plt.title(title)
    return None
