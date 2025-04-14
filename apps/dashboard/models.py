from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Material(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    unidade = models.CharField(max_length=10)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_estoque = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Orcamento(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    valor_total = models.DecimalField(max_digits=12, decimal_places=2)
    valor_realizado = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orçamento {self.projeto.nome}"

class SolicitacaoCompra(models.Model):
    numero = models.CharField(max_length=20)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(default=timezone.now)
    status = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitação {self.numero}"

class Cotacao(models.Model):
    solicitacao = models.ForeignKey(SolicitacaoCompra, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    prazo_entrega = models.IntegerField()  # em dias
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cotação {self.solicitacao.numero} - {self.fornecedor.nome}"

class PedidoCompra(models.Model):
    numero = models.CharField(max_length=20)
    cotacao = models.ForeignKey(Cotacao, on_delete=models.CASCADE)
    data_pedido = models.DateField()
    data_entrega = models.DateField()
    status = models.CharField(max_length=50)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.numero}" 