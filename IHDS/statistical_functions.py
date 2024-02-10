# Should automatically do statiscal analysis on a dataset and break it down for me, have a UI very simmilar to Office 365, and be able to answer questions
import numpy as np

class QAgent:
    def __init__(self, statesByActions, discountFactor, learningRate) -> None:
        self.board = np.zeros(statesByActions)
        self.discount = discountFactor
        self.lr = learningRate
    
    def learn(self, state, action, nextState, reward):
        stateAndAction = state + action
        self.board[stateAndAction] = self.board[stateAndAction] + self.lr * (reward + self.discount * max(self.board[nextState]) - self.board[stateAndAction])
        