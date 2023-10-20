import json

class Cliente:
  def __init__(self, id, nome, email, fone):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__fone = fone
  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_email(self): return self.__email
  def get_fone(self): return self.__fone
  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_email(self, email): self.__email = email
  def set_fone(self, fone): self.__fone = fone
  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__email == x.__email and self.__fone == x.__fone:
      return True
    return False 
  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

class NCliente:
  __clientes = []         # lista de clientes inicia vazia
  @classmethod
  def inserir(cls, obj):
    NCliente.abrir()
    id = 0 # encontrar o maior id já usado
    for cliente in cls.__clientes:
      if cliente.get_id() > id: id = cliente.get_id()
    obj.set_id(id + 1)
    cls.__clientes.append(obj)  # insere um cliente (obj) na lista
    NCliente.salvar()
  @classmethod
  def listar(cls):
    NCliente.abrir()    
    return cls.__clientes       # retorna a lista de clientes
  @classmethod
  def listar_id(cls, id):
    NCliente.abrir()
    for cliente in cls.__clientes:
      if cliente.get_id() == id: return cliente
    return None
  @classmethod
  def atualizar(cls, obj):
    NCliente.abrir()
    cliente = cls.listar_id(obj.get_id())
    if cliente is not None:
      cliente.set_nome(obj.get_nome())
      cliente.set_email(obj.get_email())
      cliente.set_fone(obj.get_fone())
      NCliente.salvar()
  @classmethod
  def excluir(cls, obj):
    NCliente.abrir()
    if cliente is not None:
      cliente = cls.listar_id(obj.get_id())
      cls.__clientes.remove(cliente)    
      NCliente.salvar()
  @classmethod
  def abrir(cls):
    try:
      cls.__clientes = []
      with open("clientes.json", mode="r") as f:
        s = json.load(f)
        for cliente in s:
          c = Cliente(cliente["_Cliente__id"], cliente["_Cliente__nome"],
                     cliente["_Cliente__email"], cliente["_Cliente__fone"])
          cls.__clientes.append(c)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as f:
      json.dump(cls.__clientes, f, default=vars, indent=4)