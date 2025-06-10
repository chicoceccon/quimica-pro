# 🧪 Química Pro - Sistema Completo

Sistema completo de resolução de questões de química com IA, upload de imagens e monetização.

## 🚀 Funcionalidades

### ✅ Sistema de Usuários
- Cadastro e login
- Planos: Gratuito, Estudante, Premium
- Controle de questões restantes
- Painel administrativo

### ✅ Resolução Inteligente
- IA avançada para química
- Suporte a múltiplos tópicos:
  - Massa molar e fórmulas
  - Concentrações (M, m, g/L)
  - pH, pOH e soluções tampão
  - Balanceamento de equações
  - Estequiometria
  - Hibridização e geometria molecular
  - Mecanismos de reação (SN1, SN2)
  - Cinética química
  - Termoquímica

### ✅ Upload de Imagens
- Análise visual de exercícios
- Suporte: JPG, PNG, GIF, WebP
- Redimensionamento automático
- Preview e miniaturas

### ✅ Interface Moderna
- Design responsivo
- Bootstrap 5
- Drag & drop para imagens
- Histórico completo
- Dashboard com estatísticas

## 🛠️ Tecnologias

- **Backend:** Flask + SQLite
- **Frontend:** Bootstrap 5 + jQuery
- **Upload:** Pillow para processamento
- **Deploy:** Render + Gunicorn

## 📦 Instalação Local

```bash
pip install -r requirements.txt
python app.py
```

## 🌐 Deploy no Render

1. Conecte repositório GitHub
2. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Python Version: 3.11.0

## 👤 Usuários de Teste

- **Admin:** admin@quimicapro.net.br / admin123
- **Usuário:** Criar novo cadastro

## 📊 Planos

- **Gratuito:** 5 questões/mês
- **Estudante:** 100 questões/mês - R$ 9
- **Premium:** Ilimitado - R$ 19

## 🔧 Configuração

Arquivo principal: `app.py`
Templates: `templates/`
Estáticos: `static/`

Sistema pronto para produção!

