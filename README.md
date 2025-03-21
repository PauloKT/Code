# Como Fazer Pull e Push no Git

Este guia explica como enviar (push) e baixar (pull) alterações de um repositório Git no GitHub.

## 🔄 Atualizar o Repositório (Pull)
Se você deseja baixar as alterações mais recentes do repositório remoto para seu computador, use:
```bash
git pull origin master
```
Isso garante que você tenha a versão mais atualizada do código antes de fazer alterações.

## 📤 Enviar Alterações para o GitHub (Push)
Depois de modificar arquivos no seu repositório local, siga estes passos:

1. **Adicionar os arquivos modificados**:
   ```bash
   git add .
   ```
2. **Criar um commit com uma mensagem descritiva**:
   ```bash
   git commit -m "Descrição das alterações"
   ```
3. **Enviar as alterações para o GitHub**:
   ```bash
   git push origin main
   ```

Isso enviará seu código atualizado para o repositório remoto.

## ⚠️ Erros Comuns
- Se aparecer o erro `fatal: Authentication failed`, verifique se você está autenticado no GitHub.
- Se o repositório estiver desatualizado, use `git pull origin main` antes de fazer o push.

Agora você pode manter seu repositório sempre sincronizado! 🚀
