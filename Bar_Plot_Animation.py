import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation


crypto_cap = pd.read_csv('crypto_market_cap.csv')  # Read CSV file

crypto_cap.index = crypto_cap['date']  # Set index as date index
crypto_cap = crypto_cap.drop(['date'], axis=1)  # Remove date column

crypto_cap1 = crypto_cap.T  # Get Transpose of DataFrame
crypto_cap1.index = crypto_cap1.index.str.upper()  # Covert coins names to uppercase

print(crypto_cap1.head())

Writer = animation.writers['ffmpeg']  # Select writer
writer = Writer(fps=20, metadata=dict(artist='Me'))  # Writer's parameters

fig, ax = plt.subplots(figsize=(16, 12))


def animate(i):  # Animation function

    data = crypto_cap1[crypto_cap1.columns[i]].astype(int).sort_values() / 1000000  # select data range

    ax.clear()  # clean ax to vaoid overlap
    data.plot(kind='barh', color='b', width=0.70)  # Horizantal bar plot
    ax.tick_params(labelsize=17)
    ax.set_facecolor('gray')  # Set background color
    ax.patch.set_alpha(0.7)

    ax.yaxis.grid(color='gray', linestyle='dashed')  # to make vertical grids
    ax.xaxis.grid(color='gray', linestyle='dashed')  # to make horizontal grids
    ax.spines['bottom'].set_color('yellow')  # to set x-axis color
    ax.spines['left'].set_color('yellow')  # to define y-axis color

    plt.title('Top 15 CryptoCurrencies Market Cap-wise', fontsize=20, color='g')
    plt.ylabel('Crypto Currency', fontsize=18, color='b')
    plt.xlabel('Market Capitalization [Millions USD]', fontsize=18, color='b')

    plt.text((data.max() * 0.85), 11, crypto_cap1.columns[i], horizontalalignment='center',\
             fontsize=24, color='c', bbox=dict(facecolor='k', edgecolor='y'))  # Add date
    plt.text((data.max() * 0.67), 0.0, 'Created by :\n                  Dayal Chand Aichara\n              \
    dc.aichara@lastroots.com ', fontsize=16, bbox=dict(facecolor='c', edgecolor='y'))  # add creator's information

    for i, h in enumerate(data):  # label bars
        ax.text(h - 1, i - 0.15, str(h), color='k', fontweight='bold', fontsize=14)


ani = animation.FuncAnimation(fig, animate, interval=100, frames=575, repeat=False)  # create animation
ani.save('crypto_market_cap.mp4')  # save Animation
plt.show()


