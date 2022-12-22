"""
Given a set of investment projects with their respective profits, we need to
find the most profitable projects. We are given an initial capital and are allowed
to invest only in a fixed number of projects. Our goal is to choose projects that
give us the maximum profit. Write a function that returns the maximum total
capital after selecting the most profitable projects.

We can start an investment project only when we have the required capital.
Once a project is selected, we can assume that its profit has become our capital.

revisit : nail down heaps
"""

from typing import List
from collections import defaultdict


def get_project_map(project_capitals, project_profits):
    project_map = defaultdict(int)
    for index in range(len(project_capitals)):
        capital = project_capitals[index]
        profit = project_profits[index]
        project_map[capital] = profit
    return project_map


def get_next_profitable_project(project_capitals, total_capital):
    # find a project that's just below the total capital
    for i in range(len(project_capitals)):
        if i > total_capital:
            # as soon as the next value is great use the immediate previous project
            return project_capitals[i - 1]
    else:
        # if the loop completes with all projects being under the budget
        # then simply grab the last project in the list
        return project_capitals[-1]


def find_maximum_capital(
        project_capitals: List[int],
        project_profits: List[int],
        num_of_projects: int,
        initial_capital: int
    ):
    """
    1. create a project_map, mapping capital to project_profits
    2. instantiate total_capital and add initial capital to it
    3. use total_capital value to get project profit from the project_map
        1. this will return project profit
        2. add project profit to total_profit
    3. continue using total_capital to check if next project_capital is present in
        project_profits map
        1. if nothing is present return the total_capital
    Time: O(C^2 + P) | Space: O(C)
    """
    project_map = get_project_map(project_capitals, project_profits)
    total_capital = 0
    total_capital += initial_capital
    for _ in range(num_of_projects):
        project_profit = project_map.get(total_capital)
        if not project_profit:
            profitable_project = get_next_profitable_project(project_capitals, total_capital)
            project_profit = project_map[profitable_project]
        total_capital += project_profit
    return total_capital


def main():

    print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
