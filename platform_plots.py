def pie_charts(NetflixDict, HuluDict, PrimeDict, DisneyDict, Title, Filename, NumSubplots, ExplodeList=[]):
    '''
    This function outputs a pie chart of the input DataDict and saves the figure under Filename
    :param DataDict: Dictionary of number of instances of each possible data value (e.g. {'Action Movies': 22, 'Comedy Movies': 43})
    :param Title: Title of figure
    :param Filename: Filename of saved pie chart figure
    :param NumSubplots: Number of subplots per figure
    :param ExplodeList: List of the amount of separation between pie slices in the pie chart (bigger values mean more separation)
    :type DataDict: dictionary 
    :type Title: string
    :type Filename: string
    :type ExplodeList: list
    '''
    assert isinstance(NetflixDict, dict), "Netflix data must be a dictionary"
    assert isinstance(HuluDict, dict), "Hulu data must be a dictionary"
    assert isinstance(PrimeDict, dict), "Prime data must be a dictionary"
    assert isinstance(DisneyDict, dict), "Disney data must be a dictionary"
    assert isinstance(Title, str), "Title must be a string"
    assert isinstance(Filename, str), "Filename must be a string"
    assert isinstance(NumSubplots, int), "NumSubplots must be an int"
    assert isinstance(ExplodeList, list), "ExplodeList must be a list"

    
    import matplotlib.pyplot as plt
    import matplotlib as mpl


    mpl.rcParams['font.size'] = 12.0

    # four subplots on one figure option
    if NumSubplots == 4:
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=[12, 10])
        # Netflix subplot 
        ax1.pie([float(Vals) for Vals in NetflixDict.values()], autopct="%.1f%%", labels=[NetLabels for NetLabels in NetflixDict], pctdistance=.8, labeldistance=1.1)
        ax1.set_title('Netflix Plot')
        # Hulu subplot 
        ax2.pie([float(Vals) for Vals in HuluDict.values()], autopct="%.1f%%", labels=[HuluLabels for HuluLabels in HuluDict], pctdistance=.8, labeldistance=1.1)
        ax2.set_title('Hulu Plot')
        # Prime subplot 
        ax3.pie([float(Vals) for Vals in PrimeDict.values()], autopct="%.1f%%", labels=[PrimeLabels for PrimeLabels in PrimeDict], pctdistance=.8, labeldistance=1.1)
        ax3.set_title('Prime Plot')
        # Disney subplot 
        ax4.pie([float(Vals) for Vals in DisneyDict.values()], autopct="%.1f%%", labels=[DisneyLabels for DisneyLabels in DisneyDict], pctdistance=.8, labeldistance=1.1)
        ax4.set_title('Disney Plot')
        plt.set_cmap('PuBuGn')
        # plt.title(Title, fontsize=18)
        fig.savefig(Filename + '.png')
    
    # option currently not used for any figures, but left in for team to decide if subplots with two figures on them could be used anywhere
    elif NumSubplots == 2:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[12, 10])
        ax1.pie([float(Vals) for Vals in NetflixDict.values()], explode=ExplodeList[0], autopct="%.1f%%", labels=[NetLabels for NetLabels in NetflixDict], pctdistance=0.8)
        ax1.set_title('Netflix Plot')
        # Hulu subplot 
        ax2.pie([float(Vals) for Vals in HuluDict.values()], explode=ExplodeList[1], autopct="%.1f%%", labels=[HuluLabels for HuluLabels in HuluDict], pctdistance=0.8)
        ax2.set_title('Hulu Plot')
        fig.savefig(Filename + '1.png')

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[12, 10])
        # Prime subplot 
        ax1.pie([float(Vals) for Vals in PrimeDict.values()], explode=ExplodeList[2], autopct="%.1f%%", labels=[PrimeLabels for PrimeLabels in PrimeDict], pctdistance=0.8)
        ax1.set_title('Prime Plot')
        # Disney subplot 
        ax2.pie([float(Vals) for Vals in DisneyDict.values()], explode=ExplodeList[3], autopct="%.1f%%", labels=[DisneyLabels for DisneyLabels in DisneyDict], pctdistance=0.8)
        ax2.set_title('Disney Plot')
        fig.savefig(Filename + '2.png')
    # one plot per figure option
    else:
        # Netflix Plot
        fig, ax1 = plt.subplots(figsize=[12,10])
        ax1.pie([float(Vals) for Vals in NetflixDict.values()], autopct="%.1f%%", labeldistance=1.16, labels=[NetLabels for NetLabels in NetflixDict], pctdistance=1.08)
        ax1.set_title('Netflix Plot')   
        fig.savefig(Filename + 'Netflix.png')

        # Hulu Plot
        fig, ax1 = plt.subplots(figsize=[12,10])
        ax1.pie([float(Vals) for Vals in HuluDict.values()], autopct="%.1f%%", labeldistance=1.16, labels=[HuluLabels for HuluLabels in HuluDict], pctdistance=1.08)
        ax1.set_title('Hulu Plot')   
        fig.savefig(Filename + 'Hulu.png')

        # Prime Plot
        fig, ax1 = plt.subplots(figsize=[12,10])
        ax1.pie([float(Vals) for Vals in PrimeDict.values()], autopct="%.1f%%", labeldistance=1.16, labels=[PrimeLabels for PrimeLabels in PrimeDict], pctdistance=1.08)
        ax1.set_title('Prime Plot')   
        fig.savefig(Filename + 'Prime.png')

        # Disney Plot
        fig, ax1 = plt.subplots(figsize=[12,10])
        ax1.pie([float(Vals) for Vals in DisneyDict.values()], autopct="%.1f%%", labeldistance=1.16, labels=[DisneyLabels for DisneyLabels in DisneyDict], pctdistance=1.08)
        ax1.set_title('Disney Plot')   
        fig.savefig(Filename + 'Disney.png')

