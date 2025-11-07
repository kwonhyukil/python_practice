import random
from typing import Any
from collections import OrderedDict

class Module:
  _parameters:OrderedDict
  
  def __init__(self, input: int, output: int) -> None:
    object.__setattr__(self, "_parameters", OrderedDict())
    self.weight = [ random.gauss(0, 1) for _ in range(input)]
    self.bias = [ random.gauss(0, 1) for _ in range(output)]
    
  def __setattr__(self, name: str, value: Any) -> None:
    # name -> weight or bias -> orderedDict 에 저장
    # 이외는 그냥 저장
    if name in ["weight", "bias"]:
      self._parameters[name] = value
      
    object.__setattr__(self, name, value)
    
  def __getattribute__(self, name: str) -> Any:
    if name in ["weight", "bias"]:
      return self._parameters[name]
    
    return self.name
  
  def parameters(self):
    
    return [(self.weight, self.bias)]
    
      
module = Module(3, 1)

for w, b in module.parameters():
  print(w, b)