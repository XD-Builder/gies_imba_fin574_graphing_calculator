"""Main module."""
from math import ceil
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from pydantic import BaseModel
from typing import Dict

LABEL_OFFSET = 3

class EquationsDefinition(BaseModel):
    demands: Dict[str, str]
    supplies: Dict[str, str]

def draw_graph(eq_defs: EquationsDefinition):
    # Convert the string equations to lambda functions for evaluation
    mapped_demands = dict((key, lambda x, value=value: eval(value, {'x': x})) for key, value in eq_defs.demands.items())
    mapped_supplies = dict((key, lambda x, value=value: eval(value, {'x': x})) for key, value in eq_defs.supplies.items())

    # Use the values for y-axis labeling and x-axis labeling
    y_axis_labels = [mapped_demands[key](0) for key in mapped_demands.keys()]
    x_axis_labels = [fsolve(lambda x: mapped_demands[key](x), 0) for key in mapped_demands.keys()]

    # Find max points that touches x axis and y axis
    max_demand_x = max(x_axis_labels)

    # Generate 100 points for quantity on the x-axis to the largest demand touching x curve
    x = np.linspace(0, max_demand_x, 100)

    # Plot the demand and supply curves using relative size in inches
    fig, ax = plt.subplots(figsize=(14, 10))

    for k, v in mapped_demands.items():
        # Filter x values where demand is positive
        x_positive_demand = x[v(x) >= 0]
        y_positive_demand = v(x_positive_demand)
        ax.plot(x_positive_demand, y_positive_demand, label=k)

        # Position the label to the right of the curve end
        end_index = np.argmax(x_positive_demand)  # Find index of the maximum x value
        ax.text(x_positive_demand[end_index], y_positive_demand[end_index - LABEL_OFFSET], f'{k}', ha='left', va='center')

    ## y axis is always positive
    for k,v in mapped_supplies.items():
        ax.plot(x, v(x), label=k)

        # Position the label to the right of the curve end
        end_index = np.argmax(x)  # Find index of the maximum x value
        ax.text(x[end_index], v(x[end_index - LABEL_OFFSET]), f'{k}', ha='left', va='center')

    # Find and plot the equilibrium point for each demand and supply curve
    for demand_key, demand_func in mapped_demands.items():
        for supply_key, supply_func in mapped_supplies.items():
            def equation_to_solve(q):
                return demand_func(q) - supply_func(q)

            q_eq = float(fsolve(equation_to_solve, 20))  # Calculate equilibrium quantity as a float
            p_eq = float(demand_func(q_eq))  # Calculate equilibrium price as a float
            ax.plot(q_eq, p_eq, marker='o', markersize=8, label=f'Equilibrium {demand_key}/{supply_key}')

            # Plot dotted lines from the equilibrium point to the x-axis and y-axis
            ax.plot([0, q_eq], [p_eq, p_eq], 'b--')  # Dotted line to the x-axis
            ax.plot([q_eq, q_eq], [0, p_eq], 'b--')  # Dotted line to the y-axis

            # Annotate the intersection points with their exact values
            ax.text(0, p_eq, f'  {p_eq:.2f}', ha='right', va='center', color='blue')  # Label for y-axis intersection
            ax.text(q_eq, 0, f'  {q_eq:.2f}', ha='center', va='bottom', color='blue')  # Label for x-axis intersection

    # After the line plots, use the flattened arrays for setting ticks
    x_axis_labels_flat = np.array(x_axis_labels).ravel()
    y_axis_labels_flat = np.array(y_axis_labels).ravel()

    # Set x-axis tick labels for all ticks (existing + new)
    all_x_axis_labels = np.concatenate([ax.get_xticklabels(), [f'{label:.2f}' for label in x_axis_labels_flat]])
    ax.set_xticklabels(all_x_axis_labels)

    # Add new x-axis ticks to the existing ticks
    existing_x_ticks = ax.get_xticks()
    new_x_ticks = np.concatenate([existing_x_ticks, x_axis_labels_flat])
    ax.set_xticks(new_x_ticks)

    # Set y-axis tick labels for all ticks (existing + new)
    all_y_axis_labels = np.concatenate([ax.get_yticklabels(), [f'{label:.2f}' for label in y_axis_labels_flat]])
    ax.set_yticklabels(all_y_axis_labels)

    # Add new y-axis ticks to the existing ticks
    existing_y_ticks = ax.get_yticks()
    new_y_ticks = np.concatenate([existing_y_ticks, y_axis_labels_flat])
    ax.set_yticks(new_y_ticks)

    # Add labels and legend
    ax.set_xlabel('Quantity')
    ax.set_ylabel('Price')
    ax.set_title('Graphing Calculator')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend()

    # Set x-axis start at 0
    ax.set_xlim(left=0, right=max_demand_x * 1.1)
    ax.set_ylim(bottom=0)

    # Display the plot
    plt.show()
