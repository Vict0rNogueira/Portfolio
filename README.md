# Portfólio Pessoal

Portfólio profissional para desenvolvedor, com foco em empregabilidade na área de tecnologia.

## Tecnologias

- **Backend:** Python (Flask)
- **Frontend:** HTML5, CSS3
- **JavaScript:** Mínimo (apenas para navbar responsiva)

## Estrutura do Projeto

```
/portfolio
├── app.py
├── requirements.txt
├── README.md
├── /templates
│   ├── base.html
│   ├── index.html
│   ├── projetos.html
│   └── contato.html
└── /static
    ├── /css
    │   └── style.css
    ├── /img
    └── /js
        └── main.js
```

## Como Rodar Localmente

### 1. Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

### 2. Instalação

```bash

cd portfolio

python -m venv venv


.\venv\Scripts\activate.bat


source venv/bin/activate


pip install -r requirements.txt
```

### 3. Executar

```bash
python app.py
```

### 4. Acessar

Abra o navegador em: **http://127.0.0.1:5000**


## Páginas

- **/** - Home com hero, habilidades e CTA
- **/projetos** - Lista de projetos em cards
- **/contato** - Links para WhatsApp, Instagram, LinkedIn e GitHub

## Licença

Uso livre para fins pessoais e profissionais.
