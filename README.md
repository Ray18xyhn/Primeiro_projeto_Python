# Registro de Trabalhos - App feito com Flet

Este é um aplicativo simples feito em **Python com Flet**. Desenvolvi especialmente para o meu pai, que trabalhava como operador de máquina e precisava de uma forma prática de registrar os serviços que realizava.

Inicialmente, criamos uma planilha, mas como o uso era mais frequente no celular, surgiu a ideia de transformar isso em um app.

## Funcionalidades
- Cadastro de registros de trabalho
- Interface simples adaptada para uso no celular
- Armazenamento local com SQLite

## Como executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/Primeiro_projeto_Python.git
cd Primeiro_projeto_Python/app
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o app:
```bash
python main.py
```

## Estrutura do projeto
```
app/
├── main.py
├── assets/
│   ├── components.py
│   ├── database.py
│   ├── icon.png
│   ├── fonts/
│   └── page/
├── Dados/
```

## Tecnologias usadas
- [Flet](https://flet.dev)
- SQLite
- Python 3.12