def bar_charts(StreamingPlatform, Data1, Data1Name, Filename):
    '''
    This function makes a bar graph with x-values=StreamingPlatform and y-values=Data1
    :param StreamingPlatform: list of streaming platforms
    :param Data1: List containing data on one attribute of each streaming platform
    :param Data1Name: Name of attribute in Data1 (e.g. "Popular Movie Count")
    :param Filename: Filename of saved bar chart 
    :type StreamingPlatform: list of strings
    :type Data1: list 
    :type Data1Name: string
    :type Filename: string
    '''
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    assert isinstance(StreamingPlatform, list), "StreamingPlatform must be a list"
    assert isinstance(Data1, list), "Data1 must be a list"
    assert isinstance(Filename, str), "Filename must be a string"
    assert isinstance(Data1Name, str), "Data1Name must be a string"

    Colors = ["#546e3d", "#c86a3d", "#e39e63", "#ffe5bd", "#f5e7b7"]
    sns.set(rc={'axes.facecolor': Colors[4], 'figure.facecolor': Colors[4]})

    plt.figure()
    FinalDataStruct = pd.DataFrame({"Streaming Platform": StreamingPlatform, Data1Name: Data1})
    BarChartFig = sns.barplot(x="Streaming Platform", y=Data1Name, data=FinalDataStruct, palette="Blues_d", alpha=.5)
    plt.savefig(Filename)

