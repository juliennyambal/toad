import torch
from torch.nn import Module

from .functional import focalloss


class FocalLoss(Module):
    def __init__(self, alpha = 1., gamma = 2., reduction = 'mean'):
        super(FocalLoss, self).__init__()
        
        self.alpha = alpha
        self.gamma = gamma
        self.reduction = reduction

    def forward(self, input, target):
        return focalloss(
            input,
            target,
            alpha = self.alpha,
            gamma = self.gamma,
            reduction = self.reduction,
        )
        

