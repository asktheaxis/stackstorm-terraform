from lib import action
import os

class Apply(action.BaseAction):
    def run(self, planpath):
      os.chdir(planpath)
      return self.terraform.apply(planpath)
