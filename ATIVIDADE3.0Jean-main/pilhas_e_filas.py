from lista_ligada import LinkedList
class Pilha:
    def _init_(self):
        self.lista = LinkedList()

class Pilha:
    def __init__(self):
        self.lista = LinkedList()

    def push(self, valor):
        self.lista.inserir_inicio(valor)

    def pop(self):
        tamanho = self.lista.tamanho()
        if tamanho == 0:
            return None
        return self.lista.remove_indice(tamanho - 1)

    def search(self, item):
        return self.lista.procura(item)

class Fila:

    def __init__(self):
        self.lista = LinkedList()
    
    def Enfila(self, item):
        self.lista.inserir_fim(item)

    def Desenfila(self):
        if self.lista.esta_vazio():
            return None
        return self.lista.remove_indice(0)

    def search(self, item):
        return self.lista.procura(item)