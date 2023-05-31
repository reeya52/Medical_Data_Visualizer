import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("C:/Users/Reeya/OneDrive/Desktop/Learning/medical_examination.csv")

# Add 'overweight' column
overweight_values = []
bmi = df["weight"]/np.square((df["height"]*0.01))
for bmi_value in bmi.values:
    if bmi_value > 25:
        overweight_values.append(1)
    else:
        overweight_values.append(0)

df['overweight'] = overweight_values

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = np.where(df["cholesterol"] == 1, 0, 1)
df["gluc"] = np.where(df["gluc"] == 1, 0, 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars="cardio", value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    # print(df_cat)


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")

    # Draw the catplot with 'sns.catplot()'
    plot = sns.catplot(data=df_cat, x="variable", y="total", kind="bar", col="cardio", hue="value")


    # Get the figure for the output
    fig = plot.fig


    # Do not modify the next two lines
    fig.savefig('C:/Users/Reeya/OneDrive/Desktop/Learning/catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (10,10))

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(corr, mask=mask, vmin=-0.08, vmax=0.24, annot=True, fmt='0.1f')

    # Do not modify the next two lines
    fig.savefig('C:/Users/Reeya/OneDrive/Desktop/Learning/heatmap.png')
    return fig


if __name__ == "__main__":
    draw_cat_plot()
    draw_heat_map()