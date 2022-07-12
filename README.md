## Pessoa

#### POST /pessoa

_Formato da requisição_

```json
{
  "nome": "teste",
  "cpf": "12345678901",
  "dataNascimento": "2002/12/02"
}
```

_Formato de resposta_

```json
{
  "cpf": "12345678901",
  "dataNascimento": "Mon, 02 Dec 2002 00:00:00 GMT",
  "idPessoa": 1,
  "nome": "teste"
}
```

## Conta

#### POST /conta

_Formato da requisição_

```json
{
  "cpf": "12345678901"
}
```

_Formato de resposta_

```json
{
  "dataCriacao": "Fri, 08 Jul 2022 00:00:00 GMT",
  "flagAtivo": true,
  "idConta": 1,
  "idPessoa": 1,
  "limiteSaqueDiario": 1000.0,
  "saldo": 0.0,
  "tipoConta": 1
}
```

#### PATCH /conta/saldo/:idConta

_Formato da requisição_

```json
{
  "saldo": 125.1
}
```

_Formato de resposta_

```json
125.1
```

#### PATCH /conta/saque/:idConta

_Formato da requisição_

```json
{
  "saque": 125.1
}
```

_Formato de resposta_

```json
0.0
```

#### PATCH /conta/bloqueio/:idConta

_Formato de resposta_

```json
{
  "dataCriacao": "Fri, 08 Jul 2022 00:00:00 GMT",
  "flagAtivo": false,
  "idConta": 1,
  "idPessoa": 1,
  "limiteSaqueDiario": 1000.0,
  "saldo": 0.0,
  "tipoConta": 1
}
```

#### GET /conta/saldo/:idConta

_Formato de resposta_

```json
0.0
```

#### GET /conta/transacao/:idConta

_Formato de resposta_

```json
[
  {
    "dataTransacao": "Fri, 08 Jul 2022 00:00:00 GMT",
    "idConta": 1,
    "idTransacao": 27,
    "valor": 125.1
  },
  {
    "dataTransacao": "Fri, 08 Jul 2022 00:00:00 GMT",
    "idConta": 1,
    "idTransacao": 28,
    "valor": -125.1
  }
]
```