def scatter_plots(Data1, Data1Name, Filename, Data2=[], Data2Name="", PlotFlag=4):
    '''
    This function makes a scatter plot with the x-values being the different streaming platforms Data1
    is associated with, and the y-values (Data1) being the attribute we want to compare between streaming platforms 
    (e.g. make plot of all IMDB scores of the movies on Netflix, Hulu, Prime, Disney+). 
    Data2 is an optional argument which adds a third dimension to the plot: the colors of the 
    points are tied to another attibute (e.g. point is red if movie is rated 13+, point is blue if movie is rated 18+, etc)
    Note: order of streaming platforms in Data1 and Data2 must be Netflix, Hulu, Prime, Disney+

    :param Data1: List of lists containing data on one attribute of each streaming platform 
    :param Data1Name: Name of attribute in Data1 (e.g. "IMDB Scores")
    :param Filename: Filename of saved scatter plot 
    :param Data2: List of lists containing data on one attribute of each streaming platform 
    :param Data2Name: Name of attribute in Data2 (e.g. "Ages")
    :param PlotFlag: Specifies how many plots to have on one figure. Can take on value 1 or 4.
    :type Data1: List of lists
    :type Data1Name: String
    :type Filename: String
    :type Data2: List of lists
    :type Data2Name: String
    :type PlotFlag: int
    '''
    assert isinstance(Data1, list), "Data1 must be a list"
    assert isinstance(Data2, list), "Data2 must be a list"
    assert isinstance(Filename, str), "Filename must be a string"
    assert isinstance(Data1Name, str), "Data1Name must be a string"
    assert isinstance(Data2Name, str), "Data2Name must be a string"
    assert isinstance(PlotFlag, int), "Data2Name must be a string"
    assert PlotFlag == 1 or PlotFlag == 4, "PlotFlag can only take on values 1 or 4 currently"

    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.set(rc={'figure.figsize':(18, 10)})

    # Create array with colors to use
    Colors = ["#3D5941", "#748666", "#CA562C", "#E49E6E", "#f5e7b7"] # Jake added Colors[-1] because this is the background of the slides
    # Set custom color palette
    sns.set(rc={'axes.facecolor': Colors[4], 'figure.facecolor': Colors[4], "grid.linewidth":1, "grid.color": 'k'})
    sns.set_palette(sns.color_palette(Colors))

    if PlotFlag == 1:
        StreamingPlatform1 = ["Netflix"]*len(Data1[0]) 
        StreamingPlatform2 = ["Hulu"]*len(Data1[1])
        StreamingPlatform3 = ["Prime"]*len(Data1[2])
        StreamingPlatform4 = ["Disney+"]*len(Data1[3])

    if Data2:
        if PlotFlag == 4:
            StreamingPlatform = sum([["Netflix"]*len(Data1[0]), ["Hulu"]*len(Data1[1]), ["Prime"]*len(Data1[2]), ["Disney+"]*len(Data1[3])], [])
            Data1 = sum(Data1, [])
            Data2 = sum(Data2, [])
    # Make data into long-form structure for seaborn plotting
    # this case makes it so that swarm plots are plotted on four separate plots
    if PlotFlag == 1:
        if Data2:
            FinalDataStruct1 = pd.DataFrame({"Streaming Platform": StreamingPlatform1, Data1Name: Data1[0], Data2Name: Data2[0]})
            FinalDataStruct2 = pd.DataFrame({"Streaming Platform": StreamingPlatform2, Data1Name: Data1[1], Data2Name: Data2[1]})
            FinalDataStruct3 = pd.DataFrame({"Streaming Platform": StreamingPlatform3, Data1Name: Data1[2], Data2Name: Data2[2]})
            FinalDataStruct4 = pd.DataFrame({"Streaming Platform": StreamingPlatform4, Data1Name: Data1[3], Data2Name: Data2[3]})
        else:
            FinalDataStruct1 = pd.DataFrame({"Streaming Platform": StreamingPlatform1, Data1Name: Data1[0]})
            FinalDataStruct2 = pd.DataFrame({"Streaming Platform": StreamingPlatform1, Data1Name: Data1[1]})
            FinalDataStruct3 = pd.DataFrame({"Streaming Platform": StreamingPlatform1, Data1Name: Data1[2]})
            FinalDataStruct4 = pd.DataFrame({"Streaming Platform": StreamingPlatform1, Data1Name: Data1[3]})

        plt.figure()
        swarm_plot = sns.swarmplot(x="Streaming Platform", y=Data1Name, hue_order=["18+", "13+", "7+", "all"], hue=Data2Name, data=FinalDataStruct1, size=5)
        IMDBScatter = swarm_plot.get_figure()
        swarm_plot.set_xlabel("")
        swarm_plot.set_ylabel(Data1Name,fontsize=20)
        swarm_plot.tick_params(labelsize=20)
        IMDBScatter.savefig(Filename+str(1)+".png") 

        plt.figure()
        swarm_plot = sns.swarmplot(x="Streaming Platform", y=Data1Name, hue_order=["18+", "13+", "7+", "all"], hue=Data2Name, data=FinalDataStruct2, size=5) #alpha=.9
        IMDBScatter = swarm_plot.get_figure()
        swarm_plot.set_xlabel("")
        swarm_plot.set_ylabel(Data1Name,fontsize=20)
        swarm_plot.tick_params(labelsize=20)
        IMDBScatter.savefig(Filename+str(2)+".png") 

        plt.figure()
        swarm_plot = sns.swarmplot(x="Streaming Platform", y=Data1Name, hue_order=["18+", "13+", "7+", "all"], hue=Data2Name, data=FinalDataStruct3, size=5)
        IMDBScatter = swarm_plot.get_figure()
        swarm_plot.set_xlabel("")
        swarm_plot.set_ylabel(Data1Name,fontsize=20)
        swarm_plot.tick_params(labelsize=20)
        IMDBScatter.savefig(Filename+str(3)+".png") 

        plt.figure()
        swarm_plot = sns.swarmplot(x="Streaming Platform", y=Data1Name, hue_order=["18+", "13+", "7+", "all"], hue=Data2Name, data=FinalDataStruct4, size=5)
        IMDBScatter = swarm_plot.get_figure()
        swarm_plot.set_xlabel("")
        swarm_plot.set_ylabel(Data1Name,fontsize=20)
        swarm_plot.tick_params(labelsize=20)
        plt.legend(fontsize='15', title_fontsize='20')
        IMDBScatter.savefig(Filename+str(4)+".png") 
    # this case is for all four swarm plots to be on the same figure
    if PlotFlag == 4:
        if Data2:
            FinalDataStruct = pd.DataFrame({"Streaming Platform": StreamingPlatform, Data1Name: Data1, Data2Name: Data2})
            plt.figure()
            swarm_plot = sns.swarmplot(x="Streaming Platform", y=Data1Name, hue_order=["18+", "13+", "7+", "all"], hue=Data2Name, data=FinalDataStruct, size=4.7)
            IMDBScatter = swarm_plot.get_figure()
            swarm_plot.set_xlabel("")
            swarm_plot.set_ylabel(Data1Name,fontsize=20)
            swarm_plot.tick_params(labelsize=20)
            plt.legend(fontsize='15', title_fontsize='20')
            IMDBScatter.savefig(Filename+".png") 

