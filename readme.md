# GERENCIADORES DE EVENTOS DO SISTEMA DE ARQUIVOS

## sobre watchdog: 🐶

- No Python, um módulo watchdog pode ser usado para monitorar nosso sistema de arquivos para alterações como criação, modificação, movimentação ou exclusão de um arquivo ou de um diretório.

- Quando ocorre uma mudança, o watchdog a relata para nós, gerando um evento específico que podemos gerenciar.

#### Usaremos a classe *FileSystemEventHandler* (gerenciador de eventos do sistema de arquivos) e a classe *Observer* (observador) do módulo watchdog.

- O watchdog.observers.Observer é a classe que procurará qualquer alteração no caminho fornecido. Ela chama o gerenciador de eventos específico com base nas alterações.
- O watchdog.events.FileSystemEventHandler é a classe do gerenciador de eventos que irá gerenciar os eventos do sistema de arquivos (como *criação, modificação, movimentação e exclusão de arquivos*).

## 
# instalações:
- pip install watchdog


##
#### Na classe FileSystemEventHandler, temos diferentes métodos para monitorar diferentes eventos:
● on_any_event(): é chamado para todos os
gerenciadores de eventos.

● on_created(): é chamado quando um arquivo ou
diretório é criado.

● on_modified(): é chamado quando um arquivo
ou diretório é modificado.

● on_moved(): é chamado quando um arquivo ou
diretório é movido ou renomeado.
● on_deleted(): é chamado quando um arquivo ou
diretório é excluído.
