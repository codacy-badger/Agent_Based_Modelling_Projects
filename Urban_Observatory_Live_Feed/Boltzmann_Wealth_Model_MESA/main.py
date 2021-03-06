from MoneyModel import MoneyModel
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

all_wealth = []
#for j in range(100):
model = MoneyModel(50, 10, 10)
for i in range(100):
    model.step()
 #Store the results
for agent in model.schedule.agents:
    all_wealth.append(agent.wealth)

#Firstly we create an empty numpy array with the same size width and heigth
#as the grid. Then we populate this array with zeroes.
agent_counts = np.zeros((model.grid.width, model.grid.height))
# For each cell content in the grid,
for cell in model.grid.coord_iter():
    #cell_content, x and y variables store the content and cell coordinates i.e.
    # returned parameters [content, x coordinate, y coordinate]
    cell_content, x, y = cell
    # agent_count variable is initialised to the length of the cell_content variable.
    agent_count = len(cell_content)
    # Agent_counts variable is a 2D array which contains all the agents.
    agent_counts[x][y] = agent_count

# A dataframe of the model data collection variables which were the compute_gini method.
gini = model.datacollector.get_model_vars_dataframe()
agent_wealth = model.datacollector.get_agent_vars_dataframe()
# We can now create any form of graph/analysis method to analyse the agent_wealth.
end_of_simulation_wealth = agent_wealth.xs(99, level = "Step")["Wealth"]
#  Storing the agent_wealth data in a dataframe to a csv.
agent_wealth.to_csv("results/wealth_of_agents.csv")
# Store the gini coefficient of agents to csv.
gini.to_csv("results/gini_of_agents.csv")
# I decided to create a histogram of the agents wealth at the end of the simulation.
end_of_simulation_wealth.hist(bins = range(agent_wealth.Wealth.max() + 1))
plt.show()

# Create a heatmap of the agent counts on each grid cell
plt.imshow(agent_counts, interpolation='nearest')
plt.colorbar()
gini.plot()# Creating a plot of the gini coefficient data.
plt.show()