def stacked_bar_chart(NetflixDict, HuluDict, PrimeDict, DisneyDict, Filename):
    '''
    This function creates a stacked bar chart figure
    :param NetflixDict: dictionary containing Netflix data to be plotted
    :param HuluDict: dictionary containing Hulue data to be plotted
    :param PrimeDict: dictionary containing Prime data to be plotted
    :param DisneyDict: dictionary containing Disney data to be plotted
    :param Filename: name of saved figure file
    :type NetflixDict: dictionary
    :type HuluDict: dictionary
    :type PrimeDict: dictionary
    :type DisneyDict: dictionary
    :type Filename: string
    '''
    assert isinstance(NetflixDict, dict), "NetflixDict must be a dictionary"
    assert isinstance(HuluDict, dict), "HuluDict must be a dictionary"
    assert isinstance(PrimeDict, dict), "PrimeDict must be a dictionary"
    assert isinstance(DisneyDict, dict), "DisneyDict must be a dictionary"
    assert isinstance(Filename, str), "Filename must be a string"
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np
        
    labels = set(sum([list(NetflixDict.keys()), 
                        list(HuluDict.keys()), 
                        list(PrimeDict.keys()), 
                        list(DisneyDict.keys())], []))

    NetflixVals = [NetflixDict[key] if key in NetflixDict.keys() else 0 for key in labels]
    HuluVals = [HuluDict[key] if key in HuluDict.keys() else 0 for key in labels]
    PrimeVals = [PrimeDict[key] if key in PrimeDict.keys() else 0 for key in labels]
    DisneyVals = [DisneyDict[key] if key in DisneyDict.keys() else 0 for key in labels]
    width = 0.35

    Colors = ["#964B00", "#F27900", "#FF9021", "#FFA74F", "#CE5F34", 
              "#D36D41", "#DC8556", "#E7A575", "#EEC08F", "#F0CB9B",
              "#F1D2A1", "#D5D3A7", "#B5B991", "#9EA782", "#7B8B6B", 
              "#607659", "#435E45", "#f5e7b7"]
    
    fig, ax = plt.subplots()
    sns.set(rc={'axes.facecolor': Colors[17], 'figure.facecolor': Colors[17], "grid.linewidth":1, "grid.color": 'k'})
    sns.set_palette(sns.color_palette(Colors))

    LangBottom = np.array([0, 0, 0, 0])
    # streaming platform on x-axis
    for lang in range(len(labels)):
        if all(LangBottom) == 1:
            ax.bar(["Netflix", "Hulu", "Prime", "Disney"], [NetflixVals[lang], HuluVals[lang], PrimeVals[lang], DisneyVals[lang]], width, label=list(labels)[lang])
            LangBottom = np.array([NetflixVals[lang], HuluVals[lang], PrimeVals[lang], DisneyVals[lang]])
        else:
            ax.bar(["Netflix", "Hulu", "Prime", "Disney"], [NetflixVals[lang], HuluVals[lang], PrimeVals[lang], DisneyVals[lang]], width, bottom=LangBottom, label=list(labels)[lang])
            LangBottom = LangBottom + np.array([NetflixVals[lang], HuluVals[lang], PrimeVals[lang], DisneyVals[lang]])
        
    ax.set_ylabel('Number of Movies', fontsize=17)
    ax.set_title('')
    ax.legend()
    plt.savefig(Filename) 
    
